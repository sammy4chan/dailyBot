#module for selenium webdriver
#takes in link
#returns html source object

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import sqlite3
from sqlite3 import Error
from bs4 import BeautifulSoup

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_entry(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
    sql = ''' INSERT INTO flights(queryTime, flightDate, depTime, arrTime, price)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid

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

#scrape 10 a day
def getFlight(link:str, flightDate:str, queryTime, db_location):
    soup = BeautifulSoup(getSource(link), "html.parser")
    journey_container = soup.find(id="journey-container")
    
    conn = create_connection(db_location)
    with conn:
        #time to parse the link
        #soup = BeautifulSoup(open("./flights/sample.html", "r"), "html.parser") #offline ver
        
        times = [i.text.strip() for i in journey_container.find_all("p", class_="cipHcF")] #cipHcF for time text <p>
        prices = [i.text.strip() for i in journey_container.find_all("p", class_="djKEhy")] #djKEhy for price text <p>
        
        #raise an early error >:((
        if len(times) < 10 or len(prices) < 10:
            return IndexError
        
        #take the first x values and returns them as a string to be sent by bot
        for j in range(10):
            entry = (queryTime, str(flightDate), f"{times[(2*j)]}", f"{times[(2*j)+1]}", prices[j])
            create_entry(conn, entry)

    return "sucess"

#test code
if __name__ == '__main__':
    from bs4 import BeautifulSoup
    print(BeautifulSoup(getSource("https://www.airasia.com/flights/search/?origin=KUL&destination=PEN&departDate=10/06/2023&tripType=O&adult=1&child=0&infant=0&locale=en-gb&currency=MYR&ule=true&cabinClass=economy&uce=false&ancillaryAbTest=false&isOC=false&isDC=false&promoCode=&type=paired&airlineProfile=all&upsellWidget=true&upsellPremiumFlatbedWidget=true"), "html.parser").prettify())