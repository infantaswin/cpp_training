from bs4 import BeautifulSoup
from urllib.request import Request,urlopen

inputs="view-source:https://www.scimagojr.com/journalsearch.php?"
url=Request(inputs)
fp=urlopen(url)
soup=BeautifulSoup(fp,"lxml")
print(soup)
