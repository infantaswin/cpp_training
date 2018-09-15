#!/usr/bin/env python3

# specific dependency modules next
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

#system level imports first
import sys
import os
import io
import json
#global package imports next
import requests
import gzip
from datetime import datetime


agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
# print(soup)
def easy(soupq):
    for a in soupq.find_all('a'):
        for img in a.find_all('img',attrs={'class':'bqpht zoomc delayedPhotoLoad'}):
            for alt img.find_all('alt'):
                print(alt)
            # print(img.fin)
        # s=a.text
        # a={}
        # a['quotes']=s
        # return a
        # return s



input="https://www.brainyquote.com/topics/motivational"
link=requests.get(input,headers=agent)
soup=BeautifulSoup(link.text,'lxml')
x=easy(soup)
# print(x)
