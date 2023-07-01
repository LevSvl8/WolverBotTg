import telebot.types

from consts import *
#from queries import *

TREE = []

@bot.message_handler(commands=['start'])
def send_start(message,initial = True ):
    """ Начало взаимодействия с ботом
            - данные пользователя сверяются с данными игроков команды
            - заправшиваются дополнительные данные, сохраняются в бд
    """


    """if message.chat.id not in PLAYERS_ID_LIST:
        if initial == True:
            bot.reply_to(message, f'Привет, для доступа обратись к админам команды')
    else:
        user = User(message)
        if initial == True:
            bot.reply_to(message,f'Привет, {user.name}!')"""

        # Реализация главного меню
    buttons_list = ['Моя биография','Моя статистика','Команда','Важная информация','Управление командой']
    menu_keyboard = Keyboard(buttons_list)

    bot.send_message(chat_id=message.chat.id,text='Главное меню',reply_markup=menu_keyboard.get_keyboard())

@bot.message_handler(func=lambda message: message.text == 'Вернуться')
def cancel(message):
    print(TREE)
    try:
        TREE.pop(-1)
    except:
        send_start(message)

    if not TREE.__len__():
        send_start(message,initial=False)
    else:
        parent = TREE[-1]
        if parent == 'Моя статистика':
            send_my_stat(message)
        if parent == 'По сезонам':
            send_my_by_season_stat(message)
        if parent == 'Команда':
            send_team(message)
        if parent == 'Турнирные таблицы':
            send_tables(message)
        if parent == 'Статистика команды':
            send_team_stat(message)
"""
--------------------------------------------------БЛОК МОЯ СТАТИСТИКА--------------------------------------------------
"""
@bot.message_handler(func=lambda message: message.text=='Моя статистика')
def send_my_stat(message):
    if message.text !='Вернуться':
        TREE.append(message.text) # добавляем родительский раздел, чтобы понять, какую статистику выдать

    buttons_list = ['По сезонам', 'За всё время','Вернуться']
    stat_keyboard = Keyboard(buttons_list)
    bot.send_message(chat_id=message.chat.id, text='Статистика', reply_markup=stat_keyboard.get_keyboard())

@bot.message_handler(func=lambda message: message.text == 'За всё время')
def send_my_all_time_stat(message):
    pass

@bot.message_handler(func=lambda message: message.text=='По сезонам')
def send_my_by_season_stat(message):
    if message.text !='Вернуться':
        TREE.append(message.text) # добавляем родительский раздел, чтобы понять, какую статистику выдать

    buttons_list = ['Сезон 2021-2022', 'Текущий сезон','Вернуться']
    season_stat_keyboard = Keyboard(buttons_list)
    bot.send_message(chat_id=message.chat.id, text='Статистика по сезонам',reply_markup=season_stat_keyboard.get_keyboard())

"""
--------------------------------------------------БЛОК КОМАНДА--------------------------------------------------
"""
''' Посмотреть ответы на сообщения'''
# @bot.message_handler(func=lambda message: 1==1)
# def handle_text(message):
#     print(message.text)

@bot.message_handler(func=lambda message: message.text=='Команда')
def send_team(message):
    if message.text !='Вернуться':
        TREE.append(message.text) # добавляем родительский раздел, чтобы понять, какую статистику выдать

    buttons_list = ['Турнирные таблицы', 'Список игроков','Статистика команды','Вернуться']
    stat_keyboard = Keyboard(buttons_list)
    bot.send_message(chat_id=message.chat.id, text='Команда', reply_markup=stat_keyboard.get_keyboard())

@bot.message_handler(func=lambda message: message.text=='Турнирные таблицы')
def send_tables(message):
    if message.text !='Вернуться':
        TREE.append(message.text) # добавляем родительский раздел, чтобы понять, какую статистику выдать

    buttons_list = ['Лига','Кубок','Вернуться']
    stat_keyboard = Keyboard(buttons_list)
    bot.send_message(chat_id=message.chat.id, text='Турнирные таблицы', reply_markup=stat_keyboard.get_keyboard())
 
@bot.message_handler(func=lambda message: message.text=='Статистика команды')
def send_team_stat(message):
    if message.text !='Вернуться':
        TREE.append(message.text) # добавляем родительский раздел, чтобы понять, какую статистику выдать

    buttons_list = ['По сезонам', 'За всё время','Вернуться']
    stat_keyboard = Keyboard(buttons_list)
    bot.send_message(chat_id=message.chat.id, text='Статистика команды', reply_markup=stat_keyboard.get_keyboard())

"""@bot.message_handler(func=lambda message: message.text=='По сезонам')
def send_team_by_season_stat(message):
    if message.text !='Вернуться':
        TREE.append(message.text) # добавляем родительский раздел, чтобы понять, какую статистику выдать

    buttons_list = ['Сезон 2021-2022', 'Текущий сезон','Вернуться']
    season_stat_keyboard = Keyboard(buttons_list)
    bot.send_message(chat_id=message.chat.id, text='Статистика команды по сезонам',reply_markup=season_stat_keyboard.get_keyboard())

@bot.message_handler(func=lambda message: message.text == 'За всё время')
def send_team_all_time_stat(message):
    pass"""


"""
--------------------------------------------------БЛОК УПРАВЛЕНИЕ КОМАНДОЙ--------------------------------------------------
"""
@bot.message_handler(func=lambda message: message.text=='Управление командой')
def team_management(message):
    if message.text !='Вернуться':
        TREE.append(message.text) # добавляем родительский раздел, чтобы понять, какую статистику выдать

    buttons_list = ['Добавить/Удалить игрока', 'Добавить/Удалить статистику','Вернуться']
    team_management_keyboard = Keyboard(buttons_list)
    bot.send_message(chat_id=message.chat.id, text='Меню управления командой',
                     reply_markup=team_management_keyboard.get_keyboard())

@bot.message_handler(func=lambda message: message.text=='Добавить/Удалить игрока')
def add_delete_player_pt1(message):
    if message.text !='Вернуться':
        TREE.append(message.text) # добавляем родительский раздел, чтобы понять, какую статистику выдать

    buttons_list = ['Вернуться']
    add_new_player_keyboard = Keyboard(buttons_list)
    bot.send_message(chat_id=message.chat.id, text='Добавление игрока',
                     reply_markup=add_new_player_keyboard.get_keyboard())

    player_info = []
    bot.send_message(chat_id=message.chat.id,text='Введите фамилию и имя игрока')
    bot.register_next_step_handler(message, type_player_name,player_info)

def type_player_name(message,player_info):
    ''' Админ вводит имя игрока с клавиатуры'''
    name = message.text
    #if validate_field(name) == True: # todo добавить проверку введного значения
    player_info.append(name)
    bot.send_message(chat_id=message.chat.id,text='Введите номер игрока')
    bot.register_next_step_handler(message, type_player_number,player_info)

def type_player_number(message,player_info):
    ''' Админ вводит игровой номер игрока с клавиатуры'''
    number = message.text
    #if validate_field(name) == True: # todo добавить проверку введного значения
    number = int(number)
    player_info.append(number)
    add_delete_player_pt2(message.chat.id,player_info)
    # add_player_to_db(player_info)

def add_delete_player_pt2(chat_id,player_info):
    name, number = player_info[0],player_info[1]
    str_player_info = f'Игрок: {name},\nИгровой номер: {number}'

    inline_buttons = [
        [
          InlineKeyboardButton(text='Добавить',callback_data='create'),
          InlineKeyboardButton(text='Удалить', callback_data='delete')
        ],
    ]
    add_or_delete_kb = InlineKeyboardMarkup(inline_buttons)
    bot.send_message(chat_id,str_player_info,reply_markup=add_or_delete_kb)

# @bot.callback_query_handler()
# def process_add_or_delete_kb(callback):
#     if callback.data == 'create':
#         print('create')
#     if callback.data == 'create':
#         print('delete')

@bot.message_handler(func=lambda message: message.text=='Удалить игрока')
def delete_player(message):
    pass


