import serial
import time
ser=serial.Serial('COM3',9600,timeout=0.5)

while True:
    if(ser.inWaiting()>0): # if dht sensory data is available
        t=ser.readline()
        t=t.decode('utf-8')
        t=t.split(' ')
        hum=t[1][:-1]
        temp=t[-1][:-2]
        print(hum,temp)

        time.sleep(1)