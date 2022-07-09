import requests

if __name__ == '__main__':

    url = 'https://www.latercera.com/'

    latercera = requests.get(url)

    print(latercera.status_code)
    #print(latercera.text)
