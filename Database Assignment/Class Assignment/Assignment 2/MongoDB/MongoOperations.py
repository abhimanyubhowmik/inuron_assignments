import MongoLog
import pandas as pd
import numpy as np

logging = MongoLog.mongo_logging()

class DatabaseOps:
    
    def __init__(self,client) -> None:
        self.client = client

    def SelectDB(self,dbName: str):
        """Select or Create new Database of the given Name."""
        try:
            db = self.client[dbName]
            logging.info('Database :{db} is created.'.format(db = dbName))
            return db

        except Exception as exp:
            logging.error(exp)

    def ViewDB(self):
        """List all Database under the given Client."""
        try:
            db_list = self.client.list_database_names()
            return db_list

        except Exception as exp:
            logging.error(exp)
        

    def DropDB(self,dbName: str):
        """Drop/Delete Database of the given name."""
        try:
            self.client.drop_database(dbName)
            logging.info('Database :{db} is dropped.'.format(db = dbName))
        
        except Exception as exp:
            logging.error(exp)


class collectionOps:

    def __init__(self,database) -> None:
        self.database = database

    def SelectColl(self,collName: str):
        """Select or Create new Collection of the given Name."""
        try:
            coll = self.database[collName]
            logging.info('Collection :{coll} is created.'.format(coll = collName))
            return coll

        except Exception as exp:
            logging.error(exp)

    def DeleteColl(self,collName: str):
        """Drop/Delete Collection of the given Name."""
        try:
            coll = self.database[collName].drop()
            logging.info('Collection :{coll} is dropped.'.format(coll = collName))
            return coll

        except Exception as exp:
            logging.error(exp)


class documentOps:

    def __init__(self,collection) -> None:
        self.collection = collection
    
    def InsertCSV(self, filename: str,separator: str = ','):
        """Insert Data from CSV file."""
        try:
            df = pd.read_csv(filename,sep=separator)
            colName = df.columns
            rows = np.array(df)

            dict_list = []
            for row in rows:
                dict_obj = {}
                for r in range(len(row)):
                    dict_obj[colName[r]] = row[r]
                dict_list.append(dict_obj)

            insert_obj = self.collection.insert_many(dict_list)
            logging.info('Data from CSV: {file} inserted into {coll}'.format(file = filename, coll =self.collection))
            return insert_obj
        
        except Exception as exp:
            logging.error(exp)
        
    def InsertDoc(self, doc):
        """Insert document/documents."""
        logging.info(type(doc))
        if type(doc) == dict:
            try:
                insert_obj = self.collection.insert_one(doc)
                logging.info('One Document inserted into {coll}'.format(coll =self.collection.name))
                return insert_obj
            except Exception as exp:
                logging.error(exp)
        elif type(doc) == list: 
            try:
                insert_obj = self.collection.insert_many(doc)
                logging.info('Document/Documents inserted into {coll}'.format(coll =self.collection.name))
                return insert_obj
            
            except Exception as exp:
                logging.error(exp)
        else:
            raise Exception('Wrong Input Type.(Input type must be list or dict)')
    
    def UpdateDoc(self, searchField: str, searchValue, updateField: str, updateValue):
        """Find document/documents by field value and update given field value.
        For updating many documents give searchValue as dictionary condition."""
        try:
            #Finding Object ID of updated Documents
            search_dict = {searchField:searchValue}
            search_obj = self.collection.find(search_dict)
            data = []
            for i in search_obj:
                data.append(i)
            id_list = []
            for j in data:
                id_list.append(j['_id'])
            #Updating Documents
            update_dict = {'$set':{updateField:updateValue}}
            update_obj = self.collection.update_many(search_dict,update_dict)
            logging.info('Updatetion of document Completed at: {_id}.'.format(_id = id_list))
            return update_obj
        
        except Exception as exp:
            logging.error(exp)

    def DeleteDoc(self, searchField: str, searchValue) -> None:
        """Find document/documents by field value and Delete."""
        try:
            #Finding Object ID to Delete Documents
            search_dict = {searchField:searchValue}
            search_obj = self.collection.find(search_dict)
            data = []
            for i in search_obj:
                data.append(i)
            id_list = []
            for j in data:
                id_list.append(j['_id'])
            #Deteting Documents
            self.collection.delete_many(search_dict)
            logging.info('Deletion of document Completed at: {_id}.'.format(_id = id_list))
        
        except Exception as exp:
            logging.error(exp)


class documentQuery:

    def __init__(self,collection) -> None:
        self.collection = collection

    def FindDoc(self, searchField: str = None, searchValue = None):
        """Find document/documents by field value.
        If field value is not given find all documents of the given collection."""
        if searchField == None or searchValue == None:
            #Finding all Documents
            try:
                search_obj = self.collection.find()
                logging.info('Found all Documents of Collection: {coll}'.format(coll = self.collection.name))
                return search_obj
            
            except Exception as exp:
                logging.error(exp)
        else:
            #Finding specific Documents using field values 
            try:
                #Finding Document and Object ID
                search_dict = {searchField:searchValue}
                search_obj = self.collection.find(search_dict)
                data = []
                for i in search_obj:
                    data.append(i)
                id_list = []
                for j in data:
                    id_list.append(j['_id'])

                logging.info('Found Document/Documents at: {_id}.'.format(_id = id_list))
                return search_obj

            except Exception as exp:
                logging.error(exp)
 