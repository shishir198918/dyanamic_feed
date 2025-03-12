from bs4 import BeautifulSoup as BS4
from urllib.request import urlopen,Request
from pprint import pprint
import html



def parse_html_connection_url(url:str)->BS4:
    request=Request(url,headers={"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"})
    return BS4(urlopen(request).read(),"html5lib")

def get_job_link_list(url):
    anchor_list=parse_html_connection_url(url).find_all("a",class_="justify-start leading-loose")
    #return anchor_list
    return ["https://www.ycombinator.com"+a["href"] for a in anchor_list]

def extract_json_job(url):
   pass


pprint(get_job_link_list("https://www.ycombinator.com/jobs"))