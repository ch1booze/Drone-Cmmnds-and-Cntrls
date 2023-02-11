#include "Wire.h"
#include "MCP4725.h"

MCP4725 MCP(0x62);  // 0x62 or 0x63

#define MCP4725_ADDRESS 0x60  // DAC address (depends on the wiring)

const int arraySize = 4;
int arr[arraySize];
int channel = 0;
int max_voltage_level = 33;

void setup() {
  Serial.begin(9600);
  Wire.begin();  // Initialize the I2C bus
}

// Function to write the voltage to the DAC
void writeVoltage(int voltage) {
  int dacValue = (voltage / max_voltage_level) * 4095;
  byte highByte = dacValue >> 4;
  byte lowByte = dacValue << 4;
  Wire.beginTransmission(MCP4725_ADDRESS);
  Wire.write(0x40);      // write to the DAC register
  Wire.write(highByte);  // write the high byte
  Wire.write(lowByte);   // write the low byte
  Wire.endTransmission();
}

void loop() {
  // if (Serial.available() >= 4) {
  //   for (int i = 0; i < arraySize; i++) {
  //     int incoming = Serial.read();
  //     int value = incoming - 127;
  //     int voltage_level = map(incoming, 0, 255, 0, max_voltage_level);

  //     if (i == channel) {
  //       writeVoltage(voltage_level);
  //     }
  //   }
  // }

  // TEST FOR I2C COMMUNICATION BETWEEN ARDUINO AND MCP4725

  for (int i = 0; i < 255; i += 20) {
    int voltage_level = map(i, 0, 255, 0, max_voltage_level);
    Serial.println(i);
    writeVoltage(voltage_level);
    delay(1500);
  }
}
