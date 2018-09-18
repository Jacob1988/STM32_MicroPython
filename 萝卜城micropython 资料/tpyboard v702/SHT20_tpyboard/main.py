# main.py -- put your code here!
import pyb
from TPYBoard_SHT20 import SHT20
from pyb import Pin


y3 = Pin('Y3',Pin.OUT_PP) 

ds=SHT20(1)
while True:
    H=ds.TEMP()
    S=ds.TEMP1()
    H=125*H/256-6
    S=175.72*S/256-46.85
    H=H/6.000
    print('原始数据:',ds.TEMP(),ds.TEMP1())
    print('温度:',S,'湿度:',H)
    #print(ds.DateTime())
    if S>20:
        print(S)
        y3.value(1)
    else :
        print(S)
        y3.value(0)
    pyb.delay(1000)
    
