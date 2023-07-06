import MySQLdb as ms
from getpass import getpass
from mysql.connector import connect, Error

def db_player_list():   
    try:
        with connect(
        host="127.0.0.1",
        user="root",
        password="obraz1401",
        database = ("wolver2023"),
        ) as connection:
            select_table_query = "select player_id, player_name, vk_id from players" 
            with connection.cursor() as cursor:
                cursor.execute(select_table_query)
                player_list=[]
                result = cursor.fetchall()
                for row in result:
                    player_list.append(row)
                return(player_list)
    except Error as e:
        print(e)
"""
def db_link_list():
    try:
        with connect(
        host="127.0.0.1",
        user="root",
        password="obraz1401",
        database = ("wolver2023"),
        ) as connection:
            select_table_query = "select vk_id from players" 
            with connection.cursor() as cursor:
                cursor.execute(select_table_query)
                link_list=[]
                result = cursor.fetchall()
                for row in result:
                    link_list.append(row)
                return(link_list)
    except Error as e:
        print(e)
"""
def db_my_all_time_stat():
    try:
        with connect(
        host="127.0.0.1",
        user="root",
        password="obraz1401",
        database = ("wolver2023"),
        ) as connection:
            select_table_query = "select games ,goals, assists, yellow_cards, red_cards from alltime_players_statistics where player_id=4" #where добавлен на время, чтобы не возникло путаницы с индексами в хэндлере
            with connection.cursor() as cursor:
                cursor.execute(select_table_query)
                player_list=[]
                result = cursor.fetchall()
                for row in result:
                    player_list.append(row)
                #print(player_list)
                return(player_list)
    except Error as e:
        print(e)

def db_my_season_2023_stat():
    try:
        with connect(
        host="127.0.0.1",
        user="root",
        password="obraz1401",
        database = ("wolver2023"),
        ) as connection:
            select_table_query = "select games ,goals, assists, yellow_cards, red_cards from season_2023_players_statistics where player_id=4" #where добавлен на время, чтобы не возникло путаницы с индексами в хэндлере
            with connection.cursor() as cursor:
                cursor.execute(select_table_query)
                player_list=[]
                result = cursor.fetchall()
                for row in result:
                    player_list.append(row)
                #print(player_list)
                return(player_list)
    except Error as e:
        print(e)

def db_my_season_2022_stat():
    try:
        with connect(
        host="127.0.0.1",
        user="root",
        password="obraz1401",
        database = ("wolver2023"),
        ) as connection:
            select_table_query = "select games ,goals, assists, yellow_cards, red_cards from season_2022_players_statistics where player_id=4" #where добавлен на время, чтобы не возникло путаницы с индексами в хэндлере
            with connection.cursor() as cursor:
                cursor.execute(select_table_query)
                player_list=[]
                result = cursor.fetchall()
                for row in result:
                    player_list.append(row)
                #print(player_list)
                return(player_list)
    except Error as e:
        print(e)

def db_team_all_time_stat():
    try:
        with connect(
        host="127.0.0.1",
        user="root",
        password="obraz1401",
        database = ("wolver2023"),
        ) as connection:
            select_table_query = "select * from alltime_team_statistics" #where добавлен на время, чтобы не возникло путаницы с индексами в хэндлере
            with connection.cursor() as cursor:
                cursor.execute(select_table_query)
                player_list=[]
                result = cursor.fetchall()
                for row in result:
                    player_list.append(row)
                #print(player_list)
                return(player_list)
    except Error as e:
        print(e)

def db_team_season_2022_stat():
    try:
        with connect(
        host="127.0.0.1",
        user="root",
        password="obraz1401",
        database = ("wolver2023"),
        ) as connection:
            select_table_query = "select * from season_2022_team_statistics" #where добавлен на время, чтобы не возникло путаницы с индексами в хэндлере
            with connection.cursor() as cursor:
                cursor.execute(select_table_query)
                player_list=[]
                result = cursor.fetchall()
                for row in result:
                    player_list.append(row)
                #print(player_list)
                return(player_list)
    except Error as e:
        print(e)

def db_team_season_2023_stat():
    try:
        with connect(
        host="127.0.0.1",
        user="root",
        password="obraz1401",
        database = ("wolver2023"),
        ) as connection:
            select_table_query = "select * from season_2023_team_statistics" #where добавлен на время, чтобы не возникло путаницы с индексами в хэндлере
            with connection.cursor() as cursor:
                cursor.execute(select_table_query)
                player_list=[]
                result = cursor.fetchall()
                for row in result:
                    player_list.append(row)
                #print(player_list)
                return(player_list)
    except Error as e:
        print(e)

class Conn:
    def __init__(self,params):
        self.host,self.port = params[0], params[1]
        self.database,self.user,self.pwd = params[2],params[3],params[4]
        self.type = params[5]
        self.connection = ms.connect(host = self.host,port = int(self.port),database = self.database,
                                     user = self.user,password = self.pwd)

        self.crs = self.connection.cursor()

    def execute(self,sql):
        if self.type == 'ms':
            self.crs.execute(sql)
    def fetch_next(self):
        if self.type == 'ms':
            return self.crs.fetchone()

def get_conn_params():
    with open('files/config.txt') as f:
        return f.readline().split(';')

db_session= Conn(get_conn_params())


    


