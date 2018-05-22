import re
from bs4 import BeautifulSoup

html = '''<strong>Text:</strong>   

        <a href='http://domain.com'>url</a>'''

soup = BeautifulSoup(html)
label = soup.find("strong" , text='Text:')
contact = label.findNext('a')

if contact.get('href') != None:
    print contact
else:
    print "No href
