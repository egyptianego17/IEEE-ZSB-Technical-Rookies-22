#define mr_s 5
#define ml_s 6
#define mr_1 1
#define mr_2 2
#define ml_1 3
#define ml_2 4
#define r 12
#define l 13
void setup() {
  pinMode(12,INPUT);
  pinMode(13,INPUT);
  pinMode(1,OUTPUT);
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  analogWrite(mr_s,175);
  analogWrite(ml_s,175);
}

void loop() {
  if (digitalRead(r) == LOW and digitalRead(l) == LOW )
  {
    digitalWrite(mr_1,HIGH);
    digitalWrite(mr_2,LOW);
    digitalWrite(ml_1,HIGH);
    digitalWrite(ml_2,LOW);
  }
  if (digitalRead(r) == HIGH and digitalRead(l) == LOW)
  {
    digitalWrite(mr_1,HIGH);
    digitalWrite(mr_2,LOW);
    digitalWrite(ml_1,LOW);
    digitalWrite(ml_2,HIGH); 
  }
  if (digitalRead(r) == LOW and digitalRead(l) == HIGH)
  {
    digitalWrite(mr_1,LOW);
    digitalWrite(mr_2,HIGH);
    digitalWrite(ml_1,HIGH);
    digitalWrite(ml_2,LOW);
  }
  delay(200);
}
