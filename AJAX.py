import requests
import json 
from datetime import datetime
from pprint import pprint


def get_request_body(page_no:int)->dict:
    """return string which having body for post request getting id"""
    page_hits=1
    body={
        "requests": [
            {
                "indexName": "WaaSPublicCompanyJob_created_at_desc_production",
                "params": f"query=&page={page_no}&filters=&attributesToRetrieve=%5B%22company_id%22%5D&attributesToHighlight=%5B%5D&attributesToSnippet=%5B%5D&hitsPerPage={page_hits}&distinct=True"
            }
        ]
    }
    return body



def get_company_id(page_number=1):
    url="https://45bwzj1sgc-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (3.35.1); Browser&x-algolia-application-id=45BWZJ1SGC&x-algolia-api-key=NWJmYTkxYzQ2NzRjNTA4ZmE5ZmJkODFkOTYyZDlkODM4OGY1MmU4NTE5MDUyZWVmMjI3MzBmZmNjNzcwYjM2OHRhZ0ZpbHRlcnM9JTVCJTVCJTIyam9ic19hcHBsaWNhbnQlMjIlNUQlNUQmYW5hbHl0aWNzVGFncz0lNUIlMjJ3YWFzJTIyJTVEJnVzZXJUb2tlbj1rUTJNUiUyRiUyQnJicnZXZiUyRnNNN0cySzVYYXUlMkZjQVoyZVJvd0hFQVJDd2VQSTQlM0Q="
    
    r=requests.post(url,data=json.dumps(get_request_body(page_number)))
    
    ids=json.dumps({"ids":\
            [r.json()["results"][0]["hits"][lenght]["company_id"]\
            for lenght in range(1)]})    
    return ids


def get_total_page_number(page_number):
    url="https://45bwzj1sgc-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (3.35.1); Browser&x-algolia-application-id=45BWZJ1SGC&x-algolia-api-key=NWJmYTkxYzQ2NzRjNTA4ZmE5ZmJkODFkOTYyZDlkODM4OGY1MmU4NTE5MDUyZWVmMjI3MzBmZmNjNzcwYjM2OHRhZ0ZpbHRlcnM9JTVCJTVCJTIyam9ic19hcHBsaWNhbnQlMjIlNUQlNUQmYW5hbHl0aWNzVGFncz0lNUIlMjJ3YWFzJTIyJTVEJnVzZXJUb2tlbj1rUTJNUiUyRiUyQnJicnZXZiUyRnNNN0cySzVYYXUlMkZjQVoyZVJvd0hFQVJDd2VQSTQlM0Q="
    r=requests.post(url,data=json.dumps(get_request_body(page_number)))
    return r.json()["results"][0]["nbPages"]-1

def get_companies_id():
    total_pages=get_total_page_number(1)
    print(total_pages)
    for serial in range(1,total_pages):
        print(serial)
        yield get_company_id(serial)

def fetch_company_jobs(id):
    url="https://www.workatastartup.com/companies/fetch"
    header={"user-agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0",
            "Accept":"application/json",
            "x-csrf-token":"m5JMs2ziBonW1BOObn0kXB3rhtdrmcvdzWt_bTkG6J3FNsppJiONz4wyb_nZVMTZOtE48eG5k8KfD5SCPj7HvA",
            "content-type":"application/json",
            "Cookie":"_bf_session_exists=eyJfcmFpbHMiOnsibWVzc2FnZSI6ImRISjFaUT09IiwiZXhwIjpudWxsLCJwdXIiOiJjb29raWUuX2JmX3Nlc3Npb25fZXhpc3RzIn19--c09bf3da17accf4c53e92f910eef613c6f99527b; XSRF-TOKEN=q4Z2NgSxOgJGsz9VM0SGTVfrhj-3crh1NM2lYfd2wjj1IvDsTnCxRBxVQyKEbWbIcNE4GT1S4GpmqU6O8E7tGQ; _bf_session_key=EHSXVSxcmhRN72buPh4S0rWTAPFt9jjAP2u4SA%2FP0lzp7Pf3xwnybYO%2Bx1wKtcxhCZKLfIOCN7d1ep9O0%2FcTZPp7BP01VKm8zyJjqY2SM8OoF%2ByhLKgHAyHV38wStGgcSmyuziL79mw%2B6BeIm02QZIMK6rW9uVLtNzGF5TsDXpdSiDQfh5J8E%2B3IeQUjAKPM7mZcqe9MLzLa7v9rXszyTdp1795%2FqHnPfUy4JITVeIG7s%2Fjzk%2B2ckzia90i951SpFKYUMys5wX3FcvyG%2FuqDf5SsTawBO%2BY%3D--OC9a4%2FB43CI0cToM--mIqWsTYvUu2OryrhaUHj6g%3D%3D; amp_e48895=F3qb4B7GaRj0AhG_KFARSO.MjY1MTg4MQ==..1imn421bu.1imn4jhae.3.a.d; _ga=GA1.2.865754013.1742368420; _gid=GA1.2.1305355942.1742368420; _sso.key=SxxJkuBAzjSt62x5cCKt8JgyJwbtPy5o; _gat=1"
            }    
    r=requests.post(url,headers=header,data=id)
    return r.json()

def job_update_date(json_response):
    no_of_jobs=len(json_response["companies"][0]["jobs"])
    return [datetime.strptime(json_response["companies"][0]["jobs"][serial]["pretty_updated_at"],"%m/%d/%Y")\
    for serial in range(no_of_jobs)]



def Is_updated(posted_date):
    return (datetime(2025, 3, 25, 0, 0)<=posted_date)


def extract_jobs():
    pass

#pprint(job_update_date(fetch_company_jobs(get_companies_ids())))
#pprint((datetime.strptime((son["companies"][0]["jobs"][0]["pretty_updated_at"]),"%m/%d/%Y")))
#print(datetime(2025, 3, 24, 0, 0)>datetime(2025, 3, 20, 0, 0))
#print([Is_updated(date) for date in job_update_date(fetch_company_jobs(get_companies_ids(1,1)))])
while True:
    try:
        ids=next(get_companies_id())
        print(ids)
    except StopIteration:
        print("done")
        break    