from bs4 import BeautifulSoup
import requests
import re

html_page = requests.get("http://osho-dhara-community.blogspot.com/2016/06/osho-audio-discourses-maha-geeta-osho.html")
soup = BeautifulSoup(html_page.content,'html.parser')
for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
    print (link.get('href'))

class="ndfHFb-c4YZDc-Bz112c ndfHFb-c4YZDc-C7uZwb-LgbsSe-Bz112c ndfHFb-c4YZDc-nupQLb-Bz112c"
class="ndfHFb-c4YZDc-Bz112c ndfHFb-c4YZDc-C7uZwb-LgbsSe-Bz112c ndfHFb-c4YZDc-nupQLb-Bz112c"
ndfHFb-c4YZDc-to915-LgbsSe ndfHFb-c4YZDc-C7uZwb-LgbsSe VIpgJd-TzA9Ye
-eEGnhe ndfHFb-c4YZDc-LgbsSe ndfHFb-c4YZDc-C7uZwb-LgbsSe-SfQLQb-Bz112c