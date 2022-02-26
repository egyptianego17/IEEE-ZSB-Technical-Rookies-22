#define trigger 9
#define echo 8
int t=0, distance=0;
void setup() {
  
Serial.begin(9600);
pinMode(trigger,OUTPUT);
pinMode(echo,INPUT);

}

void loop() {

digitalWrite(trigger,LOW);
delay(10);
digitalWrite(trigger,HIGH);
delay(10);
digitalWrite(trigger,LOW);
t = pulseIn(echo,HIGH);
distance = t * 0.0173565;
Serial.println(distance);
if ( distance < 10 )
{
  Serial.println("too close");
}
if ( distance >= 10 )
{
  Serial.println("safe");
}
delay(1000);
}
