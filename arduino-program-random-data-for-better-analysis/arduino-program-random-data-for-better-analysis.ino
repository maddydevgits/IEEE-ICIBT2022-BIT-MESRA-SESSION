
void setup() {
  // put your setup code here, to run once:
 Serial.begin(9600);
 
}

void loop() {
  float hum,temp;
  hum=random(20,100);
  temp=random(30,40);

  Serial.print("Hum: ");
  Serial.print(hum);
  Serial.print(", temp: ");
  Serial.println(temp);
  delay(2000);

}
