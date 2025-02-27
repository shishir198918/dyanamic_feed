from urllib.request import urlopen,Request
from bs4 import BeautifulSoup as BS4
from pprint import pprint
from datetime import datetime
import dates
import db


resource=[{"url":"https://remoteok.com/rss","head_tag":"","update_tag":""},{"url":"https://weworkremotely.com/remote-jobs.rss","head_tag":"","update_tag":""},{"url":"https://hasjob.co/feed","head_tag":"entry","update_tag":"published"}]

#resource=["https://remoteok.com/rss"]

def connection(url):
    request=Request(url,headers={"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"})
    #return urlopen(request).read()
    #a = BS4(urlopen(request).read(),"xml")
    return BS4(urlopen(request).read(),"xml")



def multiple_request(url_list):
    for url in url_list:
        print(connection(url))



def extract_job_listings (parsed_xml):
    entries=parsed_xml.entry.next_siblings
    return [extract_job_listing(entry) for entry in entries  if entry.name] 


def extract_job_listing(entry):
    job_listing=[]
    for tag in entry.children:
        if tag.name:
            if tag.name=="content":
                job_listing.append(parse_html_tag(tag))
            else:
                job_listing.append(tag.text)
#    print(job_listing)
    return job_listing             


def parse_html_tag(tag):
    return BS4(tag.text,"html.parser").text.strip().replace("\xa0","")



def Isupdated(head_tag,tag_name): # check whether content is new or not 
    for tag in head_tag.children:
        if tag.name:
            
            for tag1 in tag.next_siblings:
                
                if tag1.name==tag_name:
                    return dates.comparing_dates(tag1.text)


#entry=connection(resource[2]["url"]).entry
#print(Isupdated(entry,"published"))                                
                    
