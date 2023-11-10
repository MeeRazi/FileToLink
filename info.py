from os import environ

# Bot information
API_ID = environ.get('API_ID', "")
API_HASH = environ.get('API_HASH', "")
BOT_TOKEN = environ.get('BOT_TOKEN', "")

# stream vars
PORT = int(environ.get('PORT', '5050'))
BIN_CHANNEL = environ.get("BIN_CHANNEL", "")
URL = environ.get("URL", "")