import telebot
from queries import *

def get_token():
    with open('files/token.txt') as f:
        return f.readline()

def get_conn_params():
    with open('files/config.txt') as f:
        return f.readline().split(';')

TOKEN = get_token()

bot = telebot.TeleBot(TOKEN)
db_session = Conn(get_conn_params())
PLAYERS_ID_LIST = [878297528,1548423795]

class Keyboard:
    def __init__(self, captions):
        self.keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
        self.add_buttons(captions)
    def get_keyboard(self):
        return self.keyboard
    def add_buttons(self, captions):
        for caption in captions:
            button = telebot.types.KeyboardButton(text=caption)
            self.keyboard.add(button)

class User:
    def __init__(self, message):
        self.tg_id = int(message.chat.id)

        self.name = get_player_name(db_session,self.tg_id)
