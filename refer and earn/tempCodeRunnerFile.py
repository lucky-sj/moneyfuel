import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
client = MongoClient()
client = MongoClient("mongodb://localhost:27017/")
myDatabase = client["Order_list"]
mycollection = myDatabase["royale"]


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)
token = os.getenv("TELEGRAM_API")
print(token)