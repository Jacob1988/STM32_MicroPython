# main.py -- put your code here!
import pyb
from pyb import Pin

heart=Pin('X1',Pin.IN)
adc = pyb.ADC(Pin('Y11'))
while 1:
    print(heart.value())
    print(adc.read())
    pyb.delay(1000)