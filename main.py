from urllib.request import urlopen,Request
from bs4 import BeautifulSoup as BS4
from pprint import pprint
import dates



resource=[{"url":"https://remoteok.com/rss","head_tag":"","update_tag":""},{"url":"https://weworkremotely.com/remote-jobs.rss","head_tag":"","update_tag":""},{"url":"https://hasjob.co/feed","head_tag":"entry","update_tag":"published"}]


def connection_url(url):
    request=Request(url,headers={"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"})
    return BS4(urlopen(request).read(),"xml")
 
def extract_job(entry,updated_tag_name):
    job_listing={}
    for tag in entry.children: 
        if tag.name:
            if tag.name==updated_tag_name and not Isupdated(tag):
                return None
                #print(Isupdated(tag))
            if tag.name in ["content"]:
                job_listing['content']=parse_html_tag(tag)
            if tag.name in ["title"]:
                job_listing["title"]=tag.text
            if tag.name in ["published"]:
                job_listing["published"]=tag.text
            if tag.name in ["link"]:
                job_listing["link"]=tag.text
            if tag.name in ["location"]:
                job_listing["location"]=tag.text  

    return job_listing             


def parse_html_tag(tag):
    return BS4(tag.text,"html.parser").text.strip().replace("\xa0","")



def Isupdated(update_tag): # check whether content is new or not 
    return dates.comparing_dates(update_tag.text)


def head_and_upadate_tag(resource,index): # used for Isupdated function

    soup=connection_url(resource[index]["url"])
    head_tag=resource[index]["head_tag"]
    head_object=soup.find(head_tag)
    
    update_tag=resource[index]["update_tag"]
    
    return(head_object,update_tag)


                             
def extracted_jobs(resource,index):
    jobs=[]
    head_tag,update_tag_name=head_and_upadate_tag(resource,index)
    for entry_tag in head_tag.next_siblings:
        if entry_tag.name:
            jobs.append(extract_job(entry_tag,update_tag_name))
    return jobs

#soup=connection_url(resource[2]["url"]).entry
#print(Isupdated(soup.published))        
pprint(extracted_jobs(resource,2))
             
