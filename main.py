#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import time

ARD_BASE = "https://www.ardmediathek.de"

# NOTE: only loads first page, to load all results we need to use Selenium
def scrape_tatort():
    r: Response = requests.get(ARD_BASE+"/tatort")
    soup = BeautifulSoup(r.content, "html.parser")
    driver = webdriver.Chrome()

    tag: bs4.Tag = soup.find("a", href=re.compile("\/sammlung\/neue-tatort-videos"))
    if(tag):
        # print("found tag!")
        # print(tag)
        driver.get(ARD_BASE+tag['href'])
        # input()
        episodes = set()
        all_found = False
        scroll_height = 0;
        while not all_found:
            # last_height = driver.execute_script("return document.documentElement.scrollHeight")
            # print(last_height)
            soup = BeautifulSoup(r.content, "html.parser")
            episode_titles = set(map(lambda t: t.string, soup.findAll("h3")))
            if len(episode_titles - episodes) == 0:
                all_found = True
            episodes |= episode_titles
            scroll_height += driver.execute_script("return document.documentElement.scrollHeight;")
            driver.execute_script(f"window.scrollTo(0, {scroll_height});")
            # new_scroll_height = driver.execute_script("return document.documentElement.scrollHeight;")
            # if (scroll_height == new_scroll_height):
            #     driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            # driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            # input()
            # tag: bs4.Tag
            # for tag in soup.findAll("h3"):
            #     print(tag.string)
        print(episode_titles)
        input()


if __name__ == "__main__":
    scrape_tatort()
