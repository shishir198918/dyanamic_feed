from urllib.request import urlopen,Request
from bs4 import BeautifulSoup as BS4
from pprint import pprint

resource=["https://remoteok.com/rss","https://weworkremotely.com/remote-jobs.rss","https://hasjob.co/feed"]


def connection(url):
    request=Request(url,headers={"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"})
    #return urlopen(request).read()
    return BS4(urlopen(request).read(),"xml")



def multiple_request(url_list):
    for url in url_list:
        print(connection(url))



def to_json(parsed_xml):
    for entry in parsed_xml.entry.next_siblings:
        if entry.name:
            for tag in entry.children:
                if tag.name=="content":

                    print(BS4(tag.text,"html.parser").text)
            




print(to_json(connection(resource[2])))