from pymongo import MongoClient

#from AJAX import get_ids,fetch_jobs
#from main import extract_jobs,resource
def get_json_jobs():
    pass

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

database=client["Jobs"]

def insert_into_ycombinator():
    table=database["ycombinator"]
    
    pass