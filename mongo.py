from pymongo import MongoClient

#from AJAX import get_ids,fetch_jobs
#from main import extract_jobs,resource
def get_json_jobs():
    pass

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

database=client["Jobs"]
collection=database["hashjob"]
#database.create_collection("hashjob")
#database.create_collection("remotework")
#print(database)
#collection.insert_one(fetch_jobs(get_ids()))
#collection.insert_many(extract_jobs(resource,2)) 
#print(database.list_collection_names())