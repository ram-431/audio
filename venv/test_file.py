from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os 
import gdown
import re
 
    
    
options = webdriver.FirefoxOptions()
options.add_argument("--private")



#browser = webdriver.Firefox(options=options)



def get_page_links():

    page_url= "http://osho-dhara-community.blogspot.com/2016/06/osho-audio-discourses-osho-selected.html"

    links=[]

    html_page = requests.get(page_url)
    soup = BeautifulSoup(html_page.content,'html.parser')
    for link in soup.findAll('a', attrs={'href': re.compile("^http://osho-dhara-community.blogspot.com/2016/06/osho-audio-discourses-osho")}):
        #print(link.get('href'))
        links.append(link.get('href'))
    page_links=links[3:11]
    return(page_links)

def get_drive_links():

    links=get_page_links()
    drive_links=[]
    discourse_name=[]
    for link in links:

        html_page = requests.get(link)
        soup = BeautifulSoup(html_page.content,'html.parser')
        for link in soup.findAll('a', attrs={'href': re.compile("^https://drive.google.com")}):
            drive_links.append((link.get('href')))
            discourse_name.append((link.contents[0]))
            #print(link.get('href'))
            #print(link.contents[0])
    return(drive_links,discourse_name)
def download():
    drive_links,names=get_drive_links()
    a=1
    for link in drive_links:
        url=link.replace('open','uc')
        outfile = linux  + "/Desktop//Osho-Discourses/"+names[drive_links.index(link)]+".mp3"
        gdown.download(url, outfile, quiet=True)

        print(names[drive_links.index(link)]+"   downloaded")
        a=a+1
linux = os.getenv("HOME")
download()


