from machine import Pin
import time

dhruv = Pin(23, Pin.OUT)
ansh = Pin(22, Pin.OUT)
tanay = Pin(19, Pin.OUT)
avyukt = Pin(18, Pin.OUT)
x=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

while True:
    for i in range(0,501,1):
        for i in x:
            dhruv.value(i[0])
            ansh.value(i[1])
            tanay.value(i[2])
            avyukt.value(i[3])
            time.sleep(0.003)


    for i in range(501,1001,1):
        for i in reversed(x):
            dhruv.value(i[0])
            ansh.value(i[1])
            tanay.value(i[2])
            avyukt.value(i[3])
            time.sleep(0.003)

    
