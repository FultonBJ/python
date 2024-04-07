from pymongo.mongo_client import MongoClient
import certifi
import test
from test import AnimalShelter


AnimalShelter

AnimalShelter.connect("mongodb+srv://fultonbj:mongopass@cs340.isa9tad.mongodb.net/?retryWrites=true&w=majority&appName=CS340")





#class DbTools:
 #   def __init__(self, new: list[str]):
  #      self.new = ['Animal_id', 'rec_num', 'age']
        
        
  

    


 
# class A(object):
#    def __init__(self, *args, **kwargs):
#        for k,v in kwargs.items():
#            setattr(self, k, v)   
    
    
############## find all unique keys in a collection #####################
#   
#   mr = db.runCommand({
#     "mapreduce" : "my_collection",
#     "map" : function() {
#       for (var key in this) { emit(key, null); }
#     },
#     "reduce" : function(key, stuff) { return null; }, 
#     "out": "my_collection" + "_keys"
#   })
#       
#       
#   db[mr.result].distinct("_id")
#   ["foo", "bar", "baz", "_id", ...]
    
    
    
    
    
    
    
    
    
    
    
#    docs={'animal_id': input('enter animal ID'), 'rec_num': input('enter rec number'), 'age_upon_outcome': input('enter age upon outcome')}
#    def __init__(self, animal_id, rec_num, age_upon_outcome):
#        self.animal_id=animal_id
#        self.rec_num=rec_num
#        self.age_upon_outcome=age_upon_outcome
#        
#        print(DbTools.docs)
#        
#
#        
#    def insertOne(self, *kwargs):
#        for k, v in kwargs:
#            DbTools.docs.update[k,v]
            



 
#    def __repr__(key, value):
#        return "Document('{}', '{}', '{}')".format(self.animal_id, self.rec_num)
#    def __str__(self):
#        return '{} - {} - {}'.format(self.animal_id, self.rec_num, self.breed())
#    
#
#    def __update__(self, k, v):
#        pass
#    
#    def __new__(cls: type[object]):
#        pass
#        
#    def __dir__(self) -> Iterable[str]:
#        pass
#        
#    def __getattribute__(self, __name: str) -> Any:
#        pass
#    def __new__(cls: type[Self]) -> Self:
#        pass
#    def __str__(self):
#        return '{}'.format(self.key)
#