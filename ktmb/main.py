#module for selenium webdriver
#takes in link
#navigates
#returns html source object

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time

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
    
    onwardDate = driver.find_element(By.XPATH, "/html/body/div[3]/div/form/div/div[5]/div/div[1]/input")
    onwardDate.click()
    
    nextMonthBtn = driver.find_element(By.XPATH, "/html/body/section/div/div[1]/section/header/div[2]/button[2]")
    nextMonthBtn.click()
    
    calendar = driver.find_element(By.XPATH, "/html/body/section/div/div[1]/section/div[2]")
    elm = calendar.find_element(By.XPATH, ".//*[text()='30' and not(contains(@class, 'is-previous-month') or contains(@class, 'is-next-month'))]")
    elm.click()
    
    oneWayBtn = driver.find_element(By.XPATH, "/html/body/section/div/a[2]")
    oneWayBtn.click()
    
    searchBtn = driver.find_element(By.XPATH, "/html/body/div[3]/div/form/div/div[5]/div/div[4]/button")
    searchBtn.click()
    
    time.sleep(5) #wait or implement implicit wait
    departureList = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/table/tbody")
    
    soup = BeautifulSoup(departureList.get_attribute("outerHTML"), "html.parser")
    print(soup)
    
    driver.quit()