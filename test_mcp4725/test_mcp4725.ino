
#include "Wire.h"
#include "MCP4725.h"

MCP4725 MCP(0x62); // 0x62 or 0x63

#define MCP4725_ADDRESS 0x60 // DAC address (depends on the wiring)

void setup()
{
  Serial.begin(115200);
  Wire.begin(); // Initialize the I2C bus
}

// Function to write the voltage to the DAC
void writeVoltage(float voltage)
{
  int dacValue = (voltage / 5) * 4095;
  byte highByte = dacValue >> 4;
  byte lowByte = dacValue << 4;
  Wire.beginTransmission(MCP4725_ADDRESS);
  Wire.write(0x40);     // write to the DAC register
  Wire.write(highByte); // write the high byte
  Wire.write(lowByte);  // write the low byte
  Wire.endTransmission();
}

int channel(int channel_number)
{
  while (Serial.available() == 0)
  {
  }

  String commands = Serial.readStringUntil("\r");
  int str_length = commands.length();
  String command_str = commands.substring(0, str_length - 1);

  for (int i = 0; i < 4; i++)
  {
    int check = i * 3;
    String substr = command_str.substring(check, check + 3);
    int value = substr.toInt();

    int channel_value;

    if (i == channel_number)
    {
      channel_value = value;
    }

    return channel_value
  }
}

void loop()
{
  // Example usage: set the output voltage to 2.5V
  //  while Serial.available(){};
  //  Serial.readStringUntil("\r")
  for (int i = 0; i <= 10; i++)
  {
    int channel_number = 0; // 0 for Throttle, 1 for Yaw, 2 for Pitch, 3 for Roll
    int channel_value = channel(channel_number);
    float voltage = map(channel_value, 0, 400, 0, 33);
    writeVoltage(0.1 * voltage);
    delay(5000);
  }
}
