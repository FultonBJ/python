from pymongo.mongo_client import MongoClient
import certifi
from bson.objectid import ObjectId
import pprint

class AnimalShelter(object):
    def __init__(self, new_doc, connect):
        self.new_doc = ['Animal_id', 'rec_num', 'age'] 
        self.connect = "mongodb+srv://fultonbj:mongopass@cs340.isa9tad.mongodb.net/?retryWrites=true&w=majority&appName=CS340"