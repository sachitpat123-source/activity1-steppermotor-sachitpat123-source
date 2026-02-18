from machine import Pin
import time

dhruv = Pin(23, Pin.OUT)
ansh = Pin(22, Pin.OUT)
tanay = Pin(19, Pin.OUT)
avyukt = Pin(18, Pin.OUT)
x=[[0,1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]]

for i in range (0,1000,1):
    for i in x:
        dhruv.value(i[0])
        ansh.value(i[1])
        tanay.value(i[2])
        avyukt.value(i[3])
        time.sleep(0.003)
        
        dhruv.value(0)
        ansh.value(0)
        tanay.value(0)
        avyukt.value(0)

        
