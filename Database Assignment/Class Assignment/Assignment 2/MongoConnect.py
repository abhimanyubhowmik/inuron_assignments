import pymongo
import MongoLog

logging = MongoLog.mongo_logging()

class connection:

    def __init__(self,username : str, password: str, database: str) -> None:
        self.username = username
        self.password = password
        self.database = database
        
    def connect(self):
        """Connoect with MongoDB Client of the given User and return Client Obj."""
        try :
            client = pymongo.MongoClient("mongodb+srv://{user}:{passwd}@abhibhowmik.e258o.mongodb.net/{db}?retryWrites=true&w=majority".format(user = self.username,passwd = self.password, db = self.database))
            logging.info('Connection to MongoDB Client: {user} is Started.'.format(user = self.username))
            return client

        except Exception as exp:
            logging.error(exp)
    
    def disconnect(self, client) -> None:
        """Disconnoect with MongoDB Client of the given User and return None."""
        try:
            client.close()
            logging.info('Connection to MongoDB Client: {user} is Closed.'.format(user = self.username))

        except Exception as exp:
            logging.error(exp)



