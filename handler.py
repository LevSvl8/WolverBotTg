from consts import *
from queries import *

TREE = []

@bot.message_handler(commands=['start'])
def send_start(message):
    """ Начало взаимодействия с ботом
            - данные пользователя сверяются с данными игроков команды
            - заправшиваются дополнительные данные, сохраняются в бд
    """
    if message.chat.id not in PLAYERS_ID_LIST:
        bot.reply_to(message, f'Привет, для доступа обратись к админам команды')
    else:
        bot.reply_to(message,f'Привет!')

        # Реализация главного меню
        buttons_list = ['Моя биография','Моя статистика','Команда',
                        'Управление командой','Важная информация']
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
        send_start(message)
    else:
        parent = TREE[-1]
        if parent == 'Моя статистика':
            send_stat(message)
        if parent == 'Статистика':
            pass # добавить процедуру, которая обрабатывает Статистика
        if parent == 'По сезонам':
            send_season_stat(message)


"""
--------------------------------------------------БЛОК СТАТИСТИКА--------------------------------------------------
"""
@bot.message_handler(func=lambda message: message.text=='Моя статистика' or  message.text == 'Статистика')
def send_stat(message):
    if message.text !='Вернуться':
        TREE.append(message.text) # добавляем родительский раздел, чтобы понять, какую статистику выдать

    buttons_list = ['По сезонам', 'За всё время','Вернуться']
    stat_keyboard = Keyboard(buttons_list)
    bot.send_message(chat_id=message.chat.id, text='Статистика', reply_markup=stat_keyboard.get_keyboard())

@bot.message_handler(func=lambda message: message.text == 'За всё время')
def send_all_time_stat(message):
    pass

@bot.message_handler(func=lambda message: message.text=='По сезонам')
def send_season_stat(message):
    if message.text !='Вернуться':
        TREE.append(message.text) # добавляем родительский раздел, чтобы понять, какую статистику выдать

    buttons_list = ['Прошлый сезон', 'Текущий сезон','Вернуться']
    season_stat_keyboard = Keyboard(buttons_list)
    bot.send_message(chat_id=message.chat.id, text='Статистика по сезонам', reply_markup=season_stat_keyboard.get_keyboard())

@bot.message_handler(func=lambda message: message.text=='Прошлый сезон' or message.text=='Текущий сезон')
def send_season_stat(message):
    TREE.append(message.text) # добавляем родительский раздел, чтобы понять, какую статистику выдать
    season_stat = get_stat(TREE)

''' Посмотреть ответы на сообщения'''
# @bot.message_handler(func=lambda message: 1==1)
# def handle_text(message):
#     print(message.text)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)
    if message.text=='Моя биография':
        bot.reply_to(message,message.text)

    if message.text=='Моя статистика':
        myStat_keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
        all_time= telebot.types.KeyboardButton(text='За всё время')
        by_season= telebot.types.KeyboardButton(text='По сезонам')

        myStat_keyboard.add(all_time, by_season)
        bot.send_message(chat_id=message.chat.id,text=message.text ,reply_markup=myStat_keyboard)

    if message.text=='По сезонам':
        by_season_keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
        recent_season= telebot.types.KeyboardButton(text='Текущий сезон')
        n_season=telebot.types.KeyboardButton(text='Нн-ый сезон')

        by_season_keyboard.add(recent_season, n_season)
        bot.send_message(chat_id=message.chat.id,text=message.text ,reply_markup=by_season_keyboard)

    if message.text=='За всё время':
        original_keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
        fact= telebot.types.KeyboardButton(text='Факт №1- я дрочу на себя')

        original_keyboard.add(fact)
        bot.send_message(chat_id=message.chat.id,text=message.text ,reply_markup=original_keyboard)

    if message.text=='Команда':
        team_keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
        tournament_tables= telebot.types.KeyboardButton(text='Турнирные таблицы')
        stat=telebot.types.KeyboardButton(text='Статистика')
        players_list=telebot.types.KeyboardButton(text='Список игроков')

        team_keyboard.add(tournament_tables, stat, players_list)
        bot.send_message(chat_id=message.chat.id,text=message.text ,reply_markup=team_keyboard)

    if message.text=='Турнирные таблицы':
        tournament_keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
        league= telebot.types.KeyboardButton(text='Лига')
        cup=telebot.types.KeyboardButton(text='Кубок')

        tournament_keyboard.add(league, cup)
        bot.send_message(chat_id=message.chat.id,text=message.text ,reply_markup=tournament_keyboard)

    if message.text=='Статистика':
        '''структура как в моя статистика'''
        bot.reply_to(message,'Рановато')

    if message.text=='Список игроков':
        bot.reply_to(message,'Доделать')

#добавить кнопку назад на каждую клавиатуру