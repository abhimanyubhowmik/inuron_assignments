import logging


logging.basicConfig(filename = "mongo_db.log", level = logging.INFO, format = '%(asctime)s %(levelname)s %(message)s')

class mongo_logging:

    def error(self,message):
        logging.error(message)
    
    def info(self,message):
        logging.info(message)