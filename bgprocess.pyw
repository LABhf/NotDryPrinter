import csv
import os
import datetime
import time
blist=[]

with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row == []:
            pass
        else:
            blist.append(row)

clist=[]
for a in blist:
    for i in a:
        clist.append(i)

#               ###    ###

wn=clist[0]
hn=clist[1]

week = wn
week=str(week)

hour =int(hn)-1
hour=str(hour)

#since the != hour triggers at a hour diferent
# then the chosen, we go back 1 hour so that it prints on time

delay = 1
now = datetime.datetime.now()


while 1 == 1:
    now = datetime.datetime.now()
    time.sleep(delay)


    while now.strftime("%w") == week and now.strftime("%H") == hour:
        now = datetime.datetime.now()

        time.sleep(delay)

        if now.strftime("%H") != hour:
            os.startfile("aviso.py", "open")
