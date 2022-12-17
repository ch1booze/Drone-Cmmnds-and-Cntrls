// Basic demo for configuring the MCP4728 4-Channel 12-bit I2C DAC
#include <Adafruit_MCP4728.h>
#include <Wire.h>

Adafruit_MCP4728 mcp;
int analogPin = 4;
    
  float mcp.setChannelValue(MCP4728_CHANNEL_A, 0);// channel a is throttle
  float mcp.setChannelValue(MCP4728_CHANNEL_B, 0);// channel b is yaw
  float mcp.setChannelValue(MCP4728_CHANNEL_C, 0);// channel c is pitch
  float mcp.setChannelValue(MCP4728_CHANNEL_D, 0);// channel d is roll
  int ToBegin=0; //setup time for the drone
void setup(void) {
  Serial.begin(115200);
  while (!Serial)
    delay(10); // will pause, etc until serial console opens
    
 
}

 // Serial reader
      // Interpreter
      // Mapping input voltage from bits to a range of 0 -200
         int controlLevel =analogRead(analogPin);
       for (int x=0; x<4096; x++) {
        int y = map(x, 0, 4096, 0, 200);

void loop(){
  // at the start, throttle=0, yaw=1.7v, pitch=1.7v, roll=1.7v (1.7v is the middle value => position zero
  // This means that no motion is required 
 // if (Tobegin=0){
    int mcp.setChannelValue(MCP4728_CHANNEL_A, 0);
    int mcp.setChannelValue(MCP4728_CHANNEL_B, 68);
    int mcp.setChannelValue(MCP4728_CHANNEL_C, 68);
    int mcp.setChannelValue(MCP4728_CHANNEL_D, 68);
       Serial.print("y = map(x, 0, 1024, 0, 11): x = ");
    Serial.print(x);
    Serial.print(", y = ");
    Serial.println(y)

     mcp.setChannelValue(MCP4728_CHANNEL_A, y<132);
     mcp.setChannelValue(MCP4728_CHANNEL_B,  y<132);
     mcp.setChannelValue(MCP4728_CHANNEL_C,  y<132);
     mcp.setChannelValue(MCP4728_CHANNEL_D,  y<132);

    // Tobegin=1;
 // }
  //=============================================================================
  //if (Serial.available()>0){
     
    // Ready to work state!
  //  for (int y; 
 // mcp.setChannelValue(MCP4728_CHANNEL_A, y<132);
 // mcp.setChannelValue(MCP4728_CHANNEL_B, 0);
//  mcp.setChannelValue(MCP4728_CHANNEL_C, 0);
//  mcp.setChannelValue(MCP4728_CHANNEL_D, 0);