#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import re

ARD_BASE = "https://www.ardmediathek.de"

# NOTE: only loads first page, to load all results we need to use Selenium
def scrape_tatort():
    r = requests.get(ARD_BASE+"/tatort")
    soup = BeautifulSoup(r.content, "html.parser")

    tag: bs4.Tag = soup.find("a", href=re.compile("\/sammlung\/neue-tatort-videos"))
    if(tag):
        # print("found tag!")
        # print(tag)
        r = requests.get(ARD_BASE+tag['href'])
        soup = BeautifulSoup(r.content, "html.parser")
        for tag in soup.findAll("h3"):
            print(tag.string)



if __name__ == "__main__":
    scrape_tatort()
