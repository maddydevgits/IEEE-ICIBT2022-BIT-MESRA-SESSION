import serial
import time
ser=serial.Serial('COM3',9600,timeout=0.5)

while True:
    if(ser.inWaiting()>0): # if dht sensory data is available
        t=ser.readline()
        t=t.decode('utf-8')
        print(t)
        time.sleep(1)