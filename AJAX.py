import requests
import json 
from pprint import pprint



def get_request_body(page_no:int,page_hits:int)->dict:
    """return string which having body for post request getting id"""
    body={
        "requests": [
            {
                "indexName": "WaaSPublicCompanyJob_created_at_desc_production",
                "params": f"query=&page={page_no}&filters=&attributesToRetrieve=%5B%22company_id%22%5D&attributesToHighlight=%5B%5D&attributesToSnippet=%5B%5D&hitsPerPage={page_hits}&clickAnalytics=true&distinct=true"
            }
        ]
    }
    return body



def get_ids():
    url="https://45bwzj1sgc-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (3.35.1); Browser&x-algolia-application-id=45BWZJ1SGC&x-algolia-api-key=NWJmYTkxYzQ2NzRjNTA4ZmE5ZmJkODFkOTYyZDlkODM4OGY1MmU4NTE5MDUyZWVmMjI3MzBmZmNjNzcwYjM2OHRhZ0ZpbHRlcnM9JTVCJTVCJTIyam9ic19hcHBsaWNhbnQlMjIlNUQlNUQmYW5hbHl0aWNzVGFncz0lNUIlMjJ3YWFzJTIyJTVEJnVzZXJUb2tlbj1rUTJNUiUyRiUyQnJicnZXZiUyRnNNN0cySzVYYXUlMkZjQVoyZVJvd0hFQVJDd2VQSTQlM0Q="
    r=requests.post(url,data=json.dumps(get_request_body(1,)))
    #print(r.url)
    return r.json()


pprint((get_ids()))