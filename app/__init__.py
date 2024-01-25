import logging
import time
from pyrogram import Client
from app.config import var

StartTime = time.time()
plugins = dict(
    root = "app/plugins"
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(format="[%(levelname)s] [%(filename)s] [%(funcName)s] [%(lineno)d] %(message)s")

bot = Client(
    session_name=':memory:',
    api_id=var.API_ID,
    api_hash=var.API_HASH,
    bot_token=var.BOT_TOKEN,
    plugins=plugins
)
