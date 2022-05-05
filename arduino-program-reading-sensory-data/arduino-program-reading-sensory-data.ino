#include "DHT.h" // DHT - Digital Humidity Temp Sensor

DHT dht(2,DHT11); 
// creating an object, data pin of DHT is with Pin2


void setup() {
  // configure your hardware
  dht.begin(); 
  // it will start transmitting data
  Serial.begin(9600); 
  // debugging monitor with a speed of 9600bps (BaudRate)

}

void loop() {
  // put your main code here, to run repeatedly:
 float hum;
 float temp;
 hum=dht.readHumidity();
 temp=dht.readTemperature();

 Serial.print("Hum: ");
 Serial.print(hum); // %
 Serial.print(", Temp: ");
 Serial.println(temp); // oC
 delay(2000); // 2 seconds of delay
 
}
