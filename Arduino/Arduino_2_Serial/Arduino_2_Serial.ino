/*
Write a series of random numbers through the serial port

Gilberto Echeverria
23/10/2020
*/

long rand_num;

void setup()
{
    // Initialize the serial port
    Serial.begin(9600);
    // Wait for the port to initialize
    while(!Serial);
    
    // Initialize the random seed
    randomSeed(analogRead(0));
}

void loop()
{
    rand_num = random(1, 101);
    // Write through serial port
    Serial.println(rand_num);
    delay(1500);
}
