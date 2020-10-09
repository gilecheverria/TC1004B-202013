/*
   Program to test the basics of memory use in Arduino

   - This program is loaded into the Flash memory
   - The global variables, as well as the stack for function calls will use
        the SRAM during execution
   - The EEPROM can be used to store persistent values that won't be lost
        even if the device is powered down

NOTE: EEPROM has a finite lifetime of about 100,000 write cycles,
    so be careful to use only when necessary

   Gilberto Echeverria
   09/10/2020
 */

// Library required to read and write to EEPROM
#include <EEPROM.h>

// Example of definint a constant value
// The name of the constant should be in all uppercases
#define WAIT 100

// Global variables accessible in any function
int wait = 1000;
int value = 0;
int eeAddress = 0;

void setup()
{
    // Configure the serial port to print debug messages
    Serial.begin(9600);
    // Configure the led pin
    pinMode(LED_BUILTIN, OUTPUT);

    // Read from the EEPROM
    EEPROM.get(eeAddress, value);
    Serial.print("Current value in EEPROM: ");
    Serial.println(value);
    // Initialize the wait
    if (value > 0)
        wait = value;
}

void loop()
{
    // Turn the led on and off. The delay will be increasing
    digitalWrite(LED_BUILTIN, HIGH);
    delay(wait); // Wait for 1000 millisecond(s)
    digitalWrite(LED_BUILTIN, LOW);
    delay(wait); // Wait for 1000 millisecond(s)

    // Update the delay
    wait += 500;
    Serial.println(wait);

    // Store the value, so next time it will start from where it left
    EEPROM.put(eeAddress, wait);
    // Test that the value is being stored correctly
    EEPROM.get(eeAddress, value);
    Serial.print("New value in EEPROM: ");
    Serial.println(value);
}
