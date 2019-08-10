from telethon import TelegramClient, sync, events
import re
import setup
import setup # Remove one
# from setup import list_del_chat, list_add_chat # remove unused comments

# Add 2 empty lines after import (PEP8)

# Take this variables from environment (see os.environ)
phone = '+38093 000 00 00'
api_hash = ''
api_id = 00000
bot_token = ''

client = TelegramClient('qwe', api_id, api_hash)
client.start(phone=phone)

async def asfind_chats(patern, dictt):
#     Rename dictt -> dict_ or give propper name (PEP8)
    dictt.clear()
    async for dialog in client.iter_dialogs():
        result = re.findall(patern.lower(), dialog.title.lower())
#         Use logging instead of print for logging in stdout.
        print(result)
        if result:
            dictt[dialog.title] = dialog.id

async def start(start_await):
#     Put import in the beginning. (PEP8)
    from setup import list_id_chat, start_await
    # tuple_chat = tuple(list_add_chat) # the same
    print(start_await) # the same
    # print(tuple_chat) # the same
    
#     You really need this function here? Why not in this module but inside start function?
    @client.on(events.NewMessage(chats=(x for x in list_id_chat)))
    async def handler_start(event):
        serch_text = re.match(setup.pattern_in.lower(), event.message.to_dict()['message'].lower())
        if event.message.to_dict()['message'] and serch_text and start_await:
            print(event.message.to_dict()['message']) # the same
            await client.send_message('me', event.message.to_dict()['message'])



