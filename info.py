import re
from os import environ,getenv
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '21911596'))
API_HASH = environ.get('API_HASH', '11c95e9516ee3f829f91f5e21692939e')
BOT_TOKEN = environ.get('BOT_TOKEN', "8040663206:AAHyX5cPAuaoEcYFLpvIpdk3UK8RFTYQ7Hs")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://graph.org/file/592d568b2a09e7fcf1188-d4c66150463a43f15e.jpg https://graph.org/file/2f8ee9efe81fd42092c1c-313f8e73b1b9e57b68.jpg https://graph.org/file/ffcfb1e9ef336fbcb4771-0c5a7560dc2c6f6b64.jpg https://graph.org/file/290bf9261d799ac5c4c97-cee65615a3c35617da.jpg https://graph.org/file/130fb8f60c2bf704e062a-a1d257ad63a70624ca.jpg https://graph.org/file/f871bd9f686ae1e1b4b04-58376f5518e51d599f.jpg https://graph.org/file/1d9b27c4d04131b93013b-e5a0edbab19697bef9.jpg')).split() #SAMPLE PIC
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/e20b5fdaf217252964202.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://envs.sh/Cu9.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/13702ae26fb05df52667c.jpg")
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://envs.sh/5H7.jpg'))
CODE = (environ.get('CODE', 'https://envs.sh/5H7.jpg'))


# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6594043398').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002387592793').split()] #Channel id for auto indexing ( make sure bot is admin )
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002189233525')) #Log channel id ( make sure bot is admin )
DEENDAYAL_MOVIE_UPDATE_CHANNEL = int(environ.get('DEENDAYAL_MOVIE_UPDATE_CHANNEL', '-1002401488764')) #Notification of those who verify will be sent to your channel. Enter the ID of the channel you want to send notification to here.
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', '-1002189233525')) # add premium logs channel id
auth_channel = environ.get('AUTH_CHANNEL', '-1001692297236') #Channel / Group Id for force sub ( make sure bot is admin )
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-1002474691060').split()]
support_chat_id = environ.get('SUPPORT_CHAT_ID', '') # support group id ( make sure bot is admin )
reqst_channel = environ.get('REQST_CHANNEL_ID', '') # request channel id ( make sure bot is admin ).


# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://maran116:cK5V1CJbJVVOXcdo@cluster0.1ybqm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "mangoDB")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Files')

# index movie Notification & update channel 
DEENDAYAL_MOVIE_UPDATE_NOTIFICATION = bool(environ.get('DEENDAYAL_MOVIE_UPDATE_NOTIFICATION', False))  # NOTIFICATION On ( True ) / Off ( False )
DEENDAYAL_IMAGE_FETCH = bool(environ.get('DEENDAYAL_IMAGE_FETCH', True))  #  On ( True ) / Off ( False )
CAPTION_LANGUAGES = ["Bhojpuri", "Hindi", "Bengali", "Tamil", "English", "Bangla", "Telugu", "Malayalam", "Kannada", "Marathi", "Punjabi", "Bengoli", "Gujrati", "Korean", "Gujarati", "Spanish", "French", "German", "Chinese", "Arabic", "Portuguese", "Russian", "Japanese", "Odia", "Assamese", "Urdu"]



# Verify
VERIFY = bool(environ.get('VERIFY', True)) # Verification On ( True ) / Off ( False )
DEENDAYAL_VERIFY_EXPIRE = int(environ.get('DEENDAYAL_VERIFY_EXPIRE', 24)) # Add time in hours
DEENDAYAL_VERIFIED_LOG = int(environ.get('DEENDAYAL_VERIFIED_LOG', '-1002189233525')) #Log channel id ( make sure bot is admin )
HOW_TO_VERIFY = environ.get('HOW_TO_VERIFY', 'https://t.me/+4gvPwxUwq2o3Njc9') # How to open tutorial link for verification

# Shortner 
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'instantlinks.co')
SHORTLINK_API = environ.get('SHORTLINK_API', '645ea7db843cb1a5977267341cf8adb1873675f5')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/+4gvPwxUwq2o3Njc9') # Tutorial video link for opening shortlink website 
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', False))

#Channel & Group link 
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/Movies_request_group_tamil')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/TamilFlix_Mv')
OWNER_LNK = environ.get('OWNER_LNK', 'https://t.me/TamilFlix_Admine_bot')
DEENDAYAL_MOVIE_UPDATE_CHANNEL_LNK = environ.get('DEENDAYAL_MOVIE_UPDATE_CHANNEL_LNK', 'https://t.me/TamilFlix_Mv')

auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '').split()]
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", True)) # True if you want no results messages in Log Channel
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
MSG_ALRT = environ.get('MSG_ALRT', 'Hi Friends ❤️')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/TamilFlix_Admine_bot') #Support group link ( make sure bot is admin )
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
IMDBSEARCH_TEMPLATE = environ.get("IMDBSEARCH_TEMPLATE", f"{script.IMDBSEARCH_TEMPLATE}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), True)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)
PM_SEARCH = bool(environ.get('PM_SEARCH', True)) # PM Search On ( True ) / Off ( False )

LANGUAGES = ["malayalam", "", "tamil", "", "english", "", "hindi", "", "telugu", "", "kannada", "", "gujarati", "", "marathi", "", "punjabi", ""]

SEASONS = ["season 1" , "season 2" , "season 3" , "season 4", "season 5" , "season 6" , "season 7" , "season 8" , "season 9" , "season 10"]

QUALITIES = ["360P", "", "480P", "", "720P", "", "1080P", "", "1440P", "", "2160P", ""]

# Online Stream and Download
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', 'https://hushed-lenna-marankk-53d7a26b.koyeb.app/'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://hushed-lenna-marankk-53d7a26b.koyeb.app/".format(FQDN) if ON_HEROKU or NO_PORT else \
    "https://hushed-lenna-marankk-53d7a26b.koyeb.app/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'LazyBot'))
MULTI_CLIENT = False
name = str(environ.get('name', 'LazyPrincess'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))

else:
    ON_HEROKU = False
HAS_SSL=bool(getenv('HAS_SSL',True))
if HAS_SSL:
    URL = "https://hushed-lenna-marankk-53d7a26b.koyeb.app/".format(FQDN)
else:
    URL = "https://hushed-lenna-marankk-53d7a26b.koyeb.app/".format(FQDN)

#ADD_REACTION
REACTIONS = ["❤️‍🔥", "❤️", "🔥", "🙋","😢", "🎉", "🤩", "🙏", "👌", "🕊"]


LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
