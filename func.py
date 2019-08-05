from telethon import TelegramClient, sync, events
import re
import setup
import setup
# from setup import list_del_chat, list_add_chat
phone = '+380936593570'
api_hash = '8e643734dc596de5d2a082a1698c9489'
api_id = 702193
bot_token = '732023198:AAEoQQcFy_r5wRQzIF7qWfv4ieBfeGNChQ4'

client = TelegramClient('qwe', api_id, api_hash)
client.start(phone=phone)

async def asfind_chats(patern, dictt):
    dictt.clear()
    async for dialog in client.iter_dialogs():
        result = re.findall(patern.lower(), dialog.title.lower())
        print(result)
        if result:
            dictt[dialog.title] = dialog.id

async def start(start_await):
    from setup import list_id_chat, start_await
    # tuple_chat = tuple(list_add_chat)
    print(start_await)
    # print(tuple_chat)
    @client.on(events.NewMessage(chats=(x for x in list_id_chat)))
    async def handler_start(event):
        serch_text = re.match(setup.pattern_in.lower(), event.message.to_dict()['message'].lower())
        if event.message.to_dict()['message'] and serch_text and start_await:
            print(event.message.to_dict()['message'])
            await client.send_message('me', event.message.to_dict()['message'])



