import requests

if __name__ == '__main__':

    url = 'https://www.latercera.com/'

    latercera = requests.get(url)

    print(latercera.status_code)
    print(latercera.headers)
    #print(latercera.text)
    print(latercera.request.headers)
    print(latercera.request.method)
    print(latercera.request.url)