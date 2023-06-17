from conn import *

def get_stat(tree):

    sql = "SELECT p.player_name, games, goals, asists\
    FROM wolver.players p\
    JOIN wolver.stats s ON p.player_id = s.player_id"

    where_clause = ''

    if tree[0] == 'Моя статистика':
        pass
    elif tree[0] == 'Статистика':
        pass

    if tree[1] == 'За все время':
        pass
    elif tree[1] == 'По сезонам':

        if tree[2] == 'Прошлый сезон':
            pass
        elif tree[2] == 'Текущий сезон':
            pass

    sql = ''
    return sql