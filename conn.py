class Conn:
    def __init__(self,params):
        self.host,self.port = params[0], params[1]
        self.dbname,self.user,self.pwd = params[2],params[3],params[4]
        self.type = params[5]
    def __enter__(self):
        if self.type == 'PG':
            import psycopg as pg
            self.connection = pg.connect(host = self.host,
                                         port = self.port,
                                         dbname = self.dbname,
                                         user = self.user,
                                         password = self.pwd)
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    def execute(self,sql):
        pass
    def fetch_next(self):
        pass