# Thunder/utils/messages.py

# =====================================================================================
# ====== ERROR MESSAGES ======
# =====================================================================================

# ------ General Errors ------
MSG_ERROR_GENERIC = "⚠️ **Oops!** Something went wrong. Please try again. If the issue persists, contact support."
MSG_ERROR_USER_INFO = "❗ **User Not Found:** Couldn't find user. Please check the ID or Username."
MSG_ERROR_INVALID_ARG = "❗ Please provide a valid Telegram user ID or username."
MSG_ERROR_RATE_LIMIT = "⏳ **Slow Down!** Too many requests. Please wait `{seconds}` seconds."
MSG_ERROR_PRIVATE_CHAT_ONLY = "⚠️ **Private Chat Only:** This command works only in a private chat with me."

# ------ User Input & Validation Errors ------
MSG_INVALID_USER_ID = "❌ **Invalid User ID:** Please provide a numeric user ID."
MSG_ERROR_START_BOT = "⚠️ You need to start the bot in private first to use this command.\n👉 [Click here]({invite_link}) to start a private chat."
MSG_ERROR_REPLY_FILE = "⚠️ Please use the /link command in reply to a file."
MSG_ERROR_NO_FILE = "⚠️ The message you're replying to does not contain any file."
MSG_ERROR_INVALID_NUMBER = "⚠️ **Invalid number specified.**"
MSG_ERROR_NUMBER_RANGE = "⚠️ **Please specify a number between 1 and 100.**"
MSG_ERROR_DM_FAILED = "⚠️ I couldn't send you a Direct Message. Please start the bot first."

# ------ File & Media Errors ------
MSG_ERROR_FILE_INVALID = "🚫 **File Error:** Invalid file. It might be deleted or inaccessible."
MSG_ERROR_FILE_INVALID_ID = "🚫 **File Error:** Invalid file. It might be deleted or inaccessible. Please provide a valid message ID from the bot's storage channel."
MSG_ERROR_LINK_GENERATION = "⚠️ **Link Generation Failed!** 🔗 Unable to create links for this file. It might be inaccessible or corrupted."
MSG_ERROR_FILE_ID_EXTRACT = "⚠️ **File Error:** Could not extract file identifier from the media. Please try sending the file again."
MSG_MEDIA_ERROR = "⚠️ **Media Error:** The file appears to be empty or corrupted. Please try sending a valid file."
MSG_ERROR_PROCESSING_MEDIA = "⚠️ **Oops!** Something went wrong while processing your media. Please try again. If the issue persists, contact support."
MSG_ERROR_CHANNEL_BANNED = "🚫 **Channel Banned:** Files from this channel are blocked."
MSG_ERROR_NO_MEDIA_FOUND = "⚠️ **No Media Found:** Please send or reply to a valid media file."
MSG_FILE_ACCESS_ERROR = "⚙️ **Error Retrieving File!** Could not fetch details. File might be unavailable, ID incorrect, or deleted from storage."

# ------ Admin Action Errors (Ban, Auth, etc.) ------
MSG_BAN_ERROR = "🚨 **Ban error:** {error}"
MSG_UNBAN_ERROR = "🚨 **Unban error:** {error}"
MSG_AUTHORIZE_FAILED = (
    "❌ **Authorization Failed:** "
    "Could not authorize user `{user_id}`."
)
MSG_DEAUTHORIZE_FAILED = (
    "❌ **Deauthorization Failed:** "
    "User `{user_id}` was not authorized or an error occurred."
)
MSG_TOKEN_FAILED = (
    "⚠️ **Token Activation Failed!**\n\n"
    "> ❗ Reason: {reason}\n\n"
    "🔑 Please check your token or contact support."
)
MSG_TOKEN_ERROR = "⚙️ **Token Activation Error:** Something went wrong. Please try again."
MSG_SHELL_ERROR = """**❌ Shell Command Error ❌**
<pre>{error}</pre>"""
MSG_SHELL_LARGE_OUTPUT = """Output is too large, sending as a file.
Error: {error}"""

# ------ System & Bot Errors ------
MSG_ERROR_NOT_ADMIN = "⚠️ **Admin Required:** I need admin privileges to work here."
MSG_DC_INVALID_USAGE = "🤔 **Invalid Usage:** Please reply to a user's message or a media file to get DC info."
MSG_DC_ANON_ERROR = "😥 **Cannot Get Your DC Info:** Unable to identify you. This command might not work for anonymous users."
MSG_DC_FILE_ERROR = "⚙️ **Error Getting File DC Info:** Could not fetch details. File might be inaccessible."
MSG_STATS_ERROR = "❌ **Stats Error:** Could not retrieve system statistics."
MSG_STATUS_ERROR = "❌ **Status Error:** Could not retrieve system status."
MSG_DB_ERROR = "❌ **Database Error:** Could not retrieve user count."
MSG_LOG_ERROR = "❌ **Log Retrieval Error:** Could not get logs\n\n> ❗ Error: `{error}`"
MSG_RESTART_FAILED = "❌ **Restart Failed:** Could not reboot the bot."
MSG_CRITICAL_ERROR = (
    "🚨 **Critical Media Processing Error** 🚨\n\n"
    "> ⚠️ Details:\n```\n{error}\n```\n\n"
    "Please investigate immediately! (ID: {error_id})"
)

# =====================================================================================
# ====== ADMIN MESSAGES ======
# =====================================================================================

# ------ Ban/Unban ------
MSG_DECORATOR_BANNED = "You are currently banned and cannot use this bot.\nReason: {reason}\nBanned on: {ban_time}"
MSG_BAN_USAGE = "⚠️ **Usage:** /ban [user_id] [reason]"
MSG_CANNOT_BAN_OWNER = "❌ **Cannot ban an owner.**"
MSG_ADMIN_USER_BANNED = "✅ **User {user_id} has been banned."
MSG_BAN_REASON_SUFFIX = "\n📝 **Reason:** {reason}"
MSG_ADMIN_NO_BAN_REASON = "No reason provided"
MSG_USER_BANNED_NOTIFICATION = "🚫 **You have been banned from using this bot.**"
MSG_COULD_NOT_NOTIFY_USER = "⚠️ Could not notify user {user_id}: {error}"
MSG_UNBAN_USAGE = "⚠️ **Usage:** /unban <user_id>"
MSG_ADMIN_USER_UNBANNED = "✅ **User {user_id} has been unbanned."
MSG_USER_UNBANNED_NOTIFICATION = "🎉 **You have been unbanned from using this bot.**"
MSG_USER_NOT_IN_BAN_LIST = "ℹ️ **User {user_id} was not found in the ban list."

# ------ Token & Authorization ------
MSG_TOKEN_DISABLED = "🚫 **Token System Disabled:** This feature is not currently enabled."
MSG_AUTHORIZE_USAGE = "🔑 **Usage:** `/authorize <user_id>`"
MSG_DEAUTHORIZE_USAGE = "🔒 **Usage:** `/deauthorize <user_id>`"
MSG_AUTHORIZE_SUCCESS = (
    "✅ **User Authorized!**\n\n"
    "> 👤 User ID: `{user_id}`\n"
    "> 🔑 Access: Permanent"
)
MSG_DEAUTHORIZE_SUCCESS = (
    "✅ **User Deauthorized!**\n\n"
    "> 👤 User ID: `{user_id}`\n"
    "> 🔒 Access: Revoked"
)
MSG_TOKEN_ACTIVATED = (
    "✅ **Token Activated Successfully!**\n\n"
    "> 🗓️ Access granted until: **{expiry_date}**\n"
    "> 📝 Details: _{description}_\n\n"
    "✨ Enjoy all the features!"
)
MSG_TOKEN_VERIFIED = "🎉 **Token Verified!** You're all set to use the bot's features."
MSG_TOKEN_INVALID = "🚫 **Expired or Invalid Token.** Please get a new token to continue."
MSG_NO_AUTH_USERS = "ℹ️ **No Authorized Users Found:** The list is currently empty."
MSG_AUTH_USER_INFO = """{i}. 👤 User ID: `{user_id}`
   • Authorized by: `{authorized_by}`
   • Date: `{auth_time}`\n\n"""
MSG_ADMIN_AUTH_LIST_HEADER = "🔐 **Authorized Users List**\n\n"

# ------ Shell Commands ------
MSG_SHELL_USAGE = (
    "<b>Usage:</b>\n"
    "/shell <command>\n\n"
    "<b>Example:</b>\n"
    "/shell ls -l"
)
MSG_SHELL_EXECUTING = "Executing Command... ⚙️\n<pre>{command}</pre>"
MSG_SHELL_OUTPUT = """**Shell Command Output:**
<pre>{output}</pre>"""
MSG_SHELL_OUTPUT_STDOUT = "<b>[stdout]:</b>\n<pre>{output}</pre>"
MSG_SHELL_OUTPUT_STDERR = "<b>[stderr]:</b>\n<pre>{error}</pre>"
MSG_SHELL_NO_OUTPUT = "✅ <b>Command Executed:</b> No output."
MSG_ADMIN_SHELL_STDOUT_PLAIN = "[stdout]:\n{output}\n"
MSG_ADMIN_SHELL_STDERR_PLAIN = "[stderr]:\n{error}\n"
MSG_SHELL_OUTPUT_FILENAME = "shell_output.txt"

# ------ Admin View & Control ------
MSG_ADMIN_RESTART_BROADCAST = "🔄 Restart Broadcast"
MSG_ADMIN_CANCEL_BROADCAST = "🛑 Cancel Broadcast"
MSG_ADMIN_CANCEL_BROADCAST_BUTTON_TEXT = "ID: {broadcast_id} | Progress: {progress} | Time: {elapsed}"
MSG_ADMIN_BOT_WORKLOAD_HEADER = "🤖 **Bot Workload Distribution:**\n\n"
MSG_ADMIN_BOT_WORKLOAD_ITEM = "   {bot_name}: {load}\n"
MSG_ADMIN_BROADCAST_PROGRESS_ITEM = "ID: {broadcast_id} | Progress: {progress} | Time: {elapsed}"
MSG_ADMIN_RESTART_DONE = "✅ **Restart Successful!**"

# =====================================================================================
# ====== BUTTON TEXTS (User-facing) ======
# =====================================================================================
MSG_BUTTON_STREAM_NOW = "▶️ Stream"
MSG_BUTTON_DOWNLOAD = "📥 Download"
MSG_BUTTON_GET_HELP = "📖 Get Help"
MSG_BUTTON_QUICK_START = "🚀 Quick Start"
MSG_BUTTON_CANCEL_BROADCAST = "🛑 Cancel Broadcast"
MSG_BUTTON_VIEW_PROFILE = "👤 View User Profile"
MSG_BUTTON_ABOUT = "ℹ️ About Bot"
MSG_BUTTON_STATUS = "📡 Status"
MSG_BUTTON_JOIN_CHANNEL = "Join {channel_title}"
MSG_BUTTON_GITHUB = "🛠️ GitHub"
MSG_BUTTON_START_CHAT = "Start Bot Now"
MSG_BUTTON_JOIN_CHAT = "Join {chat_title}"
MSG_BUTTON_CLOSE = "🚫 Close"

# ------ Quick Start Guide ------
MSG_QUICK_START_GUIDE = (
    "🚀 **Quick Start Guide** 🚀\n\n"
    "Welcome to the Mixology Stream Bot! Here's how to get started:\n\n"
    "1. **Private Chat:** Send any file directly to me, and I'll reply with download and stream links.\n"
    "2. **Groups:** Reply to a file with the `/link` command. For multiple files, reply to the first file with `/link <number>` (e.g., `/link 5`).\n"
    "3. **Explore:** Use `/help` to see all available commands and features.\n\n"
    "Enjoy fast and easy file sharing! ⚡"
)

# =====================================================================================
# ====== COMMAND RESPONSES (User-facing) ======
# =====================================================================================

# ------ Welcome, Help, About ------
MSG_WELCOME = (
    "🌟 **Welcome, {user_name}!** 🌟\n\n"
    "I'm **Mixology Stream Bot** ⚡\n"
    "I generate direct download and streaming links for your files.\n\n"
    "**How to use:**\n"
    "1. Send any file to me for private links.\n"
    "2. In groups, reply to a file with `/link`.\n\n"
    "» Use `/help` for all commands and detailed information.\n\n"
    "🚀 Send a file to begin!"
)

MSG_HELP = (
    "📘 **Thunder Bot - Help Guide** 📖\n\n"
    "How to get direct download & streaming links:\n\n"
    "**🚀 Private Chat (with me):**\n"
    "> 1. Send me **any file** (document, video, audio, photo, etc.).\n"
    "> 2. I'll instantly reply with your links! ⚡\n\n"
    "**👥 Using in Groups:**\n"
    "> • Reply to any file with `/link`.\n"
    "> • **Batch Mode:** Reply to the *first* file with `/link <number>` (e.g., `/link 5` for 5 files, up to 100).\n"
    "> • Bot needs administrator rights in the group to function.\n"
    "> • Links are posted in the group & sent to you privately (if you have started a chat with me).\n"
    "> • *Optional:* If the bot is an admin with delete rights, it can be configured to auto-link new files.\n\n"
    "**📢 Using in Channels:**\n"
    "> • Add me as an administrator with necessary permissions.\n"
    "> • I can be configured to auto-detect new media files.\n"
    "> • Inline stream/download buttons can be added to files automatically.\n"
    "> • Files from banned channels (owner configuration) are rejected.\n"
    "> • Auto-posting links for new files is a configurable option.\n\n"
    "**⚙️ Available Commands:**\n"
    "> `/start` 👋 - Welcome message & quick start information.\n"
    "> `/help` 📖 - Shows this help message.\n"
    "> `/link <num>` 🔗 - (Groups) Generate links. For batch processing: `/link <number>` (1-100 files).\n"
    "> `/about` ℹ️ - Learn more about me and my features.\n"
    "> `/ping` 📡 - Check my responsiveness and online status.\n"
    "> `/dc` 🌍 - View DC information (for yourself, another user, or a file).\n\n"
    "**💡 Pro Tips:**\n"
    "> • You can forward files from other chats directly to me.\n"
    "> • If you encounter a rate limit message, please wait the specified time. ⏳\n"
    "> • For `/link` in groups to work reliably (and for private link delivery), ensure you've started a private chat with me first.\n"
    "> • Processing batch files might take a bit longer. Please be patient. 🐌\n\n"
    "❓ Questions? Please ask in our support group!"
)

MSG_ABOUT = (
    "🌟 **About Mixology Stream Bot** ℹ️\n\n"
    "I'm your go-to bot for **instant download & streaming!** ⚡\n\n"
    "**🚀 Key Features:**\n"
    "> **Instant Links:** Get your links within seconds.\n"
    "> **Online Streaming:** Watch videos or listen to audio directly (for supported formats).\n"
    "> **Universal File Support:** Handles documents, videos, audio, photos, and more.\n"
    "> **High-Speed Access:** Optimized for fast link generation and file access.\n"
    "> **Secure & Reliable:** Your files are handled with care during processing.\n"
    "> **User-Friendly Interface:** Designed for ease of use on any device.\n"
    "> **Efficient Processing:** Built for speed and reliability.\n"
    "> **Batch Mode:** Process multiple files at once in groups using `/link <number>`.\n"
    "> **Versatile Usage:** Works in private chats, groups, and channels (with admin setup).\n\n"
    "💖 If you find me useful, please consider sharing me with your friends!"
)

# ------ Ping ------
MSG_PING_START = "🛰️ **Pinging...** Please wait."
MSG_PING_RESPONSE = (
    "🚀 **PONG! Bot is Online!** ⚡\n"
    "> ⏱️ **Response Time:** {time_taken_ms:.2f} ms\n"
    "> 🤖 **Bot Status:** `Active & Ready`"
)

# ------ DC Info ------
MSG_DC_USER_INFO = (
    "📍 **Information**\n"
    "> 👤 **User:** [{user_name}](tg://user?id={user_id})\n"
    "> 🆔 **User ID:** `{user_id}`\n"
    "> 🌍 **DC ID:** `{dc_id}`"
)

MSG_DC_FILE_INFO = (
    "🗂️ **File Information**\n"
    ">`{file_name}`\n"
    "💾 **File Size:** `{file_size}`\n"
    "📁 **File Type:** `{file_type}`\n"
    "🌍 **DC ID:** `{dc_id}`"
)

MSG_DC_UNKNOWN = "Unknown"

# ------ File Link Generation ------
MSG_LINKS = (
    "📝 **File Name:** `{file_name}`\n"
    "📦 **File Size:** `{file_size}`\n\n"
    "📥 **Download Link:**\n`{download_link}`\n\n"
    "▶️ **Stream Link:**\n`{stream_link}`\n\n"
    "⌛ **Note:** Links valid for 24 hours only. Download or watch before they expire!"
)

# =====================================================================================
# ====== USER NOTIFICATIONS ======
# =====================================================================================

MSG_NEW_USER = (
    "✨ **New User Alert!** ✨\n"
    "> 👤 **Name:** [{first_name}](tg://user?id={user_id})\n"
    "> 🆔 **User ID:** `{user_id}`\n\n"
)

MSG_PRIVATE_CHAT_WELCOME = (
    "👋 **Welcome!** Send me any file to get started.\n"
    "> 📤 I'll generate instant download & streaming links for you.\n"
    "> ⚡ Fast and reliable service.\n"
    "> 🔒 Your files are handled securely."
)
MSG_DEFAULT_WELCOME = "📢 Don't forget our channel for the latest news & features!"
MSG_COMMUNITY_CHANNEL = "📢 **{channel_title}:** 🔒 Join this channel to use the bot."

# =====================================================================================
# ====== PROCESSING MESSAGES ======
# =====================================================================================

# ------ General File Processing ------
MSG_PROCESSING_REQUEST = "⏳ **Processing your request...**"
MSG_PROCESSING_FILE = "⏳ **Processing your file...**"
MSG_DEFAULT_FILENAME = "Untitled File"
MSG_NEW_FILE_REQUEST = (
    "> 👤 **Source:** [{source_info}](tg://user?id={id_})\n"
    "> 🆔 **ID:** `{id_}`\n\n"
    "🔗 **Download:** `{online_link}`\n\n"
    "🖥️ **Stream:** `{stream_link}`"
)

# ------ Batch Processing ------
MSG_PROCESSING_BATCH = "🔄 **Processing Batch {batch_number}/{total_batches}** ({file_count} files)"
MSG_PROCESSING_STATUS = "📊 **Processing Files:** {processed}/{total} complete, {failed} failed"
MSG_PROCESSING_WARNING = "⚠️ **Warning:** Too many files failed processing. Please try again with fewer files or contact support."
MSG_BATCH_LINKS_READY = "🔗 Here are your {count} download links:"
MSG_DM_BATCH_PREFIX = "📬 **Batch Links from {chat_title}**\n"
MSG_LINK_FROM_GROUP = "📬 **Links from {chat_title}**\n\n{links_message}"
MSG_PROCESSING_RESULT = "✅ **Process Complete:** {processed}/{total} files processed successfully, {failed} failed"
MSG_PROCESSING_ERROR = "❌ **Error Processing Files:** {error}\n\n{processed}/{total} files were processed (ID: {error_id})"
MSG_RETRYING_FILES = "🔄 **Retrying {count} Failed Files...**"

# =====================================================================================
# ====== BROADCAST MESSAGES ======
# =====================================================================================
MSG_BROADCAST_START = "📣 **Starting Broadcast...**\n\n> ⏳ Please wait for completion."
MSG_BROADCAST_PROGRESS = (
    "📊 **Broadcast Progress**\n\n"
    "> 👥 **Total Users:** `{total_users}`\n"
    "> ✅ **Processed:** `{processed}/{total_users}`\n"
    "> ⏱️ **Elapsed:** `{elapsed_time}`\n\n"
    "> ✓ **Sent:** `{successes}`\n"
    "> ✗ **Failed:** `{failures}`"
)

# =====================================================================================
# ====== PERMISSION MESSAGES ======
# =====================================================================================
MSG_ERROR_UNAUTHORIZED = "You are not authorized to view this information."
MSG_ERROR_BROADCAST_RESTART = "Please use the /broadcast command to start a new broadcast."
MSG_ERROR_BROADCAST_INSTRUCTION = "To start a new broadcast, use the /broadcast command and reply to the message you want to broadcast."
MSG_ERROR_CALLBACK_UNSUPPORTED = "This button is not active or no longer supported."
MSG_ERROR_GENERIC_CALLBACK = "An error occurred. Please try again later. (ID: {error_id})"
MSG_BROADCAST_COMPLETE = (
    "📢 **Broadcast Completed Successfully!** 📢\n\n"
    "⏱️ **Duration:** `{elapsed_time}`\n"
    "👥 **Total Users:** `{total_users}`\n"
    "✅ **Successful Deliveries:** `{successes}`\n"
    "❌ **Failed Deliveries:** `{failures}`\n\n"
    "🗑️ **Accounts Removed (Blocked/Deactivated):** `{deleted_accounts}`\n"
)
MSG_BROADCAST_CANCEL = "🛑 **Cancelling Broadcast:** `{broadcast_id}`\n\n> ⏳ Stopping operations..."
MSG_BROADCAST_FAILED = (
    "❌ **Broadcast Failed!** 😞\n\n"
    "> ❗ **Error Details:**\n```\n{error}\n``` (ID: {error_id})"
)
MSG_INVALID_BROADCAST_CMD = "Please reply to the message you want to broadcast."
MSG_NO_ACTIVE_BROADCASTS = "ℹ️ **No Active Broadcasts:** Nothing to cancel at the moment."
MSG_BROADCAST_NOT_FOUND = "⚠️ **Broadcast Not Found:** This broadcast is no longer active or has finished."
MSG_MULTIPLE_BROADCASTS = "🔄 **Multiple Broadcasts Active:** Select one to cancel:"
MSG_CANCELLING_BROADCAST = "🛑 **Cancelling Broadcast:** `{broadcast_id}`\n\n> ⏳ Stopping operations... Please wait."

# =====================================================================================
# ====== FORCE CHANNEL MESSAGES ======
# =====================================================================================

MSG_FORCE_CHANNEL_ERROR = "Sorry, there was an issue verifying access. Please try again later. (ID: {error_id})"
MSG_FORCE_CHANNEL_RPC_ERROR = "An unexpected error occurred while checking channel membership. Please try again. (ID: {error_id})"
MSG_FORCE_CHANNEL_GENERIC_ERROR = "An error occurred. Please try again. (ID: {error_id})"
MSG_FORCE_CHANNEL_NO_LINK = "To use this bot, you must join our main channel. Please contact an admin for assistance."
MSG_FORCE_CHANNEL_ACCESS_REQUIRED = (
    "🚫 **Access Required**\n\n"
    "Please join our channel to use this bot:\n{invite_link}\n\n"
    "After joining, try your command again."
)
MSG_FORCE_CHANNEL_SERVICE_INTERRUPTION = "⚠️ Temporary service interruption. Please try again later. (ID: {error_id})"
MSG_FORCE_CHANNEL_MEMBERSHIP_REQUIRED = "🔒 This command requires channel membership. Please contact support if you need assistance. (ID: {error_id})"

# =====================================================================================
# ====== FILE TYPE DESCRIPTIONS ======
# =====================================================================================
MSG_FILE_TYPE_DOCUMENT = "📄 Document"
MSG_FILE_TYPE_PHOTO = "🖼️ Photo"
MSG_FILE_TYPE_VIDEO = "🎬 Video"
MSG_FILE_TYPE_AUDIO = "🎵 Audio"
MSG_FILE_TYPE_VOICE = "🎤 Voice Message"
MSG_FILE_TYPE_STICKER = "🎨 Sticker"
MSG_FILE_TYPE_ANIMATION = "🎞️ Animation (GIF)"
MSG_FILE_TYPE_VIDEO_NOTE = "📹 Video Note"
MSG_FILE_TYPE_UNKNOWN = "❓ Unknown File Type"

# =====================================================================================
# ====== SYSTEM & STATUS MESSAGES (Bot Health, Logs, Stats) ======
# =====================================================================================

MSG_RESTARTING = "🔄 **Restarting Bot...**\n\n> ⏳ Please wait a moment."
MSG_LOG_FILE_CAPTION = "📄 **System Logs**\n\n> ℹ️ Latest log file"
MSG_LOG_FILE_EMPTY = "ℹ️ **Log File Empty:** No data found in the log file."
MSG_LOG_FILE_MISSING = "⚠️ **Log File Missing:** Could not find the log file."
MSG_SYSTEM_STATUS = (
    "✅ **System Status:** Operational\n\n"
    "> 🕒 **Uptime:** `{uptime}`\n"
    "> 🤖 **Active Bot Instances:** `{active_bots}`\n\n"
    "{workloads}\n"
    "> ♻️ **Bot Version:** `{version}`"
)
MSG_SYSTEM_STATS = (
    "📊 **System Statistics**\n\n"
    "> 🕒 **Uptime:** `{uptime}`\n\n"
    "💾 **Storage (Server):**\n"
    "> 📀 Total: `{total}`\n"
    "> 📝 Used: `{used}`\n"
    "> 📭 Free: `{free}`\n\n"
    "📶 **Network (Server):**\n"
    "> 🔺 Upload: `{upload}`\n"
    "> 🔻 Download: `{download}`\n\n"
)
MSG_PERFORMANCE_STATS = (
    "⚙️ **Performance (Server):**\n"
    "> 🖥️ CPU: `{cpu_percent}%`\n"
    "> 🧠 RAM: `{ram_percent}%`\n"
    "> 📦 Disk: `{disk_percent}%`"
)
MSG_DB_STATS = "📊 **Database Statistics**\n\n> 👥 **Total Users:** `{total_users}`"
MSG_BOT_WORKLOAD_ITEM = "🔹 Bot {num}: {load}"
MSG_BOT_WORKLOAD_TEXT = "   {bot_name}: {load}\n"
