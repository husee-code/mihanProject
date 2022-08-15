import os
import json
import configparser
from telethon import TelegramClient, events
from telethon.tl.types import MessageActionChatJoinedByLink, MessageActionChatAddUser, MessageActionChatDeleteUser, \
    UpdateShortMessage, InputPeerChat
from cons_and_vars.vars import *
from functions import update_pre_ban_list


def register_user_handlers(client):
    @client.on(events.NewMessage())
    async def read_and_answer_msg(event):
        user_id = event.original_update.user_id
        if type(event.original_update) == UpdateShortMessage:
            if user_id not in massiv_pidorov:
                for chat in gandoniy:
                    iter_participants = client.iter_participants(int(chat))
                    gandoniy[chat] = set([participant.id async for participant in iter_participants])
                    if user_id in gandoniy[chat]:
                        await client.send_message(user_id, texts["message_if_not_unsubscribed"])
                        break
                else:
                    await client.send_message(user_id, texts["message_if_unsubscribed"])
                    massiv_pidorov.add(user_id)
                    update_pre_ban_list(list(massiv_pidorov))
            else:
                await client.send_message(user_id, texts["message_if_banned"])
