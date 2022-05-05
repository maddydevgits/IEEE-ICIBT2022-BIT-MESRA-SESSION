import serial
import time
import paho.mqtt.client as mqttpub

client=mqttpub.Client()
client.connect('broker.hivemq.com',1883)
print('Broker Connected')
ser=serial.Serial('COM3',9600,timeout=0.5)

while True:
    if(ser.inWaiting()>0): # if dht sensory data is available
        t=ser.readline()
        t=t.decode('utf-8')
        t=t.split(' ')
        hum=t[1][:-1]
        temp=t[-1][:-2]
        print(hum,temp)
        k={}
        k['hum']=hum
        k['temp']=temp
        client.publish('iot/icibt',str(k))
        print('Data Sent to Broker')

        time.sleep(1)