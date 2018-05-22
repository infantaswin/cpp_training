from bs4 import BeautifulSoup

with open("sample1.html") as fp:
    soup = BeautifulSoup(fp,"lxml")
    print(soup.title.string)

