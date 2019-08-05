from telethon import TelegramClient, sync, events
from telethon.tl.custom import Button
# import telethon.tl.custom
from func import start, asfind_chats

# Tresh
phone = '+380936593570'
api_hash = '8e643734dc596de5d2a082a1698c9489'
api_id = 702193
bot_token = '732023198:AAEoQQcFy_r5wRQzIF7qWfv4ieBfeGNChQ4'
title_list = ['работа', 'работу', 'work', 'works']
list_exept = ['Меню', 'Смена пользователя', 'Настройка чатов', 'Назад', 'Пусто', '']
BACK = ''
NEKST = ''
PHONE_AWAIT = False
add_await = False
del_await = False
started = False
start_await = False
word_await = False
word_in_await = False
list_add_chat = []
list_id_chat = []
list_patterns = []
list_del_chat = ['Пусто', 'Пусто', 'Пусто']
copy_del_chat = []
tuple_id_chat = tuple(set(list_id_chat))
pattern = ''
pattern_in = ''


# singin bot and client
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
client = TelegramClient('sesion', api_id, api_hash)







# buttons  view
# markup_stop = client.build_reply_markup([
#         [
#             Button.text('Настройка чатов', resize=True),
#             Button.text('Настройка поиска', resize=True)
#         ],
#         [
#             Button.text('Стоп')
#         ],
#         [
#             Button.text('Выход')
#         ]
#
#     ])

markup_phone = client.build_reply_markup(
            [
                [
                    Button.text('Назад')
                ]
            ])

markup1 = client.build_reply_markup(
    [
        [
            Button.text('Меню', resize=True)
        ]
    ])
markup_menu = client.build_reply_markup([
            [
                Button.text('Настройка чатов', resize=True),
                Button.text('Настройка поиска', resize=True)
            ],
            [
                Button.text(('Старт' if not started else 'stop'))
            ],
            [
                Button.text('Выход')
            ]

        ])

markup_setup_chat = client.build_reply_markup([
            [
                Button.text('Добавить чаты', resize=True),

                Button.text("Удалить чаты", resize=True),
            ],
            [
                Button.text('Ключевое слово', resize=True)
            ],
            [

                Button.text('Меню', resize=True)
            ]
        ])


markup_pattern_chat = client.build_reply_markup([
            [
                Button.text(pattern, resize=True)
            ],
            [
                Button.text('Назад', resize=True)
            ]
        ])

def put_listaddchat(dictt,listt):
    '''
    Функция берет из словаря имя и записывает в список
    :param dictt:  словарь в котором назавания и айди всех чатов
    :param listt:   список в который будут записаны только имена чатов
    :return: вункция ничего не возвращат
    '''
    try:
        listt.clear()
        print(''.format())
        for key, val in dictt.items():
            listt.append(key)
        listt.sort()
        print('Ok.append')
    except Exception as e:
        print(e)
# def asput_listaddchat(dictt,listt):
#     try:
#         for key, val in dictt.items():
#             listt.append(int(key))
#         print('Ok.append')
#     except Exception as e:
#         print(e)

def nekst(listT):
    '''
    Эта функция итерируется по списку через next()
    :param listT: список по которому итерируемся
    '''
    while True:
        for i in listT:
            revizor(listT)
            yield i

def revizor(rev):
    '''
    Если в списке меньше 3 значений то добавит Пусто
    :param rev: список в котором проверяем
    '''
    if rev == list_add_chat and len(rev) < 3:
        list_add_chat.append('Пусто')
    elif rev == list_del_chat and len(rev) < 3:
        list_del_chat.append('Пусто')


dict_add_chat = {}

next_del = nekst(list_del_chat)
next_add = nekst(list_add_chat)




# ------ all handlers -------



@bot.on(events.NewMessage())
async def setup_bot(event):
    try:
        global pattern, pattern_in
        if event.message.to_dict()['message'] == 'Выход':
            # await event.reply('By')
            await event.respond('Good by', buttons=markup1)
            exit(0)
        elif event.message.to_dict()['message'] in list_add_chat and add_await:
            if not event.message.to_dict()['message'] == 'Пусто':
                if 'Пусто' not in list_add_chat:
                    print('not in list_add_chat')
                    list_add_chat.remove(event.message.to_dict()['message'])
                    if len(list_add_chat) < 3:
                        list_add_chat.append('Пусто')
                    list_del_chat.append(event.message.to_dict()['message'])
                    list_id_chat.append(dict_add_chat.get(event.message.to_dict()['message']))
                    print(list_id_chat)
                    try:
                        list_del_chat.remove('Пусто')
                    except Exception as e:
                        print(e)
                    print(tuple(list_id_chat))
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
                    await event.reply('Добавлено', buttons=markup_add_chat)
                    print('not in list_add_chat', list_add_chat)
                    print(add_await)
                elif 'Пусто' in list_add_chat:
                    list_add_chat.remove(event.message.to_dict()['message'])
                    if len(list_add_chat) < 3:
                        list_add_chat.append('Пусто')
                    list_del_chat.append(event.message.to_dict()['message'])
                    copy_del_chat.append(event.message.to_dict()['message'])
                    list_id_chat.append(dict_add_chat.get(event.message.to_dict()['message']))
                    print(tuple(list_id_chat))
                    try:
                        list_del_chat.remove('Пусто')
                    except Exception as e:
                        print(e)
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
                    await event.reply('Добавлено', buttons=markup_add_chat)
                    print(tuple(list_id_chat))
        elif event.message.to_dict()['message'] in list_del_chat and del_await:
            if not event.message.to_dict()['message'] == 'Пусто':
                list_del_chat.remove(event.message.to_dict()['message'])
                list_add_chat.append(event.message.to_dict()['message'])
                list_id_chat.remove(dict_add_chat.get(event.message.to_dict()['message']))
                await asfind_chats(pattern, dict_add_chat)
                put_listaddchat(dict_add_chat, list_add_chat)
                print(list_id_chat)
                try:
                    list_add_chat.remove('Пусто')
                except Exception as e:
                    print(e)
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
                await event.reply('Удалено', buttons=markup_del_chat)
        #chat
        elif (event.message.to_dict()['message'] == pattern
              and word_await
              and not event.message.to_dict()['message'] in list_exept
        ):
            await asfind_chats(pattern, dict_add_chat)
            put_listaddchat(dict_add_chat, list_add_chat)
            pattern = ''
            markup_pattern_chat = client.build_reply_markup([
                [
                    Button.text(pattern, resize=True)
                ],
                [
                    Button.text('Назад', resize=True)
                ]
            ])
            await event.reply('Слово удалено!', buttons=markup_pattern_chat)
        #chat
        elif (event.message.to_dict()['message'] != pattern
              and word_await
              and not event.message.to_dict()['message'] in list_exept
        ):
            pattern = event.message.to_dict()['message']
            await asfind_chats(pattern, dict_add_chat)
            list_add_chat.clear()
            put_listaddchat(dict_add_chat, list_add_chat)
            print(pattern)
            print(dict_add_chat)
            print(list_add_chat)
            markup_pattern_chat = client.build_reply_markup([
            [
                Button.text(pattern, resize=True)
            ],
            [
                Button.text('Назад', resize=True)
            ]
            ])
            await event.reply('Слово добавленно!', buttons=markup_pattern_chat)
            if list_add_chat:
                await event.reply('Чаты найдены!', buttons=markup_pattern_chat)
            else:
                await event.reply('Чаты  не найдены!', buttons=markup_pattern_chat)
            #
        elif (event.message.to_dict()['message'] == pattern
              and word_await
              and not event.message.to_dict()['message'] in list_exept
              ):
            await asfind_chats(pattern, dict_add_chat)
            put_listaddchat(dict_add_chat, list_add_chat)
            pattern = ''
            markup_pattern_chat = client.build_reply_markup([
                [
                    Button.text(pattern, resize=True)
                ],
                [
                    Button.text('Назад', resize=True)
                ]
            ])
            await event.reply('Слово удалено!', buttons=markup_pattern_chat)
        #in_chat != pattern_in
        elif (event.message.to_dict()['message'] != pattern_in
              and word_in_await
              and not event.message.to_dict()['message'] in list_exept
        ):
            pattern_in = event.message.to_dict()['message']
            markup_pattern_in_chat = client.build_reply_markup([
                [
                    Button.text(pattern_in, resize=True)
                ],
                [
                    Button.text('Назад', resize=True)
                ]
            ])
            await event.reply('Слово добавленно!', buttons=markup_pattern_in_chat)
        # in_chat == pattern_in
        elif (event.message.to_dict()['message'] == pattern_in
              and word_in_await
              and not event.message.to_dict()['message'] in list_exept
        ):
            pattern_in = ''
            markup_pattern_in_chat = client.build_reply_markup([
                [
                    Button.text(pattern_in, resize=True)
                ],
                [
                    Button.text('Назад', resize=True)
                ]
            ])
            await event.reply('Слово удалено!', buttons=markup_pattern_in_chat)
    except Exception as e:
        print(e)
        await event.respond(str(e))



# Меню
@bot.on(events.NewMessage(pattern=r'Меню'))
async def handler_menu(event):
    try:
        global PHONE_AWAIT, add_await, del_await, word_await, word_in_await
        del_await = False
        add_await = False
        PHONE_AWAIT = False
        word_await = False
        word_in_await = False
        text_menu = 'Меню:'
        await event.respond(text_menu, buttons=markup_menu)
    except Exception as e:
        print(e)
        await event.respond(str(e))


# Настройка чатов
@bot.on(events.NewMessage(pattern=r'Настройка чатов'))
async def handler_setup_chat(event):
    try:
        global BACK
        BACK = event.message.to_dict()['message']
        global add_await, del_await
        add_await = False
        del_await = False
        await event.respond('Настройка чатов:', buttons=markup_setup_chat)
        print(event.message.to_dict())
    except Exception as e:
        print(e)
        await event.respond(str(e))

# Назад
@bot.on(events.NewMessage(pattern=r'Назад'))
async def handler_add_chat(event):
    try:
        global add_await, del_await, word_await, word_in_await
        add_await = False
        del_await = False
        word_await = False
        if BACK == 'Настройка чатов':
            try:
                await event.respond('Настройка чатов:', buttons=markup_setup_chat)
            except Exception as e:
                print(e)
                await event.respond(str(e))
        elif word_in_await:
            try:
                await event.respond('Меню:', buttons=markup_menu)
                word_in_await = False
            except Exception as e:
                print(e)
                await event.respond(str(e))
    except Exception as e:
        print(e)
        await event.respond(str(e))

# Еще
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

# Добавить чаты
@bot.on(events.NewMessage(pattern=r'Добавить чаты'))
async def handler_add_chat(event):
    try:
        if list_add_chat:
            global NEKST, add_await
            add_await = True
            NEKST = event.message.to_dict()['message']
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
        else:
            await event.respond('Добавьте ключевое слово, что бы добавть чат!', buttons=markup_setup_chat)
    except Exception as e:
        print(e)
        await event.respond(str(e))

# Удалить чаты
@bot.on(events.NewMessage(pattern=r'Удалить чаты'))
async def handler_add_chat(event):
    try:
        global NEKST, del_await
        del_await = True
        NEKST = event.message.to_dict()['message']
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

# Настройка поиска
@bot.on(events.NewMessage(pattern=r'Настройка поиска'))
async def handler_pattern_inchat(event):
    try:
        global word_in_await
        word_in_await = True
        markup_pattern_in_chat = client.build_reply_markup([
            [
                Button.text(pattern_in, resize=True)
            ],
            [
                Button.text('Назад', resize=True)
            ]
        ])
        await event.respond('Напишите слово для поиска в  отобранных чатах!', buttons=markup_pattern_in_chat)
    except Exception as e:
        print(e)
        await event.respond(str(e))

# Старт
@bot.on(events.NewMessage(pattern='Старт'))
async def handler_starts(event):
    try:
        global start_await, started
        start_await = True
        started = True
        put_listaddchat(dict_add_chat, list_add_chat)
        await event.reply('Старт бота!', buttons=markup_menu)
        await start(start_await)
    except Exception as e:
        print(e)
        await event.respond(str(e))

# Стоп
# @bot.on(events.NewMessage(pattern='Стоп'))
# async def handler_end(event):
#     try:
#         global start_await
#         start_await = False
#         await event.reply('Работа бота остановлена!', buttons=markup_menu)
#     except Exception as e:
#         print(e)
#         await event.respond(str(e))

#Ключевое слово
@bot.on(events.NewMessage(pattern=r'Ключевое слово'))
async def handler_pattern_chat(event):
    try:
        global word_await
        word_await = True
        markup_pattern_chat = client.build_reply_markup([
            [
                Button.text(pattern, resize=True)
            ],
            [
                Button.text('Назад', resize=True)
            ]
        ])
        await event.respond('Напишите слово по которому будет отбор среди чатов', buttons=markup_pattern_chat)
    except Exception as e:
        print(e)
        await event.respond(str(e))


client.start(phone=phone)
client.run_until_disconnected()


