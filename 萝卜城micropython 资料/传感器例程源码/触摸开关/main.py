# main.py -- put your code here!
import pyb
from pyb import Pin

a = Pin('X1',Pin.IN)
while 1:
    print(a.value())