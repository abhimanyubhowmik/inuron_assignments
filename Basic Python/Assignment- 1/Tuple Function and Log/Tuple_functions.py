import logging
logging.basicConfig(filename = "tuple.log", level = logging.INFO, format = '%(asctime)s %(levelname)s %(message)s')

class tuple_parser():
    
    def __init__(self,tup) -> None:
        self.tup = tup

    def check_tuple(self):
        if type(self.tup) == tuple:
            return self.tup
        else:
            logging.exception(self.tup,'Input type is not a tuple.')
    
    def count(self,element) -> int:
        '''Return number of occurrences of value.'''
        tup = self.check_tuple()
        count = 0
        for i in tup:
            if i == element:
                count += 1
        return count
    
    def index(self,value) -> int:
        '''Return first index of value.
        Raises ValueError if the value is not present.'''
        try :
            tup = self.check_tuple()
            for i in range(len(tup)):
                if tup[i] == value:
                    return i
        except:
            logging.exception(str(value) + 'is not in the tuple.')

