import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29331999"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "4531af44db005a08606af9ebc1a042b2")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://7anzarul900:anzarul900@anzarul900.jj2cv.mongodb.net/?retryWrites=true&w=majority&appName=anzarul900")
