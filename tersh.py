# markup_menu = client.build_reply_markup([[
#             Button.text('Настройка чатов', resize=True),
#             Button.text('Настройка поиска, resize=True)],
#             [Button.text('Вкл/Выкл', resize=True),
#             Button.text('Смена пользователя', resize=True)
#                         ]])



# @client.on(events.NewMessage(chats=('Мама')))
# async def normal_handler_client(event):
#     # print(event.message)
#     print(event.message.to_dict()['message'])
#     if event.message.to_dict()['message'] == 'exit':
#         exit(0)
#
# @bot.on(events.NewMessage(pattern=r'Hello'))
# async def callback(event):
#     # send = await client.send_message('me', 'Hi lol')
#
#     # await bot.send_message('yablochko_bot','Hello!', buttons=Button.inline('Click me', callback))
#     # await client.build_reply_markup(Button.text('hi', resize=True))
#     # await event.reply('hi', buttons=markup)
#     pass
#


def main():

    def lop(*arg):
        def loop(arg):
            for i in arg:
                yield i
        return print(next(loop(arg)))
    lop = lop('hi', 'helo')


if __name__ == '__main__':
    main()


def retexing(text):
    if text == 'Назад':
        pass
    elif text == '':
        pass
async def loop(*arg):
    for i in arg:
        yield str(i)

async def lop(*arg):
    async def loop(arg):
        for i in arg:
            yield i
    return print(next(loop(arg)))
lop = lop('hi', 'helo')

#
# def find_chats(patern):
#     list_ch = {}
#     for dialog in client.iter_dialogs():
#
#         result = re.search(patern, dialog.title.lower())
#         # print(result)
#         if result:
#             list_ch[dialog.title] = dialog.id
#
#     return list_ch
#
#
#
#
# find = find_chats('мама').get('Мама')
#
