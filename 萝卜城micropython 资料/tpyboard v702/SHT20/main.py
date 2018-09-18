# main.py -- put your code here!
from SHT20 import SHT20
ds=SHT20(1)

while True:

    H=ds.TEMP()
    S=ds.TEMP1()
    H=125*H/256-6
    S=175.72*S/256-46.85
    #H=H/6.000
    print('原始数据:',ds.TEMP(),ds.TEMP1())
    print('温度:',S,'湿度:',H)
    #print(ds.DateTime())

    pyb.delay(1000)
