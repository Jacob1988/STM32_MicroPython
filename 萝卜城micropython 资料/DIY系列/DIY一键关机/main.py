# main.py -- put your code here!
import pyb
FLAG=0 #flag标记，当为1时，关机
 
def release_key_once():
    buf = bytearray(8) # report is 8 bytes long
    buf[2] = 0
    hid.send(buf) # key released
    pyb.delay(10)
def press_key_once(key):
    buf = bytearray(8) # report is 8 bytes long
    buf[2] = key
    hid.send(buf) # key released
    pyb.delay(10)
def press_2key(key1,key2):
    buf = bytearray(8) # report is 8 bytes long
    buf[0] = key1
    buf[2] = key2
    hid.send(buf) # key released
    pyb.delay(10)
def release_2key():
    buf = bytearray(8) # report is 8 bytes long
    buf[0] = 0
    buf[2] = 0
    hid.send(buf) # key released
    pyb.delay(10)
     
def shutdownpc():
    global FLAG
    pyb.LED(3).on()
    FLAG=1
    pyb.delay(300)
    pyb.LED(3).off()
 
hid=pyb.USB_HID()   
sw=pyb.Switch()
sw.callback(shutdownpc)
while(1): #led4闪烁表示板子已经正常工作
    pyb.LED(4).toggle()
    pyb.delay(500)
    print(FLAG)
    if FLAG==1:
        pyb.delay(1000) #开始加入1秒延时
        press_2key(0x08,0x15)#具体键值见附录部分
        release_2key()
        pyb.delay(100)
        a=[0x06,0x10,0x07,0x28] #cmd+enter
        for i in a:
            press_key_once(i)
            release_key_once()
        pyb.delay(1000)
        #shutdown -s -t 60 + enter
        a=[0x16,0x0b,0x18,0x17,0x07,0x12,0x1a,0x11,0x2c,0x2d,0x16,0x2c,0x2d,0x17,0x2c,0x23,0x27,0x28]
        for i in a:
            press_key_once(i)
            release_key_once()
        pyb.delay(1000)
        FLAG=0 