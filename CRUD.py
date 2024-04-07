from pymongo.mongo_client import MongoClient
import certifi
from bson.objectid import ObjectId
import pprint

class DbTools:
    def __init__(self, new_doc: dict) -> None:
        self.newDocument = new_doc
     
    #TODO replace hard coded string with user input() 
    MONGODB_URI = "mongodb+srv://fultonbj:mongopass@cs340.isa9tad.mongodb.net/?retryWrites=true&w=majority&appName=CS340"

    client = MongoClient(MONGODB_URI, tlsCAFile=certifi.where())
    db = client.AAC

    for db_name in client.list_database_names():
        print(db_name)
            
       
    def insertOne(k,v):
        new_doc = {}
        new_doc[k]=v
        while input('Would you like to enter values for a new document? \nany key to continue type \'exit\' to insert your doc') != 'exit':
            key = input('enter a key')
            val = input('enter a value')
            new_doc[key]=val
        
            
        animals_collection = DbTools.db.animals
        result = animals_collection.insert_one(new_doc)
    
        document_id = result.inserted_id
        print(f"_id of inserted document: {document_id}")
        if document_id != None:
            return True
        else:
            return False

    def findOne(k,v):
        
        animals_collection = DbTools.db.animals
        
        document_to_find ={k:v}
        cursor = animals_collection.find(document_to_find)
        
        num_docs = 0
        for document in cursor:
            num_docs += 1
            pprint.pprint(document)
            print()

        if num_docs == 0:
            return True
        else:
            return False
        
        
        
#    
#    def create(key, value):
#    
#        new_doc = {key, value}
#        
#        DbTools.animals_collection.insert_one(new_doc)
#    
#        document_id = new_doc.inserted_id
#        
#        print(f"_id of inserted document: {document_id}")
#        print(new_doc)
#
#        
#
#
#
#    def read(key, value):
#        
#        animals_collection = DbTools.db.animals
#        
#        document_to_find = {'_id': ObjectId(document_id)}
#        result = animals_collection.find_one(document_id)
#        print("Found :", document_id)
#        print(result)
#  
#  
#
#    def Delete():
#        print('Input the document id of the document to be deleted')
#        delete_doc = input()
#        document_to_delete = {'_id': ObjectId(delete_doc)}
#      
#        result = DbTools.animals_collection.delete_one(document_to_delete)
#
#        print("Now Deleting :", delete_doc)
#        print("Documents deleted: " + str(result.deleted_count))
#
#
#def Read():
#    pass
#
#def Update():
#    pass


    
    
    
   

#Develop a CRUD class that, when instantiated, provides the following functionality:
# A method that inserts a document into a specified MongoDB database and collection
# Input argument to function will be a set of key/value pairs in the data type acceptable to the MongoDB driver insert API call
# Return “True” if successful insert, else “False”

# A method that queries for documents from a specified MongoDB database and collection
# Input arguments to function should be the key/value lookup pair to use with the MongoDB driver find API call
# Return result in a list if the command is successful, else an empty list..
    
#enable create and read functionality for the database
# Important: Be sure to use find() instead of find_one() 
#

# Complete this create method to implement the C in CRUD.
    # def create(self, data):
    #     if data is not None:
	# 	self.database.animals.insert_one(data)  # data should be dictionary            
    #     else:
    #         raise Exception("Nothing to save, because data parameter is empty")
#