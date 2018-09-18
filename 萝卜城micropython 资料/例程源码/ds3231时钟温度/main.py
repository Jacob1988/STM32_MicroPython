# main.py -- put your code here!
from ds3231 import ds3231
ds=ds3231(1)
def showTimeOrDate(why,x,y,separator=':'):
    # [HH,MM,SS] >> HH:MM:SS
    why = why.replace('[','')
    why = why.replace(']','')
    why = why.replace(',',separator)
    print(why)
while True:
    ds.TEMP()
    print('Tem:',ds.TEMP())
    print('Time:'ds.DateTime())
    pyb.delay(1000)
    