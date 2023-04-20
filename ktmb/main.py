#module for selenium webdriver
#takes in link
#navigates
#returns html source object

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
link = "https://online.ktmb.com.my/"

dates = [10, 24]
#for i in range(dates[0], dates[1]+1):
for i in range(1):
    driver.get(link)
    
    #navigate
    ad_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div[2]/button")
    ad_button.click()
    
    #select dates
    departureStationSelect = Select(driver.find_element(By.XPATH, "/html/body/div[3]/div/form/div/div[1]/select"))
    departureStationSelect.select_by_value("19100")
    
    arrivalStationSelect = Select(driver.find_element(By.XPATH, "/html/body/div[3]/div/form/div/div[3]/select"))
    arrivalStationSelect.select_by_value("600")