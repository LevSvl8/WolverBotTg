import telebot
from telebot.types import InlineKeyboardMarkup,ReplyKeyboardMarkup
from telebot.types import InlineKeyboardButton,KeyboardButton
<<<<<<< HEAD
=======

from queries import *
import os, json, requests
>>>>>>> c96f778764f1b5b03613f332039ee8362f67a27f

#from queries import *
#import os, json, requests
def get_token():
    with open('files/token.txt') as f:
        return f.readline()

TOKEN = get_token()
URL = 'https://api.telegram.org/bot'

bot = telebot.TeleBot(TOKEN)

PLAYERS_ID_LIST = [878297528,1548423795]
ANSWERS_FILENAME = 'files/user_answers.json'

<<<<<<< HEAD
"""def get_data_from_json_file(path):
=======
def get_data_from_json_file(path):
>>>>>>> c96f778764f1b5b03613f332039ee8362f67a27f
    if not os.path.exists(path):
        return None
    with open(path,'r',encoding='utf8') as f:
        data = json.loads(f.read())
    return data

def load_data_to_json_file(path,data):
    with open(path, 'w', encoding='utf8') as f:
        return json.dump(data,f)

def add_answer(chat_id,answer):
    answers = get_data_from_json_file(ANSWERS_FILENAME)
    answers['answers'][chat_id] = answer
    load_data_to_json_file(ANSWERS_FILENAME,answers)

def delete_answer(chat_id):
    answers:dict = get_data_from_json_file(ANSWERS_FILENAME)
    if chat_id in answers['answers']:
        answers.pop(chat_id)
    load_data_to_json_file(ANSWERS_FILENAME,answers)

def read_answer(chat_id):
    answers = get_data_from_json_file(ANSWERS_FILENAME)
    value = answers['answers'].get(chat_id)
    delete_answer(chat_id)
    return value

def validate_field(value):
    pass

def get_updates():
    updates = requests.get(f'{URL}{TOKEN}/getUpdates?offset=0').json()['result']
    return updates
<<<<<<< HEAD
"""
=======

>>>>>>> c96f778764f1b5b03613f332039ee8362f67a27f
class Keyboard:
    def __init__(self, captions):
        self.keyboard = ReplyKeyboardMarkup(row_width=1,
                                            resize_keyboard=False,
                                            one_time_keyboard=True)
        self.add_buttons(captions)
    def get_keyboard(self):
        return self.keyboard
    def add_buttons(self, captions):
        for caption in captions:
            button = KeyboardButton(text=caption)
            self.keyboard.add(button)

class User:
    def __init__(self, message):
        self.tg_id = int(message.chat.id)

        self.name = get_player_name(db_session,self.tg_id)
<<<<<<< HEAD
        
=======
>>>>>>> c96f778764f1b5b03613f332039ee8362f67a27f
