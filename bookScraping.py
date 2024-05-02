from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def getPrices(url):
    info = []
    try:
        site = urlopen(url)
        page = site.read().decode('utf-8')
    except HTTPError as Error:
        return None
    except URLError as Error:
        return None

    try:
        beautifulSoup = BeautifulSoup(page,'html.parser')
        prices = beautifulSoup.find_all('article',class_='product_pod')
    except AttributeError as Error:
        return None
    
    for price in prices:
       title = price.find('h3').find('a')['title']
       price_element = price.find('div',class_='product_price')
       price_text = price_element.find('p',class_='price_color').text.strip()
       book = {'title' : title, 'price' : price_text}
       info.append(book)
    return info
         
for i in range(50):
    url = 'https://books.toscrape.com/catalogue/page-'+str(i)+'.html'
    books = getPrices(url)
    print ("Scraping page :" + str(i))
    print(books)
    
    


