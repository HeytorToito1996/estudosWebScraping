from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen('http://pythonscraping.com/pages/page1.html')

beautifulSoup = BeautifulSoup(url,'html.parser')

print(beautifulSoup.h1)