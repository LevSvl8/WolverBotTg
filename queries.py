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

def db_player_all_time_stat(conn,player_info):
    tg_id=player_info[0]
    sql=f"select games, goals, assists, yellow_cards, red_cards from players_stat_all_time psat join players p on p.number=psat.number where tg_id={tg_id}"
    conn.execute(sql)
    stat=[]
    result=conn.fetch_all()
    for row in result:
        stat.append(row)
    return(stat)

def db_player_season_2023_stat(conn,player_info):
    tg_id=player_info[0]
    sql=f"select games, goals, assists, yellow_cards, red_cards from players_stat_season_2023 pss23 join players p on p.number=pss23.number where tg_id={tg_id}"    
    conn.execute(sql)
    stat=[]
    result=conn.fetch_all()
    for row in result:
        stat.append(row)
    return(stat)

def db_player_season_2022_stat(conn,player_info):
    tg_id=player_info[0]
    sql=f"select games, goals, assists, yellow_cards, red_cards from players_stat_season_2022 pss22 join players p on p.number=pss22.number where tg_id={tg_id}"
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

def db_insert_player(conn,player_info):
    number=player_info[1]
    name= player_info[0]
    tg_id=player_info[2]
    sql=f"insert into players (number, name, tg_id) values({number}, '{name}', {tg_id})"
    conn.execute(sql)

def db_delete_player(conn, player_info):
    number=player_info[0]
    sql=f"delete from players where number={number}"
    conn.execute(sql)

def db_insert_vk_id(conn,player_info):
    number= player_info[0]
    vk_id= player_info[1]
    sql=f"update players set vk_id='{vk_id}' where number={number}"
    conn.execute(sql)