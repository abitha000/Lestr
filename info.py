import os

class temp(object):
    BOT = None
def safe_int(val, default):
    try:
        return int(val)
    except (ValueError, TypeError):
        print(f"[WARN] Cannot convert {val!r} to int; using default {default}")
        return default
API_ID = safe_int(os.getenv('API_ID'), 24401235)
API_HASH = os.getenv('API_HASH', "149f7e13d7d861b27cffc3ab1fd52b22")
PORT = safe_int(os.getenv('PORT'), 8080)
BIN_CHANNEL = safe_int(os.getenv('BIN_CHANNEL'), -1002860251103)
BOT_TOKEN = os.getenv('BOT_TOKEN', "8167215119:AAH9giJCHz2TGbykSnLcoy5IK1rTNrr6lkc")
STREAM_URL = os.getenv("STREAM_URL", "https://causal-vania-kalaisel-339f7657.koyeb.app/")
