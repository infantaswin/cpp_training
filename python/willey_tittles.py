from bs4 import BeautifulSoup
import requests


inputs="https://onlinelibrary.wiley.com"
url=requests.get(inputs)
soup=BeautifulSoup(url.text,"lxml")
#print(soup)

def titles(soup):

    for tag in soup.find_all('body'):
        
        for title in tag.find_all('section',attrs={"class":"subjects-container"}):
            for titl in title.find_all('a'):
                 print(titl.get_text())
               
titles(soup)

      
