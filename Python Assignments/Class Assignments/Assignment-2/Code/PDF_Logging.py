import logging


logging.basicConfig(filename = "pdf_merger_app.log", level = logging.INFO, format = '%(asctime)s %(levelname)s %(message)s')

class pdf_logging:

    def error(self,message):
        logging.error(message)
    
    def info(self,message):
        logging.info(message)