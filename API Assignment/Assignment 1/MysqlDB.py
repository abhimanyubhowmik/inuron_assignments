import mysql.connector as conn
import Logging

logging = Logging.db_logging()

class Connection:

    def __init__(self,host,user,passwd):
        self.host = host
        self.user = user
        self.passwd = passwd

    def db(self):
        try:
            db = conn.connect(host=self.host,user=self.user,passwd=self.passwd)
            return db
        except Exception as exp:
            logging.error(exp)

    def cursor(self):
        try:
            db = conn.connect(host=self.host,user=self.user,passwd=self.passwd)
            cursor = db.cursor()
            return cursor
        except Exception as exp:
            logging.error(exp)

class Database:

    def __init__(self,cursor):
        self.cursor = cursor

    def showDatabase(self):
        try:
            self.cursor.execute('show databases')
            return self.cursor.fetchall()
        except Exception as exp:
            logging.error(exp)
    
    def showTable(self,databaseName):
        try:
            self.cursor.execute('use {db}'.format(db=databaseName))
            self.cursor.execute('show tables')
            print(self.cursor.fetchall())
        except Exception as exp:
            logging.error(exp)

    def fetchData(self,databaseName,tableName):
        try:
            self.cursor.execute('select * from {database}.{table}'.format(database=databaseName, table = tableName))
            return self.cursor.fetchall()
        except Exception as exp:
            logging.error(exp)
