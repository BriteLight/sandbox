#!/usr/bin/env python3
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url =  'https://www.crowdrise.com/search/all/African+American'
uClient = uReq(my_url)
page_html = uClient.read()

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class":"searchResultsStory"})

for container in containers:
    info = container.p.findAll("p",{})
    print(info)

uClient.close()
