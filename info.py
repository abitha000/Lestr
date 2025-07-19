import os

class temp(object):
    BOT = None

API_ID = int(os.getenv('API_ID', 24401235))
API_HASH = os.getenv('API_HASH', "149f7e13d7d861b27cffc3ab1fd52b22")
BOT_TOKEN = os.getenv('BOT_TOKEN', "8167215119:AAH9giJCHz2TGbykSnLcoy5IK1rTNrr6lkc")

PORT = int(os.getenv('PORT', 8080))
BIN_CHANNEL = int(os.getenv("BIN_CHANNEL", -1002860251103))
STREAM_URL = os.getenv("STREAM_URL", "https://causal-vania-kalaisel-339f7657.koyeb.app/")
