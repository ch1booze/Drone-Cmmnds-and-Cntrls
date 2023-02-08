
#include "Wire.h"
#include "MCP4725.h"

MCP4725 MCP(0x62); // 0x62 or 0x63

#define MCP4725_ADDRESS 0x60 // DAC address (depends on the wiring)

int arr[4];
int channel = 0;

void setup()
{
  Serial.begin(9600);
  Wire.begin(); // Initialize the I2C bus
}

// Function to write the voltage to the DAC
void writeVoltage(int voltage)
{
  int dacValue = (voltage / 33) * 4095;
  byte highByte = dacValue >> 4;
  byte lowByte = dacValue << 4;
  Wire.beginTransmission(MCP4725_ADDRESS);
  Wire.write(0x40);     // write to the DAC register
  Wire.write(highByte); // write the high byte
  Wire.write(lowByte);  // write the low byte
  Wire.endTransmission();
}

void loop()
{
  if (Serial.available() >= 0)
  {
    for (int i = 0; i < arraySize; i++)
    {
      int incoming = Serial.read();
      int voltage_level = map(incoming, 200, 400, 0, 33);

      if (i == channel)
      {
        writeVoltage(voltage_level)
      }
    }
  }
}
