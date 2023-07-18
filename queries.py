from conn import *

def get_player_name(conn,tg_id) -> int:
    sql = f'select name from players where tg_id={tg_id}'
    conn.execute(sql)
    player_name = conn.fetch_next()
    return player_name[0].split(' ')[1]

def get_player_number(conn,tg_id):
    sql = f'select number from players where tg_id={tg_id}'
    conn.execute(sql)
    number =''
    result=conn.fetch_next()
    for row in result:
        number=row
    return(number)

def db_players_list(conn):
    sql="select number, name, vk_id from players"
    conn.execute(sql)
    list=[]
    result=conn.fetch_all()
    for row in result:
        list.append(row)
    return(list)

number=4

def db_player_all_time_stat(conn):
    sql=f"select games, goals, assists, yellow_cards, red_cards from players_stat_alltime where number={number}"
    conn.execute(sql)
    stat=[]
    result=conn.fetch_all()
    for row in result:
        stat.append(row)
    return(stat)

def db_player_season_2023_stat(conn):
    sql=f"select games, goals, assists, yellow_cards, red_cards from players_stat_season_2023 where number=4"
    conn.execute(sql)
    stat=[]
    result=conn.fetch_all()
    for row in result:
        stat.append(row)
    return(stat)

def db_player_season_2022_stat(conn):
    sql=f"select games, goals, assists, yellow_cards, red_cards from players_stat_season_2022 where number=4"
    conn.execute(sql)
    stat=[]
    result=conn.fetch_all()
    for row in result:
        stat.append(row)
    return(stat)

def db_team_all_time_stat(conn):
    sql="select * from team_stat_all_time"
    conn.execute(sql)
    stat=[]
    result=conn.fetch_all()
    for row in result:
        stat.append(row)
    return(stat)

def db_team_season_2022_stat(conn):
    sql="select * from team_stat_season_2022"
    conn.execute(sql)
    stat=[]
    result=conn.fetch_all()
    for row in result:
        stat.append(row)
    return(stat)

def db_team_season_2023_stat(conn):
    sql="select * from team_stat_season_2023"
    conn.execute(sql)
    stat=[]
    result=conn.fetch_all()
    for row in result:
        stat.append(row)
    return(stat)

def db_insert(conn,player_info):
    number=player_info[1]
    name= player_info[0]
    sql=f"insert into players (number, name) values({number}, '{name}')"
    conn.execute(sql)
    check="select * from players where number=2"
    conn.execute(check)
    line=[]
    result=conn.fetch_all()
    for row in result:
        line.append(row)
        print(line)
    return(line)

def db_count(conn):
    sql="select count(id) from players"
    conn.execute(sql)
    line=[]
    result=conn.fetch_all()
    for row in result:
        line.append(row)
        print(line)
    return(line)

def add_player_to_db(player_info):
    print(player_info)