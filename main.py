from urllib.request import urlopen,Request
from bs4 import BeautifulSoup as BS4
from pprint import pprint

resource=["https://remoteok.com/rss","https://weworkremotely.com/remote-jobs.rss","https://hasjob.co/feed"]

#resource=["https://remoteok.com/rss"]

def connection(url):
    request=Request(url,headers={"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"})
    #return urlopen(request).read()
    #a = BS4(urlopen(request).read(),"xml")
    #print('a-- connetion',a)
    return BS4(urlopen(request).read(),"xml")



def multiple_request(url_list):
    for url in url_list:
        print(connection(url))



def extract_job_listings (parsed_xml):
    jobs=[]
    for entry in parsed_xml.entry.next_siblings:
        if entry.name:
            jobs.append(extract_job_listing(entry))
    #entries=parsed_xml.entry.next_siblings
    return jobs
#[extract_job_listing(entry) for entry in entries  if entry.name] 


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



pprint(extract_job_listings(connection(resource[2])))

#(to_json(connection(resource[2])))