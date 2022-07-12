import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':

    url = 'https://www.latercera.com/'

    latercera = requests.get(url)

    # Descargando una páquina web
    #print(latercera.status_code)
    #print(latercera.headers)
    #print(latercera.text)
    #print(latercera.request.headers)
    #print(latercera.request.method)
    #print(latercera.request.url)

    # parseando HTML con BeautifulSoup
    s = BeautifulSoup(latercera.text, 'lxml')
    #s = BeautifulSoup(latercera.text, 'html.parser')
    #print(s.prettify())
    print(type(s))
    print(s.find('div', attrs={'class': "top-menu"}))
    print(s.find('header', attrs={'class': "main-header"}))
