from bs4 import BeautifulSoup
from getSource import getSource
#from db_folder.inserting_data import create_connection, create_entry
import sqlite3
from sqlite3 import Error
from string import Template
from datetime import date, timedelta, datetime

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

#scrape 10 a day
def getFlight(link:str, flightDate:str, queryTime):
    soup = BeautifulSoup(getSource(link), "html.parser")
    journey_container = soup.find(id="journey-container")
    
    conn = create_connection("./db_folder/flights.db")
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

#try for 3 attempts: return a "[error] on querytime: __ flightDate: __"

if __name__ == "__main__":
    link = Template("https://www.airasia.com/flights/search/?origin=KUL&destination=PEN&departDate=$date&tripType=O&adult=1&child=0&infant=0&locale=en-gb&currency=MYR&ule=true&cabinClass=economy&uce=false&ancillaryAbTest=false&isOC=false&isDC=false&promoCode=&type=paired&airlineProfile=all&upsellWidget=true&upsellPremiumFlatbedWidget=true")
    
    queryTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    for single_date in (date(2023, 6, 10) + timedelta(n) for n in range(15)):
        flightDate = single_date.strftime("%d/%m/%Y")
        flightLink = link.substitute(date=(flightDate))
        
        for attempts in range(3):
            try:
                getFlight(link=flightLink, flightDate=flightDate, queryTime=queryTime)
                break
            except IndexError as ie:
                print(ie)
                if attempts == 2:
                    print(f"Index Error unable to handle at {queryTime} flightDate -> {flightDate}")
            except Exception as err:
                #general error handling
                print(f"Unexpected {err=}, {type(err)=} at {queryTime} flightDate -> {flightDate}")