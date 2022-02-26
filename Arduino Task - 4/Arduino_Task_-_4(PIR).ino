int detector;
void setup() {
pinMode(13,OUTPUT);
pinMode(0,INPUT);
pinMode(1,OUTPUT);
Serial.begin(9600);
}
void loop() {
  detector = digitalRead(13);
  if  ( detector == 1 )
  {
    Serial.println("human are detected");
  }
  delay(500);
}
