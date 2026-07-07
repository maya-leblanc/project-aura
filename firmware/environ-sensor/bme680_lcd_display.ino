
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include "Adafruit_BME680.h"
#include <LiquidCrystal_I2C.h>

// Define BME680 pins for SPI communication (if used, but not required for I2C)
#define BME_SCK 13
#define BME_MISO 12
#define BME_MOSI 11
#define BME_CS 10

// Define the standard sea-level pressure in hPa
#define SEALEVELPRESSURE_HPA (1013.25)

// Create an instance of the BME680 sensor (using I2C communication)
Adafruit_BME680 bme;

// Create an instance of the LCD with I2C address 0x27, 20 columns, and 4 rows
LiquidCrystal_I2C lcd(0x27, 20, 4);

void setup() {
  // Initialize serial communication for debugging
  Serial.begin(9600);
  Serial.println(F("BME680 test"));

  // Initialize the BME680 sensor
  if (!bme.begin()) {
    Serial.println("Could not find a valid BME680 sensor, check wiring!");
    lcd.print("Sensor Error!"); // Display error message on the LCD
    while (1); // Halt execution if sensor initialization fails
  }

  // Configure BME680 settings for temperature, humidity, pressure, and gas measurements
  bme.setTemperatureOversampling(BME680_OS_8X);
  bme.setHumidityOversampling(BME680_OS_2X);
  bme.setPressureOversampling(BME680_OS_4X);
  bme.setIIRFilterSize(BME680_FILTER_SIZE_3);
  bme.setGasHeater(320, 150); // Set gas sensor heater to 320°C for 150 ms

  // Initialize the LCD
  lcd.init();
  lcd.backlight(); // Turn on the LCD backlight

  // Print static labels on the LCD for sensor data
  lcd.setCursor(0, 0); // Line 1: Temperature
  lcd.print("Temperature: ");
  lcd.setCursor(0, 1); // Line 2: Pressure
  lcd.print("Pressure: ");
  lcd.setCursor(0, 2); // Line 3: Humidity
  lcd.print("Humidity: ");
  lcd.setCursor(0, 3); // Line 4: Gas resistance
  lcd.print("Gas:  ");
}

void loop() {
  // Perform a sensor reading and check for success
  if (!bme.performReading()) {
    Serial.println("Failed to perform reading :(");
    return; // Skip this iteration if the reading fails
  }

  // Update the LCD with the latest sensor values
  lcd.setCursor(12, 0); // Position for temperature value
  lcd.print("       "); // Clear previous value
  lcd.setCursor(12, 0);
  lcd.print(bme.temperature, 1); // Display temperature with one decimal place
  lcd.print("*C");

  lcd.setCursor(9, 1); // Position for pressure value
  lcd.print("       "); // Clear previous value
  lcd.setCursor(9, 1);
  lcd.print(bme.pressure / 100.0, 1); // Convert pressure from Pa to hPa
  lcd.print("hPa");

  lcd.setCursor(9, 2); // Position for humidity value
  lcd.print("       "); // Clear previous value
  lcd.setCursor(9, 2);
  lcd.print(bme.humidity, 1); // Display humidity with one decimal place
  lcd.print("%");

  lcd.setCursor(4, 3); // Position for gas resistance value
  lcd.print("       "); // Clear previous value
  lcd.setCursor(4, 3);
  lcd.print(bme.gas_resistance / 1000.0, 1); // Convert gas resistance from Ohms to kOhms
  lcd.print("kOhm");

  delay(2000); // Wait 2 seconds before the next update
}
