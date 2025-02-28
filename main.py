from urllib.request import urlopen,Request
from bs4 import BeautifulSoup as BS4
from pprint import pprint
import dates



resource=[{"url":"https://remoteok.com/rss","head_tag":"","update_tag":""},{"url":"https://weworkremotely.com/remote-jobs.rss","head_tag":"","update_tag":""},{"url":"https://hasjob.co/feed","head_tag":"entry","update_tag":"published"}]


def connection_url(url):
    request=Request(url,headers={"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"})
    return BS4(urlopen(request).read(),"xml")
 
def extract_job_listing(entry):
    job_listing=[]
    for tag in entry.children:
        if tag.name:
            if tag.name=="content":
                job_listing.append(parse_html_tag(tag))
            else:
                job_listing.append(tag.text)
    return job_listing             


def parse_html_tag(tag):
    return BS4(tag.text,"html.parser").text.strip().replace("\xa0","")



def Isupdated(head_tag,tag_name): # check whether content is new or not 
    for tag in head_tag.children:
        if tag.name:
            
            for tag1 in tag.next_siblings:
                
                if tag1.name==tag_name:
                    return dates.comparing_dates(tag1.text)

def head_and_upadte_tag(resource,index): # used for Isupdated function

    soup=connection_url(resource[index]["url"])
    head_tag=resource[index]["head_tag"]
    head_object=soup.find(head_tag)
    
    update_tag=resource[index]["update_tag"]
    
    return(head_object,update_tag)



# def extract_job_listings (parsed_xml):
#     parsed_xml.entry.next_siblings
#     pass
                             
def extracted_job_lists
# for tag in (head_and_upadte_tag(resource,2)[0]).next_siblings:    
#     if tag.name:
#         print(f"{tag.name}--> count{count}")
#         count=count+1             
