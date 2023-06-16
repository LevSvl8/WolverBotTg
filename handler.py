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

"""
--------------------------------------------------БЛОК СТАТИСТИКА--------------------------------------------------
"""
@bot.message_handler(func=lambda message: message.text=='Моя статистика' or  message.text == 'Статистика')
def send_stat(message):
    TREE.append(message.text) # добавляем родительский раздел, чтобы понять, какую статистику выдать

    buttons_list = ['По сезонам', 'За всё время']
    stat_keyboard = Keyboard(buttons_list)
    bot.send_message(chat_id=message.chat.id, text='Статистика', reply_markup=stat_keyboard.get_keyboard())

@bot.message_handler(func=lambda message: message.text == 'За всё время')
def send_all_time_stat(message):
    pass

@bot.message_handler(func=lambda message: message.text=='По сезонам')
def send_season_stat(message):
    TREE.append(message.text) # добавляем родительский раздел, чтобы понять, какую статистику выдать

    buttons_list = ['Прошлый сезон', 'Текущий сезон']
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


