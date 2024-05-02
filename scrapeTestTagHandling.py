from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as error:
        return None
    except URLError as error:
         return None
    try:
        beautifulSoup = BeautifulSoup(html.read(),'html-parser')
        title = beautifulSoup.body.span
    except AttributeError as error:
        return None
    return title

title = getTitle('https://pythonscraping.com/pages/page1.html/')    

if (title == None):
        print('Título Não Encontrado')
else:
     print(title)        