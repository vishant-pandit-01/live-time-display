import datetime
import time

while True:
    now = datetime.datetime.now()
                 #for 24 hour format
    # print(now.strftime("%H:%M:%S"), end="\r")       

                #for 12 hour format
    print(now.strftime("%I:%M:%S"), end="\r")        
    
    time.sleep(1)
