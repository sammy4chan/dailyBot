#module for selenium webdriver
#takes in link
#returns html source object

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def getSource(link):
    driver = webdriver.Chrome()
    driver.implicitly_wait(50)
    
    driver.get(link)
    driver.find_element(By.ID, "journey-container")
    sleep(1)
    #driver.execute_script("window.scrollTo(0, document.getElementById('journey-container').scrollHeight)")
    #scroll agent
    for i in range(2):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        
        sleep(0.5)
    
    source = driver.page_source
    driver.quit()
    return source

#test code
if __name__ == '__main__':
    from bs4 import BeautifulSoup
    print(BeautifulSoup(getSource("https://www.airasia.com/flights/search/?origin=KUL&destination=PEN&departDate=10/06/2023&tripType=O&adult=1&child=0&infant=0&locale=en-gb&currency=MYR&ule=true&cabinClass=economy&uce=false&ancillaryAbTest=false&isOC=false&isDC=false&promoCode=&type=paired&airlineProfile=all&upsellWidget=true&upsellPremiumFlatbedWidget=true"), "html.parser").prettify())