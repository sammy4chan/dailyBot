#module for selenium webdriver
#takes in link
#returns html source object

from selenium import webdriver

def getSource(link):
    driver = webdriver.Chrome()
    
    driver.get(link)
    source = driver.page_source()
    driver.quit()
    return source