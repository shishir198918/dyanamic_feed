import requests
import json 
from pprint import pprint



def get_request_body(page_no:int,page_hits:int)->dict:
    """return string which having body for post request getting id"""
    body={
        "requests": [
            {
                "indexName": "WaaSPublicCompanyJob_created_at_desc_production",
                "params": f"query=&page={page_no}&filters=&attributesToRetrieve=%5B%22company_id%22%5D&attributesToHighlight=%5B%5D&attributesToSnippet=%5B%5D&hitsPerPage={page_hits}&distinct=True"
            }
        ]
    }
    return body



def get_ids():
    url="https://45bwzj1sgc-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for JavaScript (3.35.1); Browser&x-algolia-application-id=45BWZJ1SGC&x-algolia-api-key=NWJmYTkxYzQ2NzRjNTA4ZmE5ZmJkODFkOTYyZDlkODM4OGY1MmU4NTE5MDUyZWVmMjI3MzBmZmNjNzcwYjM2OHRhZ0ZpbHRlcnM9JTVCJTVCJTIyam9ic19hcHBsaWNhbnQlMjIlNUQlNUQmYW5hbHl0aWNzVGFncz0lNUIlMjJ3YWFzJTIyJTVEJnVzZXJUb2tlbj1rUTJNUiUyRiUyQnJicnZXZiUyRnNNN0cySzVYYXUlMkZjQVoyZVJvd0hFQVJDd2VQSTQlM0Q="
    r=requests.post(url,data=json.dumps(get_request_body(1,1)))
    #pprint(r.json())
    ids=json.dumps({"ids":[r.json()["results"][0]["hits"][lenght]["company_id"] for lenght in range(1)]})
    pprint(ids)
    return ids
def fetch_jobs(id):
    url="https://www.workatastartup.com/companies/fetch"
    header={"user-agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0",
            "Accept":"application/json",
            "x-csrf-token":"m5JMs2ziBonW1BOObn0kXB3rhtdrmcvdzWt_bTkG6J3FNsppJiONz4wyb_nZVMTZOtE48eG5k8KfD5SCPj7HvA",
            "content-type":"application/json",
            "Cookie":"_bf_session_exists=eyJfcmFpbHMiOnsibWVzc2FnZSI6ImRISjFaUT09IiwiZXhwIjpudWxsLCJwdXIiOiJjb29raWUuX2JmX3Nlc3Npb25fZXhpc3RzIn19--c09bf3da17accf4c53e92f910eef613c6f99527b; XSRF-TOKEN=q4Z2NgSxOgJGsz9VM0SGTVfrhj-3crh1NM2lYfd2wjj1IvDsTnCxRBxVQyKEbWbIcNE4GT1S4GpmqU6O8E7tGQ; _bf_session_key=EHSXVSxcmhRN72buPh4S0rWTAPFt9jjAP2u4SA%2FP0lzp7Pf3xwnybYO%2Bx1wKtcxhCZKLfIOCN7d1ep9O0%2FcTZPp7BP01VKm8zyJjqY2SM8OoF%2ByhLKgHAyHV38wStGgcSmyuziL79mw%2B6BeIm02QZIMK6rW9uVLtNzGF5TsDXpdSiDQfh5J8E%2B3IeQUjAKPM7mZcqe9MLzLa7v9rXszyTdp1795%2FqHnPfUy4JITVeIG7s%2Fjzk%2B2ckzia90i951SpFKYUMys5wX3FcvyG%2FuqDf5SsTawBO%2BY%3D--OC9a4%2FB43CI0cToM--mIqWsTYvUu2OryrhaUHj6g%3D%3D; amp_e48895=F3qb4B7GaRj0AhG_KFARSO.MjY1MTg4MQ==..1imn421bu.1imn4jhae.3.a.d; _ga=GA1.2.865754013.1742368420; _gid=GA1.2.1305355942.1742368420; _sso.key=SxxJkuBAzjSt62x5cCKt8JgyJwbtPy5o; _gat=1"
            }
    jar={"_bf_session_exists":"eyJfcmFpbHMiOnsibWVzc2FnZSI6ImRISjFaUT09IiwiZXhwIjpudWxsLCJwdXIiOiJjb29raWUuX2JmX3Nlc3Npb25fZXhpc3RzIn19--c09bf3da17accf4c53e92f910eef613c6f99527b",
         "_bf_session_key":"vdY2/93PaLPe58vOxzRkd9/TB3qLejrR3frN3SVg+W85JkWbjnfpdAhGMomoF0y3bb4bsmzctldpNuxmgy8iNNY3uqJEk5bjOyIiM/pzzmsH3vwHnsBwl88pVfHNidgVLKbr2LKnTU2cf0Tu3xmkCJ6VUH5W5rx0Y6Sq13ltZ/N6UVg+tE0B7m7xoCPD8ogbQhfMWSAK6yzJ60I2LgcxFIQfv8WAXip6VLIdx3FVDk9YcenFIWdoUtXppTiI2v2pvP/wibaplMV/Cdyx2UpNn6dgszyj21s=--gpaPCHXBQZCn7x8k--hoQt+YA86Xx9DHQMYMxP6Q==",
         "XSRF-TOKEN":"niCGVV4HLeafMFMtq81nIzE2weoq5jUp_6NdY04H6M_AhACPFMamoMXWL1oc5IemFgx_zKDGbTatx7aMST_H7g",
         "_ga":"GA1.2.865754013.1742368420",
         "_gat":"1",
         "_gid":"GA1.2.1305355942.1742368420",
         "_sso.key":"WefJVfUDMph7uhTMrm26sYPWnrk8g9Tr",
         "amp_e48895":"F3qb4B7GaRj0AhG_KFARSO.MjY1MTg4MQ==..1immk0bu7.1immk3tvm.1.2.3"
         }
    
    r=requests.post(url,headers=header,data=id)
    # pprint(r.request.headers)
    # pprint(r.request.body)
    # pprint(r.request.url)
    return r.json()

pprint(fetch_jobs((get_ids())))