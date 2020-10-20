# Code from Cory Althoff's Self Taught Programmer.
# Google changed from "html" to "articles" in the url for these. 
# Also altered to write to csv insead of txt file like assignment.

import csv
import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        soup= BeautifulSoup(html, parser)
        with open("beautiful_output.csv", "w", newline = '') as file:
            writer = csv.writer(file, delimiter=",")
            for tag in soup.find_all("a"):
                url= tag.get("href")
                if url and "articles" in url:
                    print("\n" + url)
                    writer.writerow(["\n" + url])

news = "https://news.google.com/"
Scraper(news).scrape()
