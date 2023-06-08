#include <Adafruit_Fingerprint.h>

Adafruit_Fingerprint finger = Adafruit_Fingerprint(&Serial2);
int mode = 3;
uint8_t p;
void login()
{
  if (finger.verifyPassword())
  {
    Serial.println("Found fingerprint sensor!");
  }
  else
  {
    Serial.println("Did not find fingerprint sensor :(");
    while (1)
    {
      delay(1);
    }
  }
}

bool setUpForSensor(int mode)
{

  while (p != FINGERPRINT_OK)
  {
    p = finger.getImage();
    if (p == FINGERPRINT_OK)
    {
      Serial.println("Image taken");
      break;
    }
    else if (p == FINGERPRINT_NOFINGER)
    {
      Serial.println("No finger detected");
      delay(500);
    }
    else if (p == FINGERPRINT_PACKETRECIEVEERR)
    {
      Serial.println("Communication error");
      return false;
    }
    else if (p == FINGERPRINT_IMAGEFAIL)
    {
      Serial.println("Imaging error");
      return false;
    }
    else
    {
      Serial.println("Unknown error");
      return false;
    }
  }
  // OK success!
  if (mode == 1)
    p = finger.image2Tz(1);
  else if (mode == 2)
    p = finger.image2Tz(2);
  else
    p = finger.image2Tz();
  if (p == FINGERPRINT_OK)
  {
    Serial.println("Image converted");
    return true;
  }
  else if (p == FINGERPRINT_IMAGEMESS)
  {
    Serial.println("Image too messy");
    return false;
  }
  else if (p == FINGERPRINT_PACKETRECIEVEERR)
  {
    Serial.println("Communication error");
    return false;
  }
  else if (p == FINGERPRINT_FEATUREFAIL)
  {
    Serial.println("Could not find fingerprint features");
    return false;
  }
  else if (p == FINGERPRINT_INVALIDIMAGE)
  {
    Serial.println("Could not find fingerprint features");
    return false;
  }
  else
  {
    Serial.println("Unknown error");
    return false;
  }
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

uint8_t deleteFingerprint()
{
  p = -1;
  uint8_t id = 0;
  Serial.println("Ready to delete a fingerprint!");
  Serial.println("Please type in the ID # (from 1 to 127) you want to delete this finger as...");

  while (id == 0)
  { // ID #0 not allowed, try again!
    id = Serial.parseInt();
  }
  Serial.print("Deleting ID #");
  Serial.println(id);
  p = finger.deleteModel(id);



  if (p == FINGERPRINT_OK)
  {
    Serial.println("Deleted!");
    Serial.print("Sensor contains ");
    Serial.print(finger.templateCount);
    Serial.println(" templates");
  }
  else if (p == FINGERPRINT_PACKETRECIEVEERR)
  {
    Serial.println("Communication error");
  }
  else if (p == FINGERPRINT_BADLOCATION)
  {
    Serial.println("Could not delete in that location");
  }
  else if (p == FINGERPRINT_FLASHERR)
  {
    Serial.println("Error writing to flash");
  }
  else
  {
    Serial.print("Unknown error: 0x");
    Serial.println(p, HEX);
  }

  return p;
}

uint8_t getFingerprintID()
{
  if (!setUpForSensor(0))
    return p;
  // OK converted!
  p = finger.fingerSearch();
  if (p == FINGERPRINT_OK)
  {
    Serial.println("Found a print match!");
  }
  else if (p == FINGERPRINT_PACKETRECIEVEERR)
  {
    Serial.println("Communication error");
    return p;
  }
  else if (p == FINGERPRINT_NOTFOUND)
  {
    Serial.println("Did not find a match");
    return p;
  }
  else
  {
    Serial.println("Unknown error");
    return p;
  }
  // found a match!
  Serial.print("Found ID #");
  Serial.print(finger.fingerID);
  Serial.print(" with confidence of ");
  Serial.println(finger.confidence);

  return finger.fingerID;
}

uint8_t getFingerprintEnroll()
{
  uint8_t id = 0;
  Serial.println("Ready to enroll a fingerprint!");
  Serial.println("Please type in the ID # (from 1 to 127) you want to save this finger as...");

  while (id == 0)
  { // ID #0 not allowed, try again!
    id = Serial.parseInt();
  }
  Serial.print("Enrolling ID #");
  Serial.println(id);

  Serial.print("Waiting for valid finger to enroll as #");
  Serial.println(id);
  p = -1;
  if (!setUpForSensor(1))
    return p;

  Serial.println("Remove finger");
  delay(2000);
  p = 0;
  while (p != FINGERPRINT_NOFINGER)
  {
    p = finger.getImage();
  }
  Serial.print("ID ");
  Serial.println(id);
  p = -1;
  Serial.println("Place same finger again");

  if (!setUpForSensor(2))
    return p;

  // OK converted!
  Serial.print("Creating model for #");
  Serial.println(id);

  p = finger.createModel();
  if (p == FINGERPRINT_OK)
  {
    Serial.println("Prints matched!");
  }
  else if (p == FINGERPRINT_PACKETRECIEVEERR)
  {
    Serial.println("Communication error");
    return p;
  }
  else if (p == FINGERPRINT_ENROLLMISMATCH)
  {
    Serial.println("Fingerprints did not match");
    return p;
  }
  else
  {
    Serial.println("Unknown error");
    return p;
  }

  Serial.print("ID ");
  Serial.println(id);
  p = finger.storeModel(id);
  if (p == FINGERPRINT_OK)
  {
    Serial.println("Stored!");
  }
  else if (p == FINGERPRINT_PACKETRECIEVEERR)
  {
    Serial.println("Communication error");
    return p;
  }
  else if (p == FINGERPRINT_BADLOCATION)
  {
    Serial.println("Could not store in that location");
    return p;
  }
  else if (p == FINGERPRINT_FLASHERR)
  {
    Serial.println("Error writing to flash");
    return p;
  }
  else
  {
    Serial.println("Unknown error");
    return p;
  }

  return true;
}

void setup()
{
  Serial.begin(9600);
  Serial.println("\n\nAdafruit finger detect test");
  // set the data rate for the sensor serial port
  finger.begin(57600);
  delay(5);
  login();
  infoDetails();
}

void loop() // run over and over again
{
  if (mode == 0)
    getFingerprintID();
  else if (mode == 1)
  {
    while (!getFingerprintEnroll())
    {
      ;
    }
  }
  else if (mode == 3)
  {
    deleteFingerprint();
  }

  delay(50); // don't ned to run this at full speed.
}
