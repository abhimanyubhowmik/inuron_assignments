import logging


logging.basicConfig(filename = "database.log", level = logging.INFO, format = '%(asctime)s %(levelname)s %(message)s')

class db_logging:

    def error(self,message):
        logging.error(message)
    
    def info(self,message):
        logging.info(message)