from pymongo.mongo_client import MongoClient
import certifi
from bson.objectid import ObjectId
import pprint


class AnimalShelter(object):
    def __init__(self, new_doc):
        self.new_doc = ['Animal_id', 'rec_num', 'age'] 
        
    def connect(connection_string):
        MONGODB_URI = connection_string
        
        client = MongoClient(MONGODB_URI, tlsCAFile=certifi.where())
        db = client.AAC
        
        for db_name in client.list_database_names():
            print(db_name)
    
x = AnimalShelter(new_doc=[])
values = [input('Enter a value for animal_id'), input('Enter a value for rec_num' ), input('Enter a value for age')]
res = {}
for key in x.new_doc:
    for value in values:
        res[key] = value
        values.remove(value)
        break
    
    


print(res)