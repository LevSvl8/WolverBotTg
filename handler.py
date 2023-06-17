from consts import *

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
        menu_keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)

        my_bio = telebot.types.KeyboardButton(text='Моя биография') # биография
        my_stat = telebot.types.KeyboardButton(text='Моя статистика') # статистика
        my_team = telebot.types.KeyboardButton(text='Команда') # команда
        
        admin_mode = telebot.types.KeyboardButton(text='Управление командой')

        info = telebot.types.KeyboardButton(text='Важная информация')

        menu_keyboard.add(my_bio,my_stat, my_team, admin_mode, info)
        bot.send_message(chat_id=message.chat.id,text='Главное меню',reply_markup=menu_keyboard)
        

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