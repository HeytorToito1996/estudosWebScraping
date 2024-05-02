from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def getScore(url):
    try:
        html = urlopen(url)
    except HTTPError as error:
        return None
    except URLError as error:
        return None
    
    try:
        beautifulSoup = BeautifulSoup(html.read(),'html.parser')
        scores = beautifulSoup.find('div',{'class':'game_summaries'}).text
    except AttributeError as error:
        return None
    return scores

url = "https://www.basketball-reference.com/boxscores/"
scores = getScore(url)

if (scores == None):
    print("Informação não encontrada")
else:
    print(scores)    