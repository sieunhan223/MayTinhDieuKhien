#include <Adafruit_Fingerprint.h>
#include <Servo.h>

#define SERVO 12

Servo servo;
int pos;
int curPos;

Adafruit_Fingerprint finger = Adafruit_Fingerprint(&Serial2);
int id, statusDoor = 0;
char dataInput, mode = 'd';
String dataOutput = "0 0";
uint8_t p;

void login()
{
  if (!finger.verifyPassword())
  {
    // Serial.println("Found fingerprint sensor!");
    delay(100);
    ESP.restart();
  }
}

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

bool setUpForSensor(int mode)
{

  while (p != FINGERPRINT_OK)
  {
    p = finger.getImage();
    if (p == FINGERPRINT_OK)
      break;
    else if (p == FINGERPRINT_NOFINGER)
      delay(500);
    else
      return false;
  }
  // OK success!
  if (mode == 1)
    p = finger.image2Tz(1);
  else if (mode == 2)
    p = finger.image2Tz(2);
  else
    p = finger.image2Tz();
  if (p == FINGERPRINT_OK)
    return true;
  else
    return false;
}

void infoDetails()
{
  Serial.println(F("Reading sensor parameters"));
  finger.getParameters();
  Serial.print(F("Status: 0x"));
  Serial.println(finger.status_reg, HEX);
  Serial.print(F("Sys ID: 0x"));
  Serial.println(finger.system_id, HEX);
  Serial.print(F("Capacity: "));
  Serial.println(finger.capacity);
  Serial.print(F("Security level: "));
  Serial.println(finger.security_level);
  Serial.print(F("Device address: "));
  Serial.println(finger.device_addr, HEX);
  Serial.print(F("Packet len: "));
  Serial.println(finger.packet_len);
  Serial.print(F("Baud rate: "));
  Serial.println(finger.baud_rate);
  finger.getTemplateCount();

  if (finger.templateCount == 0)
  {
    Serial.print("Sensor doesn't contain any fingerprint data. Please run the 'enroll' example.");
  }
  else
  {
    Serial.println("Waiting for valid finger...");
    Serial.print("Sensor contains ");
    Serial.print(finger.templateCount);
    Serial.println(" templates");
  }
}

bool deleteFingerprint()
{
  p = -1;

  while (id == 0)
  { // ID #0 not allowed, try again!
    id = Serial.readStringUntil('\n').toInt();
  }

  if (id >= 51)
  {
    delay(1000);
    ESP.restart();
  }

  p = finger.deleteModel(id);

  id = 0;
  if (p == FINGERPRINT_OK)
    return true;
  return false;
}

bool getFingerprintID()
{
  if (!setUpForSensor(0))
    return false;
  p = finger.fingerSearch();
  if (p != FINGERPRINT_OK)
    return false;
  statusDoor++;
  return true;
}

bool getFingerprintEnroll()
{

  while (id == 0)
  { // ID #0 not allowed, try again!
    id = Serial.readStringUntil('\n').toInt();
    Serial.print(id);
  }

  if (id >= 51)
  {
    delay(1000);
    ESP.restart();
  }

  p = -1;
  if (!setUpForSensor(1))
    return false;

  delay(2000);
  p = 0;
  while (p != FINGERPRINT_NOFINGER)
    p = finger.getImage();
  p = -1;

  if (!setUpForSensor(2))
    return false;

  p = finger.createModel();
  if (p != FINGERPRINT_OK)
    return false;

  p = finger.storeModel(id);

  if (p != FINGERPRINT_OK)
    return false;
  id = 0;
  return true;
}

void setup()
{
  Serial.begin(9600);
  // set the data rate for the sensor serial port
  finger.begin(57600);
  // Init Servo in 15PIN:
  servo.attach(SERVO);
  delay(5);
  Serial.println();
  login();
  // infoDetails();
}

void loop() // run over and over again
{

  if (Serial.available() > 0)
  {
    delay(1000);
    dataInput = Serial.read();
    if ((dataInput == 'r') || (dataInput == 'a') || (dataInput == 'd'))
      mode = dataInput;
    delay(1000);
  }

  if (mode == 'd')
  {
    if (getFingerprintID())
    {

      dataOutput = String(finger.fingerID) + " ";
      (statusDoor % 2 == 0) ? dataOutput += "0" : dataOutput += "1";
      Serial.println(dataOutput);
      if (statusDoor % 2 == 0)
        controlServo("OFF");
      else
        controlServo("ON");
    }
  }

  else if (mode == 'a')
  {
    if (getFingerprintEnroll())
    {
      Serial.println("1");
    }
    else
      Serial.println("0");
  }
  else if (mode == 'r')
  {
    if (deleteFingerprint())
    {
      Serial.println("1");
    }
    else
      Serial.println("0");
  }

  delay(50); // don't ned to run this at full speed.
}