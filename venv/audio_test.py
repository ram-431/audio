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

def get_drive_links():

    links=get_page_links()
    drive_links=[]
    for link in links:

        html_page = requests.get(link)
        soup = BeautifulSoup(html_page.content,'html.parser')
        for link in soup.findAll('a', attrs={'href': re.compile("^https://drive.google.com")}):
            drive_links.append((link.get('href')))
    return(drive_links)
def download():
    drive_links=get_drive_links()
    a=1
    for link in drive_links:
        modified_drive_link=link.replace('open','uc')
        outfile = linux  + "/Desktop/osho-mahageeta/discourse "+str(a)+".mp3"
        url=modified_drive_link
        gdown.download(url, outfile, quiet=True)

        print("discourse "+str(a)+" downloaded")
        a=a+1
linux = os.getenv("HOME")
download()


