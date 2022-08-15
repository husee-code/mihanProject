import os
import json

massiv_pidorov: set = set()
gandoniy_chat = -651037154
zaebis_chat = -669655344

gandoniy: dict[str:set] = {}
with open(f'black_list/permanent.json') as js:
    black_list: set = set(json.load(js))

for chat in os.listdir('black_list/restricted_chats'):
    with open(f'black_list/restricted_chats/{chat}') as js:
        chat_name = chat.replace('.json', '')
        gandoniy[chat_name] = set(json.load(js))

with open(r"cons_and_vars\texts.json", encoding='utf-8') as js:
    texts = json.load(js)
