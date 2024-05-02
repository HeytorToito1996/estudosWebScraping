from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

#Tratando possíveis erros de requisição
try:
    url = urlopen('http://pythonscraping.com/pages/page1.html')
    
except HTTPError as error:
    print(error)    
except URLError as error:
    print('Servidor Não Localizado')
else:
    print('Funcionou!')
    beautifulSoup = BeautifulSoup(url,'html.parser')
    print(beautifulSoup.h1)
            