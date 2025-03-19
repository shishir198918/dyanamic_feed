from bs4 import BeautifulSoup as BS4
from urllib.request import urlopen,Request
from pprint import pprint
from itertools import chain
import json 


# use here iter tha list and yeild than return 


def parse_html_from_connection_url(url:str)->BS4:
    request=Request(url,\
            headers=\
            {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"})
    return BS4(urlopen(request).read(),"html5lib") # cna use parse_only 

def get_companies_link_list(url):
    anchor_list=parse_html_from_connection_url(url).\
        find_all("a",class_="justify-start leading-loose")
    return ["https://www.ycombinator.com"+a["href"] for a in anchor_list]

def get_jobs_link_list(companies_list):
    anchor_list=list(chain.from_iterable([parse_html_from_connection_url(company).\
    find("div",class_="flex w-full flex-col justify-between gap-2")\
    .find_all("a",attrs={"target":"_target"}) for company in companies_list]))
    #return anchor_list 
    return ["https://www.ycombinator.com"+a["href"] for a in anchor_list]

def extract_json_job(url):
   return json.loads(parse_html_from_connection_url(url).\
          find("script",attrs={"type":"application/ld+json"}).string)

#pprint(parse_html_from_connection_url(get_companies_link_list("https://www.ycombinator.com/jobs")[0]))

pprint(extract_json_job("https://www.ycombinator.com/companies/fieldguide/jobs/wlHhxce-senior-platform-engineer-infrastructure-security"))
#pprint(get_jobs_link_list(get_companies_link_list("https://www.ycombinator.com/jobs")))