import telebot

def get_token():
    with open('files/token.txt') as f:
        return f.readline()

TOKEN = get_token()

bot = telebot.TeleBot(TOKEN)

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


