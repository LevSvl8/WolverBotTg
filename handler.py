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