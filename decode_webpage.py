#!/usr/bin/env python3
# DECODE A WEBPAGE
## if the program not run then restart kernel if not then restart ide again
## should have to connect with internet 

import urllib.request
from bs4 import BeautifulSoup
request=urllib.request.urlopen('https://timesofindia.indiatimes.com/')
soup=BeautifulSoup(request,'lxml')
for heading in soup.find_all('h3'): # heading size may vary
    print(heading.get_text())
    
