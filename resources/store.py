from flask_restful import Resource,reqparse
from models.store import StoreModel

class Store(Resource):      
    def get(self,name):        
        name = StoreModel.find_by_name(name)
        if name:
            return(name.json(),200)           
        return({"message":"Store not found"},404)    

    def post(self,name):
        if StoreModel.find_by_name(name):
            return({"message":"Store with name {} already exists.".format(name)},400)                
        store = StoreModel(name)        
        try:         
            store.save_to_db()       
        except:
            return({"message":"An error occured while creating the store"},500)
        return(store.json(),201)

    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return({"message":"Store Deleted"})

class StoreList(Resource):
    def get(self):
        return({"stores":list(map(lambda x:x.json(),StoreModel.get_stores_from_db()))},200)        