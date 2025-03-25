int sens = 4;

void setup() {
  pinMode(sens,INPUT);
  Serial.begin(9600);
}

void loop() { 
  if(digitalRead(sens) == 0)
  {
    Serial.println(millis());
    delay(100);
  }
}