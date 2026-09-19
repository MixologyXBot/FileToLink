"""Plugin registry lookup, offline builders, host validation."""

import pytest

from Thunder.utils.shortener import (
    BitlyPlugin,
    CuttLyPlugin,
    GenericShortenerPlugin,
    LinkvertisePlugin,
    OuoIoPlugin,
    ShortenerSystem,
)


@pytest.mark.unit
@pytest.mark.parametrize(
    "domain,expected",
    [
        ("bitly.com", BitlyPlugin),
        ("shrinkme.dev", GenericShortenerPlugin),  # generic fallback
        ("bitly.com.evil.com", GenericShortenerPlugin),  # lookalike rejected
    ],
)
def test_registry_lookup(domain, expected):
    system = ShortenerSystem()
    assert system._get_plugin_class(domain) is expected


@pytest.mark.unit
async def test_linkvertise_offline_constructor():
    plugin = LinkvertisePlugin()
    out = await plugin.shorten(None, "https://example.com/file", "12345", "linkvertise.com")
    assert any(
        out.startswith(prefix)
        for prefix in (
            "https://link-to.net/",
            "https://up-to-down.net/",
            "https://direct-link.net/",
            "https://file-link.net/",
        )
    )
    assert "12345" in out


@pytest.mark.unit
@pytest.mark.parametrize(
    "short_url,domain,expected",
    [
        ("https://shrinkme.dev/xAbc", "shrinkme.dev", True),
        ("https://evil.example/xAbc", "shrinkme.dev", False),
        ("https://shrinkme.dev.evil.io/xAbc", "shrinkme.dev", False),
    ],
)
def test_host_validation(short_url, domain, expected):
    assert GenericShortenerPlugin._validate_short_url(short_url, domain) is expected


@pytest.mark.unit
async def test_short_url_passthrough_when_not_ready():
    system = ShortenerSystem()
    assert await system.short_url("https://example.com") == "https://example.com"


@pytest.mark.unit
async def test_cache_hit_is_returned_without_http():
    system = ShortenerSystem()
    system.ready = True
    system._cache["https://long.example/a"] = "https://shrinkme.dev/xyz"
    assert await system.short_url("https://long.example/a") == "https://shrinkme.dev/xyz"


@pytest.mark.unit
@pytest.mark.parametrize(
    "domain,plugin,expected",
    [
        # legit hosts match (exact, subdomain, FQDN trailing dot)
        ("bitly.com", BitlyPlugin, True),
        ("bit.ly", BitlyPlugin, True),
        ("www.bit.ly", BitlyPlugin, True),
        ("bit.ly.", BitlyPlugin, True),
        ("linkvertise.com", LinkvertisePlugin, True),
        ("sub.linkvertise.com", LinkvertisePlugin, True),
        ("ouo.io", OuoIoPlugin, True),
        ("cutt.ly", CuttLyPlugin, True),
        # lookalikes that substring matching used to accept must not match
        ("evil.com/bitly.com", BitlyPlugin, False),
        ("bitly.com.evil.com", BitlyPlugin, False),
        ("notbitly.com", BitlyPlugin, False),
        ("bit.ly.evil.io", BitlyPlugin, False),
        ("evillinkvertise.com", LinkvertisePlugin, False),
        ("linkvertise.com.evil.net", LinkvertisePlugin, False),
        ("ouo.io.evil.dev", OuoIoPlugin, False),
        ("cutt.ly.evil.org", CuttLyPlugin, False),
        # cross-provider isolation
        ("ouo.io", BitlyPlugin, False),
        ("bit.ly", OuoIoPlugin, False),
    ],
)
def test_plugin_host_matching(domain, plugin, expected):
    assert plugin.matches(domain) is expected


@pytest.mark.unit
def test_vercel_protection_roundtrip():
    import hashlib
    import json
    import time
    from base64 import urlsafe_b64decode, urlsafe_b64encode

    secret_key = "my_vercel_secret_passphrase"
    payload = {
        "url": "https://shrinkme.dev/abc1234",
        "exp": int(time.time()) + 86400,
        "padding_data": "a" * 3300,
    }
    key_hash = hashlib.sha256(secret_key.encode()).digest()
    token = urlsafe_b64encode(
        bytes(c ^ key_hash[i % 32] for i, c in enumerate(json.dumps(payload).encode()))
    ).decode()

    # Decrypt
    decrypted_bytes = bytes(
        c ^ key_hash[i % 32] for i, c in enumerate(urlsafe_b64decode(token.encode()))
    )
    restored = json.loads(decrypted_bytes.decode())
    assert restored["url"] == payload["url"]
    assert restored["exp"] == payload["exp"]
    assert restored["padding_data"] == "a" * 3300


@pytest.mark.unit
async def test_vercel_protection_short_url_applied(monkeypatch):
    import hashlib
    import json
    from base64 import urlsafe_b64decode

    from Thunder.vars import Var

    monkeypatch.setattr(Var, "VERCEL_PROTECT_ENABLED", True)
    monkeypatch.setattr(Var, "VERCEL_PROTECT_KEY", "super_secret_key")
    monkeypatch.setattr(Var, "VERCEL_DOMAIN", "edge.vercel.app")
    monkeypatch.setattr(Var, "TOKEN_TTL_SECONDS", 3600)

    system = ShortenerSystem()
    system.ready = True
    system._cache["https://long.example/movie.mp4"] = "https://short.io/m1"

    short_link = await system.short_url("https://long.example/movie.mp4", user_id=554433)
    assert short_link.startswith("https://edge.vercel.app/token/__554433__/")

    token = short_link.split("/")[-1]
    key_hash = hashlib.sha256(b"super_secret_key").digest()
    decrypted_bytes = bytes(
        c ^ key_hash[i % 32] for i, c in enumerate(urlsafe_b64decode(token.encode()))
    )
    restored = json.loads(decrypted_bytes.decode())
    assert restored["url"] == "https://short.io/m1"
    assert len(restored["padding_data"]) == 3300


@pytest.mark.unit
async def test_vercel_protection_disabled(monkeypatch):
    from Thunder.vars import Var

    monkeypatch.setattr(Var, "VERCEL_PROTECT_ENABLED", False)

    system = ShortenerSystem()
    system.ready = True
    system._cache["https://long.example/movie.mp4"] = "https://short.io/m1"

    short_link = await system.short_url("https://long.example/movie.mp4", user_id=554433)
    assert short_link == "https://short.io/m1"
