import telebot

def get_token():
    with open('files/token.txt') as f:
        return f.readline()

TOKEN = get_token()

bot = telebot.TeleBot(TOKEN)

PLAYERS_ID_LIST = [878297528]
