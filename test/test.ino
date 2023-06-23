#include <Servo.h>

static const int servoPin = 12;
char data;
int curPos = 0, pos = 180, temp;
Servo servo;

// Hàm sử dụng servo:
void controlServo(String status)
{
  if (status == "ON")
  {
    for (pos = curPos; pos <= 130; pos++)
    {
      servo.write(pos);
      delay(10);
    }
    curPos = 130;
  }
  else
  {
    for (pos = curPos; pos >= 0; pos--)
    {
      servo.write(pos);
      delay(10);
    }
    curPos = 0;
  }
}

void setup()
{
  Serial.begin(9600);
  servo.attach(servoPin);
}

void loop()
{
  if (Serial.available() > 0)
  {
    data = Serial.read();
    if (data == 'a')
    {
      controlServo("ON");
    }
    else
    {
      controlServo("OFF");
    }
  }
  Serial.println(data);
  delay(50);
}