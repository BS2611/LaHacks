from pymongo import MongoClient
import os 
from dotenv import load_dotenv
import mongoengine
class DbManager:
    load_dotenv()
    ___collection_name = None
    __client = MongoClient(os.getenv("DB_String"))
    db = __client[os.getenv("DB_Name")]
    ___collection_name = db["users"]

    def addUser( username,password):
        info = {
            "username" : username,
            "password": password,
            "preferedIngredients": [],
        }
        DbManager.___collection_name.insert_one(info)
    def addUserIngridients(username,ingredients):
        DbManager.___collection_name.update_one({"username": username}, {"$push": {"preferedIngredients": {"$each": ingredients}}})
    
