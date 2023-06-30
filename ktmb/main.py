from getSource import getSource, parser, add_data
from datetime import datetime, date, timedelta

def track(year, month, day, timerange, direction):
    queryTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    for single_date in (date(year, month, day) + timedelta(n) for n in range(timerange)):
        trainDate = single_date.strftime("%d/%m/%Y")
        for attempts in range(3):
            try:
                data = parser(getSource(single_date, direction)) #0 - klpen 1-penkl
                for i in data:
                    add_data(direction, (queryTime, trainDate, i[1], i[2], i[5], i[4], i[0], i[3]))
                    #(queryTime, trainDate, depTime, arrTime, price, seats, trainName, duration)
                    #['Platinum - 9171', '05:26', '09:29', '4h 3m', ' 315', "MYR 77.00"]
                break
            except IndexError as ie:
                print(ie)
                if attempts == 2:
                    print(f"Index Error unable to handle at {queryTime} trainDate -> {trainDate}")
            except Exception as err:
                #general error handling
                print(f"Unexpected {err=}, {type(err)=} at {queryTime} trainDate -> {trainDate}")
                
    print("done.")
    
# bm_kl #kl_bm
track(2022, 7, 13, 1, "kl_bm")
track(2022, 7, 16, 1, "bm_kl")