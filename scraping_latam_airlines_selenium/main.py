from selenium import webdriver


url = 'https://www.latamairlines.com/cl/es'

if __name__ == "__main__":


    driver = webdriver.Edge(executable_path='.\_drivers\msedgedriver.exe')

    driver.get(url)

    driver.close()