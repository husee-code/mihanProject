import os
import json
import configparser
from telethon import TelegramClient, events
from telethon.tl.types import MessageActionChatJoinedByLink, MessageActionChatAddUser, MessageActionChatDeleteUser, \
    UpdateShortMessage, InputPeerChat
from handlers.chat_handlers import *
from handlers.user_handlers import *


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read(r"settings.ini")
    api_id, api_hash = int(config["userbot"]["api_id"]), config["userbot"]["api_hash"]
    client = TelegramClient('user_bot_session', api_id, api_hash)
    register_chat_handlers(client)
    register_user_handlers(client)
    client.start()
    client.run_until_disconnected()
