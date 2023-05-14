#from db_folder.inserting_data import create_connection, create_entry
from string import Template
from datetime import date, timedelta, datetime
from getSource import getFlight

#try for 3 attempts: return a "[error] on querytime: __ flightDate: __"

if __name__ == "__main__":
    link = Template("https://www.airasia.com/flights/search/?origin=PEN&destination=KUL&departDate=$date&tripType=O&adult=1&child=0&infant=0&locale=en-gb&currency=MYR&ule=true&cabinClass=economy&uce=false&ancillaryAbTest=false&isOC=false&isDC=false&promoCode=&type=paired&airlineProfile=all&upsellWidget=true&upsellPremiumFlatbedWidget=true")
    
    queryTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    for single_date in (date(2023, 6, 24) + timedelta(n) for n in range(8)):
        flightDate = single_date.strftime("%d/%m/%Y")
        flightLink = link.substitute(date=(flightDate))
        
        for attempts in range(3):
            try:
                getFlight(link=flightLink, flightDate=flightDate, queryTime=queryTime, db_location="./db_folder/pen-kl.db")
                break
            except IndexError as ie:
                print(ie)
                if attempts == 2:
                    print(f"Index Error unable to handle at {queryTime} flightDate -> {flightDate}")
            except Exception as err:
                #general error handling
                print(f"Unexpected {err=}, {type(err)=} at {queryTime} flightDate -> {flightDate}")
    
    print("done.")