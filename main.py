from urllib.request import urlopen,Request
from bs4 import BeautifulSoup as BS4
from pprint import pprint
import dates
import db



resource=[{"url":"https://remoteok.com/rss","head_tag":"item","update_tag":"pubDate"}
        ,{"url":"https://weworkremotely.com/remote-jobs.rss","head_tag":"item","update_tag":"pubDate"}
        ,{"url":"https://hasjob.co/feed","head_tag":"entry","update_tag":"published"}]


def connection_url(url:str)->BS4:
    request=Request(url,headers={"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"})
    return BS4(urlopen(request).read(),"xml")

 
def extract_heading(tag:BS4)->str:
    match tag.name:
        case "content"|"description":
            return "content"
        case "title":
            return "title"
        case "published"|"pubDate":
            return "published"
        case "link":
            return "link"
        case "location":
            return "location"
        
def extract_body(tag:BS4)->str:
    match tag.name:
        case "content"|"description":
            return parse_html_tag(tag)
        case _:
            return tag.text
        


def extract_job_listing(entry):    
    job_listing={extract_heading(tag):extract_body(tag)\
                for tag in entry.children if tag.name}
    return job_listing             


def parse_html_tag(tag:BS4)->str:
    return BS4(tag.text,"html.parser").text.strip().replace("\xa0","")



def Is_Updated(update_tag:BS4,latest_time:str)->bool:
    
    return dates.comparing_dates(update_tag.text,latest_time)




def head_tag_and_upadate_tag_name(resource:dict,index:int)->tuple: # used for Isupdated function
    soup=connection_url(resource[index]["url"])
    head_tag=resource[index]["head_tag"]
    head_object=soup.find(head_tag)
    update_tag_name=resource[index]["update_tag"]
    return(head_object,update_tag_name)


                             
def extract_jobs(resource:list,index:int)->dict:
    head_tag,update_tag_name=head_tag_and_upadate_tag_name(resource,index)
    latest_time=db.latest_time()
    entry_tags=[entry_tag \
                for entry_tag in head_tag.next_siblings \
                if entry_tag.name \
                and \
                Is_Updated(entry_tag.find(update_tag_name),latest_time)]
    jobs=[extract_job_listing(entry_tag) for entry_tag in entry_tags   ]
    return jobs


pprint(type(extract_jobs(resource,2)[0]))
             
