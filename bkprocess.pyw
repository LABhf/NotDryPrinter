import os
import datetime
import time

week=4
week=str(week)

hour=12
hour=str(hour)


delay = 1
now = datetime.datetime.now()

while 1 == 1:
    now = datetime.datetime.now()
    time.sleep(delay)
    
    while now.strftime("%w") == week and now.strftime("%H") == hour:
        now = datetime.datetime.now()
        
        time.sleep(delay)

        if now.strftime("%H") != hour:
            os.startfile("C:/Users/PC/a2.py", "open")

