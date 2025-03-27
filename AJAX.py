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
    try:

        url="https://45bwzj1sgc-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (3.35.1); Browser&x-algolia-application-id=45BWZJ1SGC&x-algolia-api-key=NWJmYTkxYzQ2NzRjNTA4ZmE5ZmJkODFkOTYyZDlkODM4OGY1MmU4NTE5MDUyZWVmMjI3MzBmZmNjNzcwYjM2OHRhZ0ZpbHRlcnM9JTVCJTVCJTIyam9ic19hcHBsaWNhbnQlMjIlNUQlNUQmYW5hbHl0aWNzVGFncz0lNUIlMjJ3YWFzJTIyJTVEJnVzZXJUb2tlbj1rUTJNUiUyRiUyQnJicnZXZiUyRnNNN0cySzVYYXUlMkZjQVoyZVJvd0hFQVJDd2VQSTQlM0Q="
        
        r=requests.post(url,data=json.dumps(get_request_body(page_number)))
        
        ids=json.dumps({"ids":\
                [r.json()["results"][0]["hits"][lenght]["company_id"]\
                for lenght in range(1)]})
        print(page_number)    
        return ids
    except Exception as e:
        print(f"Error: {e}")


def get_total_page_number(page_number):
    url="https://45bwzj1sgc-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (3.35.1); Browser&x-algolia-application-id=45BWZJ1SGC&x-algolia-api-key=NWJmYTkxYzQ2NzRjNTA4ZmE5ZmJkODFkOTYyZDlkODM4OGY1MmU4NTE5MDUyZWVmMjI3MzBmZmNjNzcwYjM2OHRhZ0ZpbHRlcnM9JTVCJTVCJTIyam9ic19hcHBsaWNhbnQlMjIlNUQlNUQmYW5hbHl0aWNzVGFncz0lNUIlMjJ3YWFzJTIyJTVEJnVzZXJUb2tlbj1rUTJNUiUyRiUyQnJicnZXZiUyRnNNN0cySzVYYXUlMkZjQVoyZVJvd0hFQVJDd2VQSTQlM0Q="
    r=requests.post(url,data=json.dumps(get_request_body(page_number)))
    return r.json()["results"][0]["nbPages"]-1

def get_companies_id():
    total_pages=get_total_page_number(1)
    print(total_pages)
    return [get_company_id(serial)\
            for serial in range(1,total_pages)]

def fetch_company_jobs(ids):
    url="https://www.workatastartup.com/companies/fetch"
    header={"user-agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0",
            "Accept":"application/json",
            "x-csrf-token":"uaOKMiacUAaNYYlDj5BWOVo8JdZPG0gfUrKyAKaBmZmBcqGo0boLuJSxSqJ-kRoYjFsOPDUhbYE1Pi9f1QHUuA",
            "content-type":"application/json",
            "Cookie":'amp_e48895=F3qb4B7GaRj0AhG_KFARSO.MjY1MTg4MQ==..1imsc7msp.1imsc87i9.3.d.g; _ga=GA1.2.865754013.1742368420; _sso.key=SxxJkuBAzjSt62x5cCKt8JgyJwbtPy5o; _bf_session_exists=eyJfcmFpbHMiOnsibWVzc2FnZSI6ImRISjFaUT09IiwiZXhwIjpudWxsLCJwdXIiOiJjb29raWUuX2JmX3Nlc3Npb25fZXhpc3RzIn19--c09bf3da17accf4c53e92f910eef613c6f99527b; XSRF-TOKEN=filor4zhbOnA908AuwLaDKA88H629sziRyjYBqFW76lG-EM1e8c3V9knjOFKA5YtdlvblMzM6XwgpEVZ0taiiA; _bf_session_key=O%2F3KccP%2F4ZeYX%2FOOrbrdOrKrAKexqG0qzkcBTt68BCWM8Lqjq%2Bm2W6CcFF%2FFR1vQSWkolCm3%2Bc4TpQkqJUUX1IaMlhfmyXvXL8AkTwzdKhGV1nXH0ECtlnZHggijWGEiw9BYqz2L7UGpuz1l2mJo5%2FzgpiOSUxdu%2F9T0bc%2B2F429iiQyrZgwg1Sse%2FKInp4e3Z9RWA%2BhcVVFtEudyd5cab%2B7SmzomC%2FSOL4KzCy7YJ107xYoplRy6v5aneGNdy3fNnuKdIf9D6nPUCf4Os35pZqUKHgi67k%3D--0kEUfAMEy9ScNVwo--FMD9Oq914GNmf5P8%2FRzQFw%3D%3D'
            }    
    r=requests.post(url,headers=header,data=ids, stream=True)
    #pprint(r.raw.read())
    #pprint("="*90)
    #pprint(r.request.__dict__)
    return r.json()

def get_job_heading(response,serial):
    return f"{response["companies"][0]["name"]}:{response["companies"][0]["jobs"][serial]["title"]}"

def get_jobs_description(response,serial):
    return f"{response["companies"][0]["jobs"][serial]}"

def Is_updated(response,compare_date,serial):
    return (datetime.strptime(response["companies"][0]["jobs"][serial]["pretty_updated_at"],"%m/%d/%Y")>=compare_date)

def extract_updated_company_jobs(comapny_id,compare_date):
    response=fetch_company_jobs(comapny_id)
    jobs=len(response["companies"][0]["jobs"])
    return [{"title":get_job_heading(response,serial),"description":get_jobs_description(response,serial)} \
            for serial in range(jobs)\
            if Is_updated(response,compare_date,serial)]

def extracted_all_jobs(id_list):
     pass


#pprint(job_update_date(fetch_company_jobs(get_companies_ids())))
#pprint((datetime.strptime((son["companies"][0]["jobs"][0]["pretty_updated_at"]),"%m/%d/%Y")))
#print(datetime(2025, 3, 24, 0, 0)>datetime(2025, 3, 20, 0, 0))
#print([Is_updated(date) for date in job_update_date(fetch_company_jobs(get_companies_ids(1,1)))])

ids=json.dumps({"ids": [29042]})
pprint(extract_updated_company_jobs(ids,datetime(2025,3,23,0,0)))