import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
URL_TEA = os.getenv("URL_TEA")
URL_COFFEE = os.getenv("URL_COFFEE")

#print(BOT_TOKEN)