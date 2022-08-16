import json


def update_black_list(chat_id: str, users: list):
    with open(f'root/botProject/mihanProject/black_list/restricted_chats/{chat_id}.json', 'w') as js:
        json.dump(users, js)


def update_pre_ban_list(banlist: list):
    with open(f'root/botProject/mihanProject/black_list/pre_ban_list.json', 'w') as js:
        json.dump(banlist, js)


def bolshe_ne_gandon(chat, bivshiy_gandon: int):
    gandoniy[chat].remove(bivshiy_gandon)
    update_json(chat, list(gandoniy[chat]))
