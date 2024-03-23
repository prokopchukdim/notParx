from pymongo import MongoClient
from django.conf import settings
from bson.objectid import ObjectId
MONGO_URI = settings.MONGO_URI
DATABASE_NAME = "NotParxDB"

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
prescription_collection = db["api_prescription"]
user_collection = db["api_user"]
presriber_collection = db["api_prescriber"]

def get_prescription_by_prescription_id(prescription_id):
    """Retrieve a prescription from MongoDB by its prescriptionID."""
    try:
        return prescription_collection.find_one({'prescriptionID': prescription_id})
    except Exception as e:
        print(e)
        return None
    

def user_details(user_id):
    """Retrieve a user from MongoDB by its _id."""
    try:
        return user_collection.find_one({'_id': ObjectId(user_id)})
    except Exception as e:
        print(e)
        return None
    
def presriber_details(presriber_id):
    """Retrieve a presriber from MongoDB by its _id."""
    try:
        return presriber_collection.find_one({'_id': ObjectId(presriber_id)})
    except Exception as e:
        print(e)
        return None