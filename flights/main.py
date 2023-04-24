from bs4 import BeautifulSoup
from datetime import datetime
from getSource import getSource
#from sqlite3 import Error
from db_folder.inserting_data import create_connection, create_date, create_entry

#scrape 10 a day
def flights():
    allFlightInfo = [] #formatted like [date, slot1, slot2, ...slot10]
    dayInterval = (10, 24)
    for i in range(dayInterval[0], dayInterval[1]+1):
        link = f"https://www.airasia.com/flights/search/?origin=KUL&destination=PEN&departDate={i}/06/2023&tripType=O&adult=1&child=0&infant=0&locale=en-gb&currency=MYR&ule=true&cabinClass=economy&uce=false&ancillaryAbTest=false&isOC=false&isDC=false&promoCode=&type=paired&airlineProfile=all&upsellWidget=true&upsellPremiumFlatbedWidget=true"
        
        soup = BeautifulSoup(getSource(link), "html.parser")
        journey_container = soup.find(id="journey-container")
        
        conn = create_connection("./db_folder/flights.db")
        with conn:
            dates = (datetime.now().strftime("%d/%m/%Y"), f"{i}/06/2023") #flight dates
            create_date(conn, dates)
            
            #time to parse the link
            #soup = BeautifulSoup(open("./flights/sample.html", "r"), "html.parser") #offline ver
            
            times = [i.text.strip() for i in journey_container.find_all("p", class_="cipHcF")] #cipHcF for time text <p>
            prices = [i.text.strip() for i in journey_container.find_all("p", class_="djKEhy")] #djKEhy for price text <p>
            
            #take the first x values and returns them as a string to be sent by bot
            for j in range(10):
                entry = (f"{i}/06/2023", f"{times[(2*j)]}", f"{times[(2*j)+1]}", f"RM{prices[j]}")
                create_entry(conn, entry)
        

if __name__ == "__main__":
    try:
        print(flights())
    except IndexError as e:
        print(f"Index error {e}")