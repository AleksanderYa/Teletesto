from telethon import TelegramClient, sync, events
import re
import pprint
from telethon import Button as buton
from telethon.tl.custom import Button
import telethon.tl.custom

# Tresh
phone = '+380936593570'
api_hash = '8e643734dc596de5d2a082a1698c9489'
api_id = 702193
bot_token = '732023198:AAEoQQcFy_r5wRQzIF7qWfv4ieBfeGNChQ4'
title_list = ['работа', 'работу', 'work', 'works']
list_exept = ['Меню', 'Смена пользователя', 'Настройка чатов', 'Назад', '', '']
BACK = ''
NEKST = ''
PHONE_AWAIT = ''

list_add_chat = [str(i) for i in range(10)]
list_del_chat = [str(i) for i in range(10)]
client_data = {}
client_data['phone'] = 'номер не записан'


# singin bot and client
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
client = TelegramClient('session_name', api_id, api_hash)

def nekst(listT):
    while True:
        for i in listT:
            yield i

next_add = nekst(list_add_chat)
next_del = nekst(list_del_chat)

markup_phone = client.build_reply_markup(
            [
                [
                    Button.text('Назад')
                ]
            ])

markup1 = client.build_reply_markup(
    [
        [
            Button.text('Логин', resize=True),
            Button.text('Меню', resize=True)
        ]
    ])
markup_menu = client.build_reply_markup([
            [
                Button.text('Настройка чатов', resize=True),
                Button.text('Настройка поиска', resize=True)
            ],
            [
                Button.text('Вкл/Выкл', resize=True),
                Button.text('Смена пользователя', resize=True)
            ],
            [
            Button.text('Выход')
            ]
        ])
markup_login = client.build_reply_markup([
            [
                Button.text('Номер телефона\n{}'.format(client_data.get('phone'))),
                Button.text('Айди клиента')
            ],
            [
                Button.text('Хеш бота'),
                Button.text('Вход'),
            ],
            [
                buton.text('Выход')
            ]
        ])
markup_setup_chat = client.build_reply_markup([
            [
                Button.text('Добавить чаты', resize=True),

                Button.text("Удалить чаты", resize=True),
            ],
            [
                Button.text('Меню', resize=True),
                Button.text('Выход', resize=True)
            ],
            [
                # Button.text('Выход')
            ]
        ])


markup_del_chat = client.build_reply_markup([
            [
                Button.text(next(next_del)),
                Button.text(next(next_del)),
                Button.text(next(next_del))
            ],
            [
                Button.text('Еще', resize=True),
                Button.text('Назад', resize=True)
            ]
        ])

markup_add_chat = client.build_reply_markup([
    [
        Button.text(next(next_add)),
        Button.text(next(next_add)),
        Button.text(next(next_add))
    ],
    [
        Button.text('Еще', resize=True),
        Button.text('Назад', resize=True)
    ]
])


# Выход 380999999999
@bot.on(events.NewMessage())
async def exit_bot(event):
    global PHONE_AWAIT
    try:
        if event.message.to_dict()['message'] == 'Выход':
            # await event.reply('By')
            await event.respond('Good by', buttons=markup1)
            exit(0)
        elif (re.search(r'\d+', event.message.to_dict()['message'])
              or re.search(r'\w\d', event.message.to_dict()['message'])
              or re.search(r'\w+', event.message.to_dict()['message'])) and (PHONE_AWAIT
                                                                             and not event.message.to_dict()['message']
                                        in list_exept):
            if re.search(r'\d{12}', event.message.to_dict()['message']):
                client_data['phone'] = event.message.to_dict()['message']
                print(client_data.get('phone'))
                PHONE_AWAIT = False
                # client_data_phone = client_data.get('phone')
                await event.respond('Телефон сохранен!\n{}'.format(client_data.get('phone')), buttons=markup_phone)
            elif re.search(r'\d\w\s+', event.message.to_dict()['message']):
                await event.reply('Введите номер телефона цифрами в формате : 380939009090')

            else:
                await event.reply('Введите коректно номер телефона в формате : 380939009090', buttons=markup_phone)
                # await event.respond('Номер телефона')



    except Exception as e:
        print(e)
        await event.respond(str(e))


# Hendler Menu
@bot.on(events.NewMessage(pattern=r'Меню'))
async def handler_menu(event):
    global PHONE_AWAIT
    PHONE_AWAIT = False
    try:
        text_menu = 'Меню:'
        await event.respond(text_menu, buttons=markup_menu)
    except Exception as e:
        print(e)
        await event.respond(str(e))



@bot.on(events.NewMessage(pattern=r'Смена пользователя'))
async def handler_login(event):
    global BACK
    BACK = event.message.to_dict()['message']
    global PHONE_AWAIT
    PHONE_AWAIT = False
    try:
        await event.respond('Вход клиента:', buttons=markup_login)
    except Exception as e:
        print(e)
        await event.respond(str(e))

@bot.on(events.NewMessage(pattern=r"Номер телефона"))
async def handler_login(event):
    try:
        await event.respond('Напишите номер телефона телеграм клиента:', buttons=markup_phone)
        global PHONE_AWAIT
        PHONE_AWAIT = True
    except Exception as e:
        print(e)
        await event.respond(str(e))

#
# @bot.on(events.NewMessage(pattern=r''))
# async def handler_phone_num(event):



@bot.on(events.NewMessage(pattern=r'Настройка чатов'))
async def handler_setup_chat(event):
    global BACK
    BACK = event.message.to_dict()['message']
    try:
        await event.respond('Настройка чатов:', buttons=markup_setup_chat)
    except Exception as e:
        print(e)
        await event.respond(str(e))

@bot.on(events.NewMessage(pattern=r'Назад'))
async def handler_add_chat(event):
    try:
        # global BACK
        if BACK == 'Настройка чатов':
            try:
                await event.respond('Настройка чатов:', buttons=markup_setup_chat)
            except Exception as e:
                print(e)
                await event.respond(str(e))
        elif BACK == 'Смена пользователя':
            global PHONE_AWAIT
            PHONE_AWAIT = False
            try:
                await event.respond('Вход клиента:', buttons=markup_login)
            except Exception as e:
                print(e)
                await event.respond(str(e))
    except Exception as e:
        print(e)
        await event.respond(str(e))





@bot.on(events.NewMessage(pattern=r'Еще'))
async def handler_add_chat(event):
    try:
        if NEKST == 'Добавить чаты':
            try:
                markup_add_chat = client.build_reply_markup([
                    [
                        Button.text(next(next_add)),
                        Button.text(next(next_add)),
                        Button.text(next(next_add))
                    ],
                    [
                        Button.text('Еще', resize=True),
                        Button.text('Назад', resize=True)
                    ]
                ])
                await event.respond('Добавить чаты:', buttons=markup_add_chat)
            except Exception as e:
                print(e)
                await event.respond(str(e))
        elif NEKST == 'Удалить чаты':
            try:
                markup_del_chat = client.build_reply_markup([
                    [
                        Button.text(next(next_del)),
                        Button.text(next(next_del)),
                        Button.text(next(next_del))
                    ],
                    [
                        Button.text('Еще', resize=True),
                        Button.text('Назад', resize=True)
                    ]
                ])
                await event.respond('Удалить чаты:', buttons=markup_del_chat)
            except Exception as e:
                print(e)
                await event.respond(str(e))
    except Exception as e:
        print(e)
        await event.respond(str(e))


@bot.on(events.NewMessage(pattern=r'Добавить чаты'))
async def handler_add_chat(event):
    global NEKST
    NEKST = event.message.to_dict()['message']
    try:
        markup_add_chat = client.build_reply_markup([
            [
                Button.text(next(next_add)),
                Button.text(next(next_add)),
                Button.text(next(next_add))
            ],
            [
                Button.text('Еще', resize=True),
                Button.text('Назад', resize=True)
            ]
        ])
        await event.respond('Добавить чаты:', buttons=markup_add_chat)
    except Exception as e:
        print(e)
        await event.respond(str(e))


@bot.on(events.NewMessage(pattern=r'Удалить чаты'))
async def handler_add_chat(event):
    global NEKST
    NEKST = event.message.to_dict()['message']
    try:
        markup_del_chat = client.build_reply_markup([
            [
                Button.text(next(next_del)),
                Button.text(next(next_del)),
                Button.text(next(next_del))
            ],
            [
                Button.text('Еще', resize=True),
                Button.text('Назад', resize=True)
            ]
        ])
        await event.respond('Удалить чаты:', buttons=markup_del_chat)
    except Exception as e:
        print(e)
        await event.respond(str(e))


# Start client
client.start(phone=phone)


client.run_until_disconnected()

