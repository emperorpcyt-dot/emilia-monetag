#(©)CodeXBotz
#Recoded By @Its_Tartaglia_Childe



import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "13296527"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "6ff44fffc149a6dc599a5d2eaeb8873c")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001929827203"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1891736799"))

#Port
PORT = int(os.environ.get("PORT", "8080"))  # Koyeb sets PORT automatically

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://INDABID:INDABID@cluster0.7x0cv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Emilia")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1001940086057"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1001850766501"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "⚡Hɪ ᴅᴜᴅᴇ.. {first}\n\nI ᴀᴍ ᴀ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ​\n​​Yᴏᴜ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ ᴘᴏᴡᴇʀᴇᴅ ʙʏ -​ @Anime_pirates")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "7154974039").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}!⚡\n\n🫧ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ʙᴏᴛʜ ᴏꜰ ᴏᴜʀ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟꜱ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ...!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

#----------------- AD VERIFICATION (Monetag rewarded ads) -----------------#
# Public HTTPS url of this bot's web server (e.g. https://your-app.koyeb.app)
# Leave empty to turn the ad verification OFF.
# On Koyeb this is filled automatically from KOYEB_PUBLIC_DOMAIN, so you can leave it empty there.
WEBAPP_URL = os.environ.get("WEBAPP_URL", "").strip().rstrip("/")
if not WEBAPP_URL and os.environ.get("KOYEB_PUBLIC_DOMAIN"):
    WEBAPP_URL = "https://" + os.environ["KOYEB_PUBLIC_DOMAIN"].strip().rstrip("/")
if WEBAPP_URL and not WEBAPP_URL.startswith("http"):
    WEBAPP_URL = "https://" + WEBAPP_URL

# Your Monetag "Telegram Mini App" zone id (only the number, e.g. 1234567)
MONETAG_ZONE = os.environ.get("MONETAG_ZONE", "")

# How long one ad verification stays valid, in seconds (default 6 hours)
VERIFY_EXPIRE = int(os.environ.get("VERIFY_EXPIRE", "21600"))

# Minimum seconds between opening the ad and finishing it (anti-cheat)
MIN_AD_SECONDS = int(os.environ.get("MIN_AD_SECONDS", "8"))

# Turned on only when both values are set
AD_VERIFY = bool(WEBAPP_URL and MONETAG_ZONE)

VERIFY_MSG = os.environ.get("VERIFY_MESSAGE", "ʜᴇʏ {first} 👋\n\n🔐 <b>Yᴏᴜʀ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ʜᴀꜱ ᴇxᴘɪʀᴇᴅ</b>\n\n1️⃣ Tᴀᴘ <b>✅ Vᴇʀɪꜰʏ Nᴏᴡ</b> ʙᴇʟᴏᴡ\n2️⃣ Wᴀᴛᴄʜ ᴛʜᴇ ꜱʜᴏʀᴛ ᴀᴅ ᴛɪʟʟ ɪᴛ ᴇɴᴅꜱ\n3️⃣ Yᴏᴜʀ ꜰɪʟᴇꜱ ᴡɪʟʟ ʙᴇ ꜱᴇɴᴛ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ\n\n⏳ Vᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ꜱᴛᴀʏꜱ ᴀᴄᴛɪᴠᴇ ꜰᴏʀ <b>{hours}</b>.\n\n<i>Nᴏᴛᴇ: ɪꜰ ᴛʜᴇ ᴀᴅ ᴅᴏᴇꜱɴ'ᴛ ʟᴏᴀᴅ, ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ɴᴇᴛᴡᴏʀᴋ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ.</i>")
#--------------------------------------------------------------------------#

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "​🚫Pʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ᴍᴇꜱꜱᴀɢᴇ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ ɪ ᴀᴍ ᴏɴʟʏ ᴡᴏʀᴋ ꜰᴏʀ​ - @Anime_pirates"

ADMINS.append(OWNER_ID)
ADMINS.append(5090651635)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
