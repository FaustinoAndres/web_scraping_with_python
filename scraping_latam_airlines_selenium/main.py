from selenium import webdriver
from selenium.webdriver.edge.options import Options



url = 'https://www.latamairlines.com/cl/es'
PATH = r"C:\Users\Faustino\Documents\GitHub\web_scraping_with_python\scraping_latam_airlines_selenium\_drivers\msedgedriver.exe"

if __name__ == "__main__":

    options = Options()
    #options.add_argument("headless")
    options.add_argument('--InPrivate')

    #driver = webdriver.Edge(executable_path=PATH)
    driver = webdriver.Edge(executable_path=PATH, options = options)
    driver.get(url)
    driver.close()