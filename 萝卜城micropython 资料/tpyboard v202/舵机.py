import machine
import time, math
while 1:
    servo = machine.PWM(machine.Pin(4), freq=50)
    servo.duty(40)
    time.sleep(1)
    servo.duty(115)
    time.sleep(1)
    servo.duty(77)
    time.sleep(1)