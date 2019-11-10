import gdown
from bs4 import BeautifulSoup
import requests
import re
import os
 


 def counter():
    if 'cnt' not in counter.__dict__:
        counter.cnt = 0
    counter.cnt += 1
    return counter.cnt
    


def get_page_links():

    page_url= "http://osho-dhara-community.blogspot.com/2016/06/osho-audio-discourses-maha-geeta-osho.html"

    links=[]

    html_page = requests.get(page_url)
    soup = BeautifulSoup(html_page.content,'html.parser')
    for link in soup.findAll('a', attrs={'href': re.compile("^http://osho-dhara-community.blogspot.com/2016/06/osho-audio-discourses-maha-geeta")}):
       # print(link.get('href'))
        links.append(link.get('href'))
    page_links=links[5:22]
    #print(page_links)
    return(page_links)

def download():

    links=get_page_links()
    for link in links:
        html_page = requests.get(link)
        soup = BeautifulSoup(html_page.content,'html.parser')
        for link in soup.findAll('a', attrs={'href': re.compile("^https://drive.google.com")}):
            drive_links=(link.get('href'))
            modified_drive_link=drive_links.replace('open','uc')
            a=counter()
            outfile = linux  + "/Desktop/osho-mahageeta/discourse "+str(a)
            url=modified_drive_link
            gdown.download(url, outfile, quiet=True)
            
            print("discourse "+str(a)+" downloaded")
            
            
    return(drive_links)
linux = os.getenv("HOME")
download()




