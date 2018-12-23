#!/usr/bin/env python3
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url =  'https://www.linkedin.com/jobs/search\?f_GC=us.7-1-0-43-16,us.7-1-0-43-14,us.7-1-0-43-21,us.7-1-0-43-18,us.7-1-0-43-12,us.7-1-0-43-19,us.7-1-0-43-4,us.7-1-0-43-8,us.7-1-0-1-7\&f_I=4,96'
uClient = uReq(my_url)
page_html = uClient.read()

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class":"searchResultsStory"})

for container in containers:
    info = container.p.findAll("p",{})
    print(info)

uClient.close()
