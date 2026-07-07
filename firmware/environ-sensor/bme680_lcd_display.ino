# bme680_lcd_display

#include <Servo.h>

Servo myServo;
int angle = 0;

void setup() {
  myServo.attach(9);  // Attach servo to pin 9
  Serial.begin(115200);  // Start serial communication
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();  // Read the incoming command
    
    // Assign distinct angles to each command
    if (command == 'DROP') {
      angle = -180;
    } 
    else if (command == 'LIFT') {
      angle = 0;
    } 
    else if (command == 'NEUTRAL') {
      angle = 180;
    } 
    myServo.write(angle);  // Move the servo to the chosen angle
    Serial.print("Moving to: ");
    Serial.println(angle);  // Print the current angle to the serial monitor
  }
}

