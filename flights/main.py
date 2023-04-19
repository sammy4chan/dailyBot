from bs4 import BeautifulSoup
from getSource import getSource

#scrape 10 a day
def flights():
    allFlightInfo = [] #formatted like [date, slot1, slot2, ...slot10]
    dayInterval = (10, 24)
    for i in range(dayInterval[0], dayInterval[1]+1):
        return_arr = [f"{i}/6/2023"]
        
        link = f"https://www.airasia.com/flights/search/?origin=KUL&destination=PEN&departDate={i}/06/2023&tripType=O&adult=1&child=0&infant=0&locale=en-gb&currency=MYR&ule=true&cabinClass=economy&uce=false&ancillaryAbTest=false&isOC=false&isDC=false&promoCode=&type=paired&airlineProfile=all&upsellWidget=true&upsellPremiumFlatbedWidget=true"
        
        #time to parse the link
        #soup = BeautifulSoup(open("./flights/sample.html", "r"), "html.parser") #offline ver
        soup = BeautifulSoup(getSource(link), "html.parser")
        
        journey_container = soup.find(id="journey-container")
        times = [i.text.strip() for i in journey_container.find_all("p", class_="cipHcF")] #cipHcF for time text <p>
        prices = [i.text.strip() for i in journey_container.find_all("p", class_="djKEhy")] #djKEhy for price text <p>
        
        #take the first x values and returns them as a string to be sent by bot
        for i in range(10):
            return_arr.append(f"{times[(2*i)]} --> {times[(2*i)+1]} : RM{prices[i]}")
        allFlightInfo.append(return_arr)

    return allFlightInfo

if __name__ == "__main__":
    try:
        print(flights())
    except IndexError as e:
        print(f"Index error {e}")