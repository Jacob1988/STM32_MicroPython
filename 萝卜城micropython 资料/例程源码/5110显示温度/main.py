#main.py
import pyb
import upcd8544
from machine import SPI,Pin
from ds18x20 import DS18X20

Pin("Y11",Pin.OUT_PP).low()#GND
Pin("Y9",Pin.OUT_PP).high()#VCC
pyb.delay(100)
DQ=DS18X20(Pin('Y10'))#DQ
while True:
    tem = DQ.read_temp()
    SPI = pyb.SPI(1) #DIN=>X8-MOSI/CLK=>X6-SCK
    #DIN =>SPI(1).MOSI 'X8' data flow (Master out, Slave in)
    #CLK =>SPI(1).SCK  'X6' SPI clock
    RST    = pyb.Pin('X1')
    CE     = pyb.Pin('X2')
    DC     = pyb.Pin('X3')
    LIGHT  = pyb.Pin('X4')
    lcd_5110 = upcd8544.PCD8544(SPI, RST, CE, DC, LIGHT)
    lcd_5110.lcd_write_string('Today',0,0)
    lcd_5110.lcd_write_string('Tusday',6,1)
    lcd_5110.lcd_write_string('Temperature',12,2)
    lcd_5110.lcd_write_string(str(tem),60,3)
    lcd_5110.lcd_write_string('Bye',0,4)
    pyb.delay(10000)