import psycopg as pg

class Conn:
    def __init__(self,params):
        self.host,self.port = params[0], params[1]
        self.dbname,self.user,self.pwd = params[2],params[3],params[4]
        self.type = params[5]
        self.connection = pg.connect(host = self.host,port = self.port,dbname = self.dbname,
                                     user = self.user,password = self.pwd)

        self.crs = self.connection.cursor()

<<<<<<< HEAD
    """def execute(self,sql):
=======
    def execute(self,sql):
>>>>>>> c96f778764f1b5b03613f332039ee8362f67a27f
        if self.type == 'PG':
            self.crs.execute(sql)
    def fetch_next(self):
        if self.type == 'PG':
<<<<<<< HEAD
            return self.crs.fetchone()"""
=======
            return self.crs.fetchone()
>>>>>>> c96f778764f1b5b03613f332039ee8362f67a27f
def get_conn_params():
    with open('files/config.txt') as f:
        return f.readline().split(';')

db_session = Conn(get_conn_params())