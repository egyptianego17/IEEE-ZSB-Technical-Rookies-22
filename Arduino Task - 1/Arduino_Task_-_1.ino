#define m1_1 5
#define m1_2 4
#define m1_s 6
#define m2_s 3
#define m2_1 2
#define m2_2 1
void setup() {
pinMode(1,OUTPUT);
pinMode(2,OUTPUT);
pinMode(3,OUTPUT);
pinMode(4,OUTPUT);
pinMode(5,OUTPUT);
pinMode(6,OUTPUT);
}
void loop() {
digitalWrite(m1_1,LOW);
digitalWrite(m1_2,HIGH);
analogWrite(m1_s,100);
digitalWrite(m2_1,LOW);
digitalWrite(m2_2,HIGH);
analogWrite(m2_s,100);
}
