import os           #operating system dependent functionality
import csv
alist=[]

def w(alist):
    file = open("data.csv", "w")
    writer = csv.writer(file)
    for a in alist:
        writer.writerow([a])




#Gui basica para escolher o dia(da semana) e hora da avaliação, por enquanto vai existir uma av. por semana..
def mainp():

    aval=1

    print("")
    print("This program will print a test file once a week to keep your printer 'healthy' ")
    print("Chose day of the week. Sunday[0],Monday[1]..., Saturday[6]")

    wn = -5         #default number for IF engaging
    wn = int(wn)

    def wquest(wn):         #define week question/filter (0,..,6), if ok def hour question

        wn = input("Choose number: ")
        wn = int(wn)

        if wn < 0 or wn > 6 and wn:         #input filter
            print("Choose number between 0 and 6 ")
            wquest(wn)
        else:
            print("Week ok, now lets choose the hour for printing")
            wn=str(wn)
            alist.append(wn)
            hn=13           #default hour

            def hquest(hn):

                hn = input("Choose hour: ")
                hn = int(hn)
                if hn < 0 or hn > 24:         #input filter
                    print("0 to 24 number...")
                    hquest(hn)

                else:
                    print("Hour ok")
                    #start .wpy     with the values from this gui...
                    os.startfile("bgprocess.py", "open")    #ADD o .pyw depois   ....
                    hn=str(hn)
                    alist.append(hn)


            hquest(hn)

    wquest(wn)
    w(alist)


if __name__ == '__main__':
    print("#T")      #isso só vai rodar se for executado diretamente o arquivo mymath
    mainp()
