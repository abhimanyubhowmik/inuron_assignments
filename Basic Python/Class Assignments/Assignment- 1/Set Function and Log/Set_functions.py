import logging
logging.basicConfig(filename = "set.log", level = logging.INFO, format = '%(asctime)s %(levelname)s %(message)s')

class set_parser:
    def __init__(self,set) -> None:
        self.set = set
    
    def raise_exception(self):
        if type(self.set) == set:
            return self.set
        else:
            logging.exception(self.set,'Input type is not Set object.')
    
    def add(self,new_element) -> set:
        '''Add an element to a set.
        This has no effect if the element is already present.'''
        old_set = self.raise_exception()
        new_set = old_set.add(new_element)
        self.set = new_set
        return self.set

    def clear(self) -> set:
        self.raise_exception()
        self.set = []
        return self.set

    def copy(self) -> set:
        '''Return a shallow copy of the list.'''
        Set = self.raise_exception() 
        return Set

    def pop(self, value):
        '''Remove and return item.
        Raises Error if set is empty or item is not present.'''
        old_set = self.raise_exception()
        if len(old_set) != 0:
            if value in self.set:
                new_set = {}
                for i in self.set:
                    if i != value:
                        new_set.add(i)
                self.set = new_set
                return value
            else:
                logging.exception('Value Error')
        else:
            logging.exception('Set is empty')
                    

    def remove(self, value):
        '''Remove and item.
        Raises Error if set is empty or item is not present.'''
        old_set = self.raise_exception()
        if len(old_set) != 0:
            if value in self.set:
                new_set = {}
                for i in self.set:
                    if i != value:
                        new_set.add(i)
                self.set = new_set
            else:
                logging.exception('Value Error')
        else:
            logging.exception('Set is empty')
    
    def union(self,new_set) -> set:
        old_set = self.raise_exception()
        if type(new_set) == set:
            for i in new_set:
                if i not in old_set:
                    old_set.add(i)
            return old_set
        else:
            logging.exception('Input is not set')

    def intersection(self,new_set) -> set:
        old_set = self.raise_exception()
        output_set = {}
        if type(new_set) == set:
            for i in new_set:
                if i in old_set:
                    output_set.add(i)
            return output_set
        else:
            logging.exception('Input is not set')
    
    def difference(self,new_set) -> set:
        old_set = self.raise_exception()
        diff_set = {}
        if type(new_set) == set:
            for i in new_set:
                if i not in old_set:
                    diff_set.add(i)
        else:
            logging.exception('Input is not set')

    def symmetric_difference(self,new_set) -> set:
        output_set = {}
        if type(new_set) == set:
            union = self.union(new_set)
            intersection = self.intersection(new_set)
            for i in intersection:
                if i not in union:
                    output_set.add(i)
        else:
            logging.exception('Input is not set')
                
    
    def display(self) -> set:
        return self.set

    
