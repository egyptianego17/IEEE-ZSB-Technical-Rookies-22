#include <SoftwareSerial.h>
#define mr_s 5
#define ml_s 6
#define mr_1 7
#define mr_2 2
#define ml_1 3
#define ml_2 4
char order = 'S';

SoftwareSerial HC05(1,0);

void setup() {
  pinMode(7,OUTPUT);
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(0,INPUT);
  pinMode(1,OUTPUT);
  analogWrite(mr_s,0);
  analogWrite(ml_s,0);
  Serial.begin(9600);
  HC05.begin(9600);
}

void loop() {

  if ( Serial.available() ){
    order = Serial.read();
  if ( order == 'F' )
  {
    analogWrite(mr_s,175);
    analogWrite(ml_s,175);
    digitalWrite(mr_1,HIGH);
    digitalWrite(mr_2,LOW);
    digitalWrite(ml_1,HIGH);
    digitalWrite(ml_2,LOW);

  }
  delay(100);
  if ( order == 'R' )
  {
    analogWrite(mr_s,175);  
    analogWrite(ml_s,175);
    digitalWrite(mr_1,HIGH);
    digitalWrite(mr_2,LOW);
    digitalWrite(ml_1,LOW);
    digitalWrite(ml_2,HIGH); 

  }
  delay(100);
  if ( order == 'L' )
  {
    analogWrite(mr_s,175);
    analogWrite(ml_s,175);
    digitalWrite(mr_1,LOW);
    digitalWrite(mr_2,HIGH);
    digitalWrite(ml_1,HIGH);
    digitalWrite(ml_2,LOW);
  }
  delay(100);
  if ( order == 'S' )
  {
    analogWrite(mr_s,0);
    analogWrite(ml_s,0);
    digitalWrite(mr_1,LOW);
    digitalWrite(mr_2,LOW);
    digitalWrite(ml_1,LOW);
    digitalWrite(ml_2,LOW);
  }
  delay(100);
  if (order == 'B')
  {
    analogWrite(mr_s,175);
    analogWrite(ml_s,175);
    digitalWrite(mr_1,LOW);
    digitalWrite(mr_2,HIGH);
    digitalWrite(ml_1,LOW);
    digitalWrite(ml_2,HIGH);
  }
  else
  {
    analogWrite(mr_s,0);
    analogWrite(ml_s,0);
    digitalWrite(mr_1,LOW);
    digitalWrite(mr_2,LOW);
    digitalWrite(ml_1,LOW);
    digitalWrite(ml_2,LOW);
  }
}
delay(100);
}
