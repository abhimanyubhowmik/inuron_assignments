import logging
logging.basicConfig(filename = "list.log", level = logging.INFO, format = '%(asctime)s %(levelname)s %(message)s')

class list_parser:
    
    def __init__(self,list) -> None:
        self.list = list
    
    def raise_exception(self):
        if type(self.list) == list:
            return self.list
        else:
            logging.exception(self.list,'Input type is not List object.')
    
    def append(self,new_element) -> list:
        '''Append object to the end of the list.'''
        old_list = self.raise_exception()
        new_list = old_list + [new_element]
        self.list = new_list
        return new_list
    
    def clear(self) -> list:
        self.raise_exception()
        self.list = []
        return self.list

    def copy(self) -> list:
        '''Return a shallow copy of the list.'''
        List = self.raise_exception() 
        return List
    
    def count(self,element) -> int:
        '''Return number of occurrences of value.'''
        List = self.raise_exception()
        count = 0
        for i in List:
            if i == element:
                count += 1
        return count

    def extend(self,iterable) -> list:
        '''Extend list by appending elements from the iterable.'''
        try :
            iter(iterable)
            old_list = self.raise_exception()
            for i in iterable:
                old_list += [i]
        except:
            logging.exception(iterable,type(iterable) + 'is not iterable')

    def index(self,value) -> int:
        '''Return first index of value.
        Raises ValueError if the value is not present.'''
        try :
            List = self.raise_exception()
            for i in range(len(List)):
                if List[i] == value:
                    return i
        except:
            logging.exception(str(value) + 'is not in the List.')
        
    def insert(self,index,value) -> list:
        '''Insert object before index.''' 
        old_list = self.raise_exception()
        if index <= len(old_list):
           first_list = old_list[0:index]
           last_list = old_list[index,len(old_list)]
           final_list = first_list + [value] + last_list
           return final_list
        else:
            logging.exception('Index out of bound')

    def pop(self, *args):
        '''Remove and return item at index (default last).
        Raises IndexError if list is empty or index is out of range.'''
        if len(args) == 0:
            old_list = self.raise_exception()
            if len(old_list) != 0: 
                new_list = old_list[0:len(old_list) - 1]
                self.list = new_list
                return old_list[len(old_list) - 1]
            else:
                logging.exception('List is empty')
        elif len(args) == 1:
            old_list = self.raise_exception()
            if len(old_list) != 0: 
                if args <= len(old_list) - 1:
                    new_list = old_list[0:args[0]] + old_list[args[0]+1:len(old_list)]
                    self.list = new_list
                    return old_list[args[0]]
                else:
                    logging.exception('Index out of bound.')
            else:
                logging.exception('List is empty')

        else:
            logging.exception('pop expected at most 1 argument, got {i}'.format(i = len(args)))

    def remove(self, value):
        '''Remove first occurrence of value.
        Raises ValueError if the value is not present.'''
        old_list = self.raise_exception()
        if value in old_list:
            index = self.index(value)
            deleted_element =self.pop(index)
            return self.list
        else:
            logging.exception(str(value)+'not in the list')

    def reverse(self):
        old_list = self.raise_exception()
        new_list = old_list[::-1]
        self.list = new_list
        return self.list

    def sort(self, reverse: bool = False) -> None:
        '''Sort the list in ascending order and return None.
        The reverse flag can be set to sort in descending order.'''
        List = self.raise_exception()
        if reverse == False:
            for i in range(len(List)):
                min_index = i
                for j in range(min_index+1,len(List)):
                    if List[min_index] > List[j]:
                        min_index = j
                        List[min_index], List[i] = List[i], List[min_index]
            self.list = List
        elif reverse == True:
            for i in range(len(List)):
                max_index = i
                for j in range(max_index+1,len(List)):
                    if List[max_index] < List[j]:
                        max_index = j
                        List[max_index], List[i] = List[i], List[max_index]
            self.list = List
        else:
            logging.exception('Invalid Input')

    def display(self) -> list:
        return self.list

