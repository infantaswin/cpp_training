from bs4 import BeautifulSoup
import requests
import urllib3


inputs="https://www.dataquest.io/blog/web-scraping-tutorial-python/"
url=requests.get(inputs)
soup=BeautifulSoup(url.text,"lxml")

#print(soup)

def meta(soup):
    for tag in soup.find_all('head'):
        #print(tag)
        for meta in tag.find_all('meta'):
            met=meta.prettify()
            me=met['name']
##            print(me)
                   

def titles(soup):

    for tag in soup.find_all('head'):
        for title in tag.find_all('title'):
            print(title.get_text())
               

meta(soup)
#titles(soup)
