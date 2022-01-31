import logging
logging.basicConfig(filename = "dict.log", level = logging.INFO, format = '%(asctime)s %(levelname)s %(message)s')


class dict_parser:
    
    def __init__(self,d) -> None:
        self.d = d

    def check_dict(self):
        if type(self.d) != dict:
            logging.exception(self.check_dict,'Input type is not a dictionary') 
        else:
            return self.d
        
    def get_keys(self):
        '''D.get_keys() -> a set-like object providing a view on D's keys'''
        d = self.check_dict()
        return d.keys()

    def get_values(self):
        '''D.get_values() -> an object providing a view on D's values'''
        d = self.check_dict()
        return d.values()

    def key_parser(self):
        '''Return value by key'''
        d = self.check_dict()
        key = input('Enter the key')
        if key in d:
            return d[key]
        else:
            logging.exception(d,'Key Error')

    def insert(self,key,value):
        '''Insert element by key and value'''
        d = self.check_dict()
        d[key] = value
        self.d = d
        return self.d

    def user_input(self):
        '''Enter input as dictionary format.'''
        new_dict = input('Enter a dictionary')
        if type(eval(new_dict)) == dict:
            self.d = new_dict
            return self.d
        else:
            logging.exception(self.d,'Input not a dictionary') 

    def copy(self) -> dict:
        '''D.copy() -> a shallow copy of D'''
        d = self.check_dict()
        copy_dict = d
        return copy_dict
    
    def clear(self) -> dict:
        d = self.check_dict()
        self.d = {}
        return self.d
    
    def get_items(self) -> list:
        '''D.get_items() -> a set-like object providing a view on D's items'''
        d = self.check_dict()
        l = []
        for key in d:
            value = d[key]
            tup = (key,value)
            l.append(tup)
        return l
    
    def pop(self,key):
        '''Pop elements by key and return the value'''
        d = self.check_dict()
        new_dict = {}
        if key in d:
            for i in d:
                if i != key:
                    new_dict[i] = d[i]
            self.d = new_dict
            return d[key]
        else:
            logging.exception('Key Error')

    def popitem(self,key):
        '''Pop elements by key and return the key and value in tuple'''
        d = self.check_dict()
        new_dict = {}
        if key in d:
            for i in d:
                if i != key:
                    new_dict[i] = d[i]
            self.d = new_dict
            return (key,d[key])
        else:
            logging.exception('Key Error')

    def display(self):
        d = self.check_dict()
        return d

    