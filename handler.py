import telebot.types
from telebot import types
from consts import *
from queries import *
from conn import *

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
        if parent == 'Моя статистика за всё время':
            send_my_all_time_stat(message)
        if parent == 'Моя статистика по сезонам':
            send_my_by_season_stat(message)
        if parent == 'Моя статистика за сезон 2022':
            send_my_season_2022_stat(message)
        if parent == 'Моя статистика за текущий сезон':
            send_my_season_2023_stat(message)
        if parent == 'Команда':
            send_team(message)
        if parent == 'Турнирные таблицы':
            send_tables(message)
        if parent == 'Статистика команды':
            send_team_stat(message)
        if parent == 'Статистика команды за всё время':
            send_team_all_time_stat(message)
        if parent == 'Статистика команды за сезон 2022':
            send_team_season_2022_stat(message)
        if parent == 'Статистика команды за текущий сезон':
            send_team_season_2023_stat(message)    
        if parent == 'Список игроков':
            send_players_list(message)



"""
--------------------------------------------------БЛОК МОЯ СТАТИСТИКА--------------------------------------------------
"""
@bot.message_handler(func=lambda message: message.text=='Моя статистика')
def send_my_stat(message):
    if message.text !='Вернуться':
        TREE.append(message.text) # добавляем родительский раздел, чтобы понять, какую статистику выдать

    buttons_list = ['Моя статистика по сезонам', 'Моя статистика за всё время','Вернуться']
    my_stat_keyboard = Keyboard(buttons_list)
    bot.send_message(chat_id=message.chat.id, text='Статистика', reply_markup=my_stat_keyboard.get_keyboard())

@bot.message_handler(func=lambda message: message.text =='Моя статистика за всё время')
def send_my_all_time_stat(message):
    if message.text !='Вернуться':
        TREE.append(message.text) # добавляем родительский раздел, чтобы понять, какую статистику выдать

    buttons_list = ['Вернуться']
    my_all_time_stat_keyboard = Keyboard(buttons_list)
    my_all_time_stat=db_my_all_time_stat()

    bot.send_message(chat_id=message.chat.id, text=f'Игры: {my_all_time_stat[0][0]}\nГолы: {my_all_time_stat[0][1]}\nГолевые передачи: {my_all_time_stat[0][2]}\nЖёлтые карточки: {my_all_time_stat[0][3]}\nКрасные карточки: {my_all_time_stat[0][4]}', reply_markup=my_all_time_stat_keyboard.get_keyboard())

@bot.message_handler(func=lambda message: message.text=='Моя статистика по сезонам')
def send_my_by_season_stat(message):
    if message.text !='Вернуться':
        TREE.append(message.text) # добавляем родительский раздел, чтобы понять, какую статистику выдать

    buttons_list = ['Моя статистика за сезон 2022', 'Моя статистика за текущий сезон','Вернуться']
    my_by_season_stat_keyboard = Keyboard(buttons_list)
    bot.send_message(chat_id=message.chat.id, text='Моя статистика по сезонам',reply_markup=my_by_season_stat_keyboard.get_keyboard())

@bot.message_handler(func=lambda message: message.text=='Моя статистика за текущий сезон')
def send_my_season_2023_stat(message):
    if message.text !='Вернуться':
        TREE.append(message.text) # добавляем родительский раздел, чтобы понять, какую статистику выдать

    buttons_list = ['Вернуться']
    my_2023_stat_keyboard = Keyboard(buttons_list)
    my_2023_stat=db_my_season_2023_stat()
    bot.send_message(chat_id=message.chat.id, text=f'Игры: {my_2023_stat[0][0]}\nГолы: {my_2023_stat[0][1]}\nГолевые передачи: {my_2023_stat[0][2]}\nЖёлтые карточки: {my_2023_stat[0][3]}\nКрасные карточки: {my_2023_stat[0][4]}', reply_markup=my_2023_stat_keyboard.get_keyboard())

@bot.message_handler(func=lambda message: message.text=='Моя статистика за сезон 2022')
def send_my_season_2022_stat(message):
    if message.text !='Вернуться':
        TREE.append(message.text) # добавляем родительский раздел, чтобы понять, какую статистику выдать

    buttons_list = ['Вернуться']
    my_2022_stat_keyboard = Keyboard(buttons_list)
    my_2022_stat=db_my_season_2022_stat()
    bot.send_message(chat_id=message.chat.id, text=f'Игры: {my_2022_stat[0][0]}\nГолы: {my_2022_stat[0][1]}\nГолевые передачи: {my_2022_stat[0][2]}\nЖёлтые карточки: {my_2022_stat[0][3]}\nКрасные карточки: {my_2022_stat[0][4]}', reply_markup=my_2022_stat_keyboard.get_keyboard())

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
        TREE.append(message.text)

    buttons_list = ['Турнирные таблицы', 'Список игроков','Статистика команды','Вернуться']
    stat_keyboard = Keyboard(buttons_list)
    bot.send_message(chat_id=message.chat.id, text='Команда', reply_markup=stat_keyboard.get_keyboard())

@bot.message_handler(func=lambda message: message.text=='Турнирные таблицы')
def send_tables(message):
    if message.text !='Вернуться':
        TREE.append(message.text) 

    buttons_list = ['Лига','Кубок','Вернуться']
    stat_keyboard = Keyboard(buttons_list)
    bot.send_message(chat_id=message.chat.id, text='Турнирные таблицы', reply_markup=stat_keyboard.get_keyboard())
    
@bot.message_handler(func=lambda message: message.text=='Список игроков')
def send_players_list(message):
    if message.text !='Вернуться':
        TREE.append(message.text) # добавляем родительский раздел, чтобы понять, какую статистику выдать

    buttons_list = ['Вернуться']
    stat_keyboard = Keyboard(buttons_list)

    player_list=db_player_list()
    #link_list= db_link_list()
    #link=""
    msg=""
    for i in range (0,len(player_list)):
        msg+=f'{player_list[i][1]}\nНомер:{player_list[i][0]}\n,{player_list[i][2]}\n'

    bot.send_message(chat_id=message.chat.id, text=msg, reply_markup=stat_keyboard.get_keyboard())

@bot.message_handler(func=lambda message: message.text=='Статистика команды')
def send_team_stat(message):
    if message.text !='Вернуться':
        TREE.append(message.text) 

    buttons_list = ['Статистика команды по сезонам', 'Статистика команды за всё время','Вернуться']
    stat_keyboard = Keyboard(buttons_list)
    bot.send_message(chat_id=message.chat.id, text='Статистика команды', reply_markup=stat_keyboard.get_keyboard())

@bot.message_handler(func=lambda message: message.text=='Статистика команды за всё время')
def send_team_all_time_stat(message):
    if message.text !='Вернуться':
        TREE.append(message.text)

    buttons_list = ['Вернуться']
    team_stat_keyboard = Keyboard(buttons_list)

    team_stat=db_team_all_time_stat()
    bot.send_message(chat_id=message.chat.id, text=f'Игры:{team_stat[0][0]}\nПобеды:{team_stat[0][1]}\nПоражения:{team_stat[0][2]}\nНичьи:{team_stat[0][3]}\nГолов забито:{team_stat[0][4]}\nГолов пропущено:{team_stat[0][5]}\nЖёлтые карточки:{team_stat[0][6]}\nКрасные карточки:{team_stat[0][7]}', reply_markup=team_stat_keyboard.get_keyboard())

@bot.message_handler(func=lambda message: message.text=='Статистика команды по сезонам')
def send_team_by_season_stat(message):
    if message.text !='Вернуться':
        TREE.append(message.text)

    buttons_list = ['Статистика команды за сезон 2022', 'Статистика команды за текущий сезон', 'Вернуться']
    team_by_season_keyboard = Keyboard(buttons_list)

    bot.send_message(chat_id=message.chat.id, text='Статика команды по сезонам' , reply_markup=team_by_season_keyboard.get_keyboard())

@bot.message_handler(func=lambda message: message.text=='Статистика команды за сезон 2022')
def send_team_season_2022_stat(message):
    if message.text !='Вернуться':
        TREE.append(message.text)

    buttons_list = ['Вернуться']
    team_22_keyboard = Keyboard(buttons_list)

    team_22=db_team_season_2022_stat()
    bot.send_message(chat_id=message.chat.id, text=f'Игры:{team_22[0][0]}\nПобеды:{team_22[0][1]}\nПоражения:{team_22[0][2]}\nНичьи:{team_22[0][3]}\nГолов забито:{team_22[0][4]}\nГолов пропущено:{team_22[0][5]}\nЖёлтые карточки:{team_22[0][6]}\nКрасные карточки:{team_22[0][7]}', reply_markup=team_22_keyboard.get_keyboard())

@bot.message_handler(func=lambda message: message.text=='Статистика команды за текущий сезон')
def send_team_season_2023_stat(message):
    if message.text !='Вернуться':
        TREE.append(message.text)

    buttons_list = ['Вернуться']
    team_23_keyboard = Keyboard(buttons_list)

    team_23=db_team_season_2023_stat()
    bot.send_message(chat_id=message.chat.id, text=f'Игры:{team_23[0][0]}\nПобеды:{team_23[0][1]}\nПоражения:{team_23[0][2]}\nНичьи:{team_23[0][3]}\nГолов забито:{team_23[0][4]}\nГолов пропущено:{team_23[0][5]}\nЖёлтые карточки:{team_23[0][6]}\nКрасные карточки:{team_23[0][7]}', reply_markup=team_23_keyboard.get_keyboard())





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


