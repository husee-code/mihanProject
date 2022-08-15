import os
import json
import configparser
from telethon import TelegramClient, events
from telethon.tl.types import MessageActionChatJoinedByLink, MessageActionChatAddUser, MessageActionChatDeleteUser, \
    UpdateShortMessage, InputPeerChat
from cons_and_vars.vars import *
from functions import *


def register_chat_handlers(client):
    @client.on(events.ChatAction(chats=[gandoniy_chat]))
    async def new_gandoniy(event):
        user_id = event.user_ids[0]
        chat_id = '-' + str(event.action_message.peer_id.chat_id)
        print(event.action_message.action)
        if type(event.action_message.action) in (MessageActionChatJoinedByLink, MessageActionChatAddUser):
            gandoniy[chat_id].add(user_id)
            update_black_list(chat_id, list(gandoniy[chat_id]))
            await client.kick_participant(zaebis_chat, user_id)
            await client.send_message(user_id, texts["message_to_kicked"])

    @client.on(events.ChatAction(chats=[zaebis_chat]))
    async def filter_gandoniy(event):
        user_id = event.user_ids[0]
        if user_id in black_list:
            await client.kick_participant(zaebis_chat, user_id)
            await client.send_message(user_id, texts["message_to_banned"])
        for chat, chat_members in gandoniy.items():
            if user_id in chat_members:
                if user_id in massiv_pidorov:
                    await client.kick_participant(zaebis_chat, user_id)
                    await client.send_message(user_id, texts['message_if_banned'])
                else:
                    await client.kick_participant(zaebis_chat, user_id)
                    await client.send_message(user_id, texts['message_to_kicked'].format(chat))



