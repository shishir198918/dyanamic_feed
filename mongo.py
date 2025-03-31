from pymongo import MongoClient

from datetime import datetime

from AJAX import extracted_all_jobs,get_total_page_number

pages=get_total_page_number(1)  # do not iterate more than this value 
compare_date=datetime(2025,3,22,0,0)
uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

database=client["Jobs"]

def insert_into_ycombinator():
    table=database["ycombinator"]
    table.create_index([("description.description.id",1),("description.description.company_id",1)],unique=True )
    jobs=extracted_all_jobs(compare_date)
    for _ in range(100):
        try:    
            table.insert_many(next(jobs))
        except Exception as e:
            print(e)
            pass       
    return table.inserted_ids

print(insert_into_ycombinator())