import telebot.types

from consts import *
<<<<<<< HEAD
#from queries import *

=======
from queries import *
>>>>>>> c96f778764f1b5b03613f332039ee8362f67a27f

TREE = []

@bot.message_handler(commands=['start'])
def send_start(message,initial = True ):
    """ Начало взаимодействия с ботом
            - данные пользователя сверяются с данными игроков команды
            - заправшиваются дополнительные данные, сохраняются в бд
    """


<<<<<<< HEAD
    """if message.chat.id not in PLAYERS_ID_LIST:
=======
    if message.chat.id not in PLAYERS_ID_LIST:
>>>>>>> c96f778764f1b5b03613f332039ee8362f67a27f
        if initial == True:
            bot.reply_to(message, f'Привет, для доступа обратись к админам команды')
    else:
        user = User(message)
        if initial == True:
<<<<<<< HEAD
            bot.reply_to(message,f'Привет, {user.name}!')"""

        # Реализация главного меню
    buttons_list = ['Моя биография','Моя статистика','Команда','Важная информация','Управление командой']
    menu_keyboard = Keyboard(buttons_list)

    bot.send_message(chat_id=message.chat.id,text='Главное меню',reply_markup=menu_keyboard.get_keyboard())
=======
            bot.reply_to(message,f'Привет, {user.name}!')

        # Реализация главного меню
        buttons_list = ['Моя биография','Моя статистика','Команда','Важная информация','Управление командой']
        menu_keyboard = Keyboard(buttons_list)

        bot.send_message(chat_id=message.chat.id,text='Главное меню',reply_markup=menu_keyboard.get_keyboard())
>>>>>>> c96f778764f1b5b03613f332039ee8362f67a27f

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
<<<<<<< HEAD
        if parent == 'По сезонам':
            send_by_season_stat(message)
        if parent =='Команда':
            send_team(message)
        if parent =='Турнирные таблицы':
            send_tables(message)
        if parent == 'Статистика команды':
            send_team_stats(message)
        if parent == 'Важная информация':
            send_information(message)
=======
        if parent == 'Статистика':
            pass # добавить процедуру, которая обрабатывает Статистика
        if parent == 'По сезонам':
            send_by_season_stat(message)

>>>>>>> c96f778764f1b5b03613f332039ee8362f67a27f
"""
--------------------------------------------------БЛОК МОЯ СТАТИСТИКА--------------------------------------------------
"""
@bot.message_handler(func=lambda message: message.text=='Моя статистика')
def send_my_stat(message):
    if message.text !='Вернуться':
        TREE.append(message.text) # добавляем родительский раздел, чтобы понять, какую статистику выдать

    buttons_list = ['По сезонам', 'За всё время','Вернуться']
    stat_keyboard = Keyboard(buttons_list)
<<<<<<< HEAD
    bot.send_message(chat_id=message.chat.id, text='Моя татистика', reply_markup=stat_keyboard.get_keyboard())
=======
    bot.send_message(chat_id=message.chat.id, text='Статистика', reply_markup=stat_keyboard.get_keyboard())
>>>>>>> c96f778764f1b5b03613f332039ee8362f67a27f

@bot.message_handler(func=lambda message: message.text == 'За всё время')
def send_all_time_stat(message):
    pass

@bot.message_handler(func=lambda message: message.text=='По сезонам')
def send_by_season_stat(message):
    if message.text !='Вернуться':
        TREE.append(message.text) # добавляем родительский раздел, чтобы понять, какую статистику выдать

    buttons_list = ['Сезон 2021-2022', 'Текущий сезон','Вернуться']
    season_stat_keyboard = Keyboard(buttons_list)
    bot.send_message(chat_id=message.chat.id, text='Статистика по сезонам',
                     reply_markup=season_stat_keyboard.get_keyboard())

@bot.message_handler(func=lambda message: message.text=='Сезон 2021-2022')
def send_21_22season_stat(message):
    if message.text!='Вернуться':
        TREE.append(message.text) # добавляем родительский раздел, чтобы понять, какую статистику выдать
        season_stat = get_stat(TREE)

    """запросить инфу из бд?
    каким образом она будет выводится?
    вариант- открывается меню 'Сезон 2021-2022', там две кнопки- 'Вывести информацию' и 'Вернуться'.
     Информация выводится bot.replay_to 
     update- вариант говна"""
@bot.message_handler(func=lambda message:  message.text=='Текущий сезон')
def send_current_season_stat(message):
    if message.text!='Вернуться':
        TREE.append(message.text) # добавляем родительский раздел, чтобы понять, какую статистику выдать
    """запросить инфу из бд?
    каким образом она будет выводится?
    вариант- открывается меню 'Сезон 2021-2022', там две кнопки- 'Вывести информацию' и 'Вернуться'.
     Информация выводится bot.replay_to 
     update- вариант говна"""



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

    buttons_list = ['Турнирные таблицы', 'Статистика команды','Список игроков','Вернуться']
    stat_keyboard = Keyboard(buttons_list)
    bot.send_message(chat_id=message.chat.id, text='Команда', reply_markup=stat_keyboard.get_keyboard())

@bot.message_handler(func=lambda message: message.text=='Турнирные таблицы')    
def send_tables(message):
    if message.text !='Вернуться':
        TREE.append(message.text) # добавляем родительский раздел, чтобы понять, какую статистику выдать

    buttons_list = ['Лига','Кубок','Вернуться']
    stat_keyboard = Keyboard(buttons_list)
    bot.send_message(chat_id=message.chat.id, text='Турнирные таблицы', reply_markup=stat_keyboard.get_keyboard())

"""
@bot.message_handler(func=lambda message: message.text=='Лига')    
def send_team(message):
    if message.text !='Вернуться':
        TREE.append(message.text) # добавляем родительский раздел, чтобы понять, какую статистику выдать
....
        
@bot.message_handler(func=lambda message: message.text=='Лига')    
def send_team(message):
    if message.text !='Вернуться':
        TREE.append(message.text) # добавляем родительский раздел, чтобы понять, какую статистику выдать
....

    вообще ноль идей как показывать турнирную таблицу
    из бд выводить галь полная
    обновлять каждый раз скрины с сайта офлк- дерьмо дерьма
    соответственно- нахуй убрать раздел"""
@bot.message_handler(func=lambda message: message.text=='Статистика команды')    
<<<<<<< HEAD
def send_team_stats(message):
=======
def send_tables(message):
>>>>>>> c96f778764f1b5b03613f332039ee8362f67a27f
    if message.text !='Вернуться':
        TREE.append(message.text) # добавляем родительский раздел, чтобы понять, какую статистику выдать

    buttons_list = ['Ну и как её блять выводить','Вернуться']
    stat_keyboard = Keyboard(buttons_list)
    bot.send_message(chat_id=message.chat.id, text='Статистика команды', reply_markup=stat_keyboard.get_keyboard())
"""ремарки аналогичные предыдущим"""
"""
-------------------------------------------------Блок ВАЖНАЯ ИНФОРМАЦИЯ-----------------------------------------------------
не назвать ли его Расписанием?"""
@bot.message_handler(func=lambda message: message.text=='Важная информация')
def send_information(message):
    if message.text !='Вернуться':
        TREE.append(message.text) # добавляем родительский раздел, чтобы понять, какую статистику выдать

    buttons_list = ['Следующая игра','Следующая тренировка','Вернуться']
    stat_keyboard = Keyboard(buttons_list)
    bot.send_message(chat_id=message.chat.id, text='Важная информация', reply_markup=stat_keyboard.get_keyboard())

@bot.message_handler(func=lambda message: message.text=='Следующая игра')
def send_next_game(message):
    if message.text !='Вернуться':
        TREE.append(message.text) # добавляем родительский раздел, чтобы понять, какую статистику выдать

    buttons_list = ['Как эту хуйню тут вставишь. Кнопку сделать var? От меня мать откажется если так сделать','Вернуться']
    stat_keyboard = Keyboard(buttons_list)
    bot.send_message(chat_id=message.chat.id, text='Следующая игра', reply_markup=stat_keyboard.get_keyboard())

@bot.message_handler(func=lambda message: message.text=='Следующая тренировка')
def send_next_train(message):
    if message.text !='Вернуться':
        TREE.append(message.text) # добавляем родительский раздел, чтобы понять, какую статистику выдать
    
    buttons_list = ['Как эту хуйню тут вставишь. Кнопку сделать var? От меня мать откажется если так сделать','Вернуться']
    stat_keyboard = Keyboard(buttons_list)
    bot.send_message(chat_id=message.chat.id, text='Следующая тренировка', reply_markup=stat_keyboard.get_keyboard())

"""
--------------------------------------------------БЛОК УПРАВЛЕНИЕ КОМАНДОЙ--------------------------------------------------
А на кой хер, если уж подумать по-человечески"""
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
