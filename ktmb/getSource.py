#module for selenium webdriver
#takes in link
#returns html source object

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from time import sleep

#link is fixed navigation isnt
#takes in param: date: int, month: int
#calculate relative month scroll distance
def getSource():
    driver = webdriver.Chrome()
    driver.get("https://online.ktmb.com.my/")
    driver.implicitly_wait(50)
    
    #close ad
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div[2]/button").click()
    
    #select location
    Select(driver.find_element(By.XPATH, "/html/body/div[3]/div/form/div/div[1]/select")).select_by_value("19100") #kl sentral
    Select(driver.find_element(By.XPATH, "/html/body/div[3]/div/form/div/div[3]/select")).select_by_value("600") #pen
    
    #select date
    driver.find_element(By.XPATH, "/html/body/div[3]/div/form/div/div[5]/div/div[1]/input").click() #click on depDate
    
    driver.find_element(By.XPATH, "/html/body/section/div/div[1]/section/header/div[2]/button[2]").click() # next month btn
    
    calendar = driver.find_element(By.XPATH, "/html/body/section/div/div[1]/section/div[2]")
    calendar.find_element(By.XPATH, ".//*[text()='30' and not(contains(@class, 'is-previous-month') or contains(@class, 'is-next-month'))]").click()
    
    driver.find_element(By.XPATH, "/html/body/section/div/a[2]").click() #click on oneway btn
    
    driver.find_element(By.XPATH, "/html/body/div[3]/div/form/div/div[5]/div/div[4]/button").click() #search/submit btn
    
    sleep(2)
    srcHtml = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/table/tbody").get_attribute("outerHTML")
    driver.quit()
    
    return srcHtml #return after closing browser instance

#test code
if __name__ == '__main__':
    soup = BeautifulSoup(getSource(), "html.parser")
    print(soup.prettify())