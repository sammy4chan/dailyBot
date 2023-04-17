#https://www.airasia.com/flights/search/?origin=KUL&destination=PEN&departDate=10/06/2023&tripType=O&adult=1&child=0&infant=0&locale=en-gb&currency=MYR&ule=true&cabinClass=economy&uce=false&ancillaryAbTest=false&isOC=false&isDC=false&promoCode=&type=paired&airlineProfile=all&upsellWidget=true&upsellPremiumFlatbedWidget=true


import time
from getSource import getSource

#scrape 10 a day
dayInterval = (10, 24)
for i in range(dayInterval[0], dayInterval[1]+1):
    link = f"https://www.airasia.com/flights/search/?origin=KUL&destination=PEN&departDate={i}/06/2023&tripType=O&adult=1&child=0&infant=0&locale=en-gb&currency=MYR&ule=true&cabinClass=economy&uce=false&ancillaryAbTest=false&isOC=false&isDC=false&promoCode=&type=paired&airlineProfile=all&upsellWidget=true&upsellPremiumFlatbedWidget=true"
    
    getSource(link)