#include <Servo.h>
int i;
Servo servo_motor;

void setup() {
  servo_motor.attach(9);
  servo_motor.write(30);
  delay(2000);
}

void loop() {
  for ( i = 31; i <= 90; i = i+1 )
  {
    servo_motor.write(i);
    delay(20);
  }
    for ( i = 89; i >= 30; i = i-1 )
  {
    servo_motor.write(i);
    delay(20);
  }

}
