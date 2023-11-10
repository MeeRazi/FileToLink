import os
# Bot information
API_ID = os.getenv('API_ID', "")
API_HASH = os.getenv('API_HASH', "")
BOT_TOKEN = os.getenv('BOT_TOKEN', "")

# stream vars
PORT = int(os.getenv('PORT', '5050'))
BIN_CHANNEL = os.getenv("BIN_CHANNEL", "")
URL = os.getenv("URL", "")