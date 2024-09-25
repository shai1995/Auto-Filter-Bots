import re
import os
from os import environ
from pyrogram import enums
from Script import script
import asyncio
import json
from collections import defaultdict
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1612652792 1255023013').split()]
USERNAME = environ.get('USERNAME', 'https://telegram.me/Mradbot_Admin')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002228536126'))
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002444360071').split()]
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_URI2 = environ.get('DATABASE_URI2', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Mass')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002359445972'))
QR_CODE = environ.get('QR_CODE', 'https://envs.sh/0-Y.jpg')

#this vars is for when heroku or koyeb acc get banned, then change this vars as your file to link bot name
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-1002468523460'))
URL = environ.get('URL', 'married-milissent-filmfree-333e214f.koyeb.app')

# verify system vars
IS_VERIFY = is_enabled('IS_VERIFY', True)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002325909402'))
TUTORIAL = environ.get("TUTORIAL", "https://youtu.be/5rsz9fWu3Ic?si=AZyGM700ABk-fUNB")
TUTORIAL2 = environ.get("TUTORIAL2", "")
TUTORIAL3 = environ.get("TUTORIAL3", "")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/45a270fc6a0a1c183c614.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "fc837447971bc7534016e082b63f59c8a3f926f8")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "shrinkforearn.in")
SHORTENER_API2 = environ.get("SHORTENER_API2", "")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "")
SHORTENER_API3 = environ.get("SHORTENER_API3", "")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "")
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "3600"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "21600"))

# languages search
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam"]

auth_channel = environ.get('AUTH_CHANNEL', '-1002169426172')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1002231312317'))

# bot settings
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '8080')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 600))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
PM_SEARCH = is_enabled('IS_PM_SEARCH', True)
