#include <Dabble.h>
#include <Servo.h>
#include <NewPing.h>
#include <Wire.h>
#include <VL6180X.h>

// Constants, defines, and object declarations
#pragma region Defines
// Motor encoder pins
const int eraPin = 2;
const int elaPin = 3;

// Ultrasonic pins
const int fultEchoPin = 26;
const int fultTrigPin = 28;
const int rultEchoPin = 27;
const int rultTrigPin = 29;

// Motor Pins
const int rDirPin = 41;
const int lDirPin = 42;
const int rPwmPin = 45;
const int lPwmPin = 46;
const int ledModePin = 50;

// Define dabble names
#define INCLUDE_TERMINAL_MODULE
#define INCLUDE_GAMEPAD_MODULE
#define CUSTOM_SETTINGS

// Define Motor directions for current configuration
#define MFORWARD LOW
#define MREVERSE HIGH

// Initiate  time of flight sensor
VL6180X sensor;
double lSensor;

// Initiate Ultrasonic sensor
#define MAX_DISTANCE 50
NewPing sonarRight(rultTrigPin, rultEchoPin, MAX_DISTANCE);
NewPing sonarFront(fultTrigPin, fultEchoPin, MAX_DISTANCE);
double rSensor;
double fSensor;

// Declare encoder variables
volatile long eraCount = 0;
volatile long elaCount = 0;
unsigned long distCountR = 0;
int countMax = 650;

// PID setup
double scaleKp = 0.50;     //0.45
double scaleKd = 5.0;      //5.0;
double desiredPWM = 140.0; //110.0;
double kp = scaleKp * (desiredPWM / 11.0);
double ki = 0.0;
double kd = scaleKd * kp; //scaleKd * kp;
double P = 0.0;
double I = 0.0;
double D = 0.0;
double lastError = 0.0;
double error = 0.0;
double increment = 0.0;
double outputR;
double outputL;
unsigned long currTime = 0;
unsigned long lastTime = 0;

// Maze start variables
bool solveMaze = false;
bool solveMazeFast = false;

// maze following targets
double rThreshold = 20.0;
double rTarget = 8.0;
double fThreshold = 12.0; //10.0
double lThreshold = 30.0;
double lTarget = 11.0;

// Identifiers
#define LEFT true
#define RIGHT false

#pragma endregion Defines

// Main setup routine
#pragma region Setup
void setup()
{
    // Attempt to connect to Serial monitor. Wait until successful
    Serial.begin(115200);
    while (!Serial)
    {
    }
    Serial.println("Connection made to Serial Port");

    // Connect to Dabble for iPhone control
    Dabble.begin(9600);

    // Set pinmodes to inpt/output
    initPinMode();

    // Set up time of flight sensor
    initTOF();

    // Set up interrupts
    initEncoder();
}
#pragma endregion Setup

// Main Loop
#pragma region MainLoop
void loop()
{
    // Check dabble for new input and reset encoders to prevent over flow
    Dabble.processInput();
    eraCount = 0;
    elaCount = 0;

    // Main looping logic
    if (GamePad.isCrossPressed())
    {
        // Stop the motors
        stop();

        // Stop navigating the maze
        solveMaze = false;
        solveMazeFast = false;
        fThreshold = 12.0;
        desiredPWM = 140.0;
        kp = scaleKp * (desiredPWM / 11.0);
        kd = scaleKd * kp; //scaleKd * kp;
        digitalWrite(ledModePin, LOW);
        delay(100);
    }
    else if (GamePad.isStartPressed())
    {
        solveMaze = true;
        solveMazeFast = false;
        fThreshold = 12.0;
        desiredPWM = 140.0;
        kp = scaleKp * (desiredPWM / 11.0);
        kd = scaleKd * kp; //scaleKd * kp;
        digitalWrite(ledModePin, LOW);
        delay(100);
    }
    else if (GamePad.isTrianglePressed())
    {
        solveMaze = false;
        solveMazeFast = true;
        fThreshold = 13.0;
        desiredPWM = 160.0;
        kp = scaleKp * (desiredPWM / 11.0);
        kd = scaleKd * kp; //scaleKd * kp;
        digitalWrite(ledModePin, HIGH);
        delay(100);
    }
    else if (solveMaze)
    {
        Navigate();
    }
    else if (solveMazeFast)
    {
        NavigateFast();
    }
}
#pragma endregion MainLoop

// Functions and algorithms
#pragma region Functions

void Navigate()
{
    ReadSensors();
    // priority 1: turn left if left wall open
    //      - 1. left wall gone, doesnt see front wall
    //      - 2. left wall gone, sees front wall
    // priority 2: drive straight if possible
    //      - 3. sees left wall and doesnt see front wall
    // priority 3: turn right if no other options
    //      - 4. sees left wall, sees front wall, doesnt see right wall
    // priority 4: turn around
    //      - 5. sees left, front, and right wall

    // Case 1
    if (fSensor > fThreshold && lSensor > lThreshold)
    {
        avoidCorner(RIGHT);
        left();
        passEdge(RIGHT);
    }
    // Case 2
    else if (fSensor < fThreshold && lSensor > lThreshold)
    {
        left();
        passEdge(RIGHT);
    }
    // Case 3
    else if (fSensor > fThreshold && lSensor < lThreshold)
    {
        drive(LEFT);
    }
    // Case 4
    else if (fSensor < fThreshold && lSensor < lThreshold && rSensor > rThreshold)
    {
        right();
        passEdge(LEFT);
    }
    // Case 5
    else if (fSensor < fThreshold && lSensor < lThreshold && rSensor < rThreshold)
    {
        while (fSensor < fThreshold)
        {
            ReadSensors();
            analogWrite(rPwmPin, desiredPWM);
            digitalWrite(rDirPin, MREVERSE);
            analogWrite(lPwmPin, desiredPWM);
            digitalWrite(lDirPin, MFORWARD);
            delay(50);
            stop();
            ReadSensors();
        }
    }
}

void NavigateFast()
{
    ReadSensors();
    // priority 1: turn left if left wall open
    //      - 1. left wall gone, doesnt see front wall
    //      - 2. left wall gone, sees front wall
    // priority 2: drive straight if possible
    //      - 3. sees left wall and doesnt see front wall
    // priority 3: turn right if no other options
    //      - 4. sees left wall, sees front wall, doesnt see right wall
    // priority 4: turn around
    //      - 5. sees left, front, and right wall

    // Case 1
    if (fSensor > fThreshold && lSensor > lThreshold)
    {
        avoidCorner(RIGHT);
        left();
        passEdge(RIGHT);
    }
    // Case 2
    else if (fSensor < fThreshold && lSensor > lThreshold)
    {
        left();
        passEdge(RIGHT);
    }
    // Case 3
    else if (fSensor > fThreshold && lSensor < lThreshold)
    {
        drive(LEFT);
    }
    // Case 4
    else if (fSensor < fThreshold && lSensor < lThreshold && rSensor > rThreshold)
    {
        right();
        passEdge(LEFT);
    }
    // Case 5
    else if (fSensor < fThreshold && lSensor < lThreshold && rSensor < rThreshold)
    {
        while (fSensor < fThreshold)
        {
            // ReadSensors();
            analogWrite(rPwmPin, desiredPWM);
            digitalWrite(rDirPin, MREVERSE);
            analogWrite(lPwmPin, desiredPWM);
            digitalWrite(lDirPin, MFORWARD);
            delay(20);
            stop();
            ReadSensors();
        }
    }
}

void drive(bool left)
{
    // Compute input and output values
    if (left)
    {
        lComputePD();
    }
    else
    {
        rComputePD();
    }

    ReadSensors();
    // PD control of robot
    if (outputR < 0)
    {
        analogWrite(rPwmPin, abs(outputR));
        digitalWrite(rDirPin, MREVERSE);
        analogWrite(lPwmPin, outputL);
        digitalWrite(lDirPin, MFORWARD);
    }
    else if (outputL < 0)
    {
        analogWrite(rPwmPin, outputR);
        digitalWrite(rDirPin, MFORWARD);
        analogWrite(lPwmPin, abs(outputL));
        digitalWrite(lDirPin, MREVERSE);
    }
    else
    {
        analogWrite(rPwmPin, outputR);
        digitalWrite(rDirPin, MFORWARD);
        analogWrite(lPwmPin, outputL);
        digitalWrite(lDirPin, MFORWARD);
    }
}

void left()
{
    stop();
    delay(10);

    distCountR = eraCount;
    while (eraCount - distCountR < (320))
    {
        analogWrite(rPwmPin, desiredPWM);
        digitalWrite(rDirPin, MFORWARD);
        analogWrite(lPwmPin, desiredPWM);
        digitalWrite(lDirPin, MREVERSE);
    }
}

void right()
{
    stop();
    delay(100);

    distCountR = eraCount;
    while (eraCount - distCountR < (320))
    {
        analogWrite(rPwmPin, desiredPWM);
        digitalWrite(rDirPin, MREVERSE);
        analogWrite(lPwmPin, desiredPWM);
        digitalWrite(lDirPin, MFORWARD);
    }
}

void turnAround()
{
    stop();
    delay(100);

    distCountR = eraCount;
    while (eraCount - distCountR < countMax)
    {
        analogWrite(rPwmPin, desiredPWM);
        digitalWrite(rDirPin, MREVERSE);
        analogWrite(lPwmPin, desiredPWM);
        digitalWrite(lDirPin, MFORWARD);
    }
    stop();
    delay(100);
}

void avoidCorner(bool sensor)
{
    stop();
    delay(100);

    distCountR = eraCount;
    while (eraCount - distCountR < 500)
    {
        drive(sensor);
    }
}

void passEdge(bool sensor)
{
    stop();
    delay(100);

    distCountR = eraCount;
    while (eraCount - distCountR < 1000 && fSensor > fThreshold)
    {
        drive(sensor);
    }
    stop();
}

void stop()
{
    analogWrite(rPwmPin, 0);
    analogWrite(lPwmPin, 0);
    lastTime = millis();
}

#pragma endregion Functions

// Sensors and controls
#pragma region Sensors
// Read ultrasonic sensor and Time of flight
void ReadSensors()
{
    // Use NewPing library to find the distance
    fSensor = sonarFront.ping_cm();
    rSensor = sonarRight.ping_cm();

    // Take small readings and set them to high for front sensor
    if (rSensor <= 1.0)
    {
        rSensor = 50.0;
    }

    // Take small readings and set them to high for right sensor
    if (fSensor <= 1.0)
    {
        fSensor = 50.0;
    }

    // Read the time of flight sensor on the left
    if (rangeDataReady())
    {
        lSensor = readRangeNonBlockingMillimeters() / 10.0;
    }
}

void lComputePD()
{
    // Compute error for the left time of flight sensor
    error = lSensor - 11.0;

    currTime = millis();
    P = kp * error;
    //I += ki * error * ((currTime - lastTime) / 1000);
    D = kd * (error - lastError);

    if (I > 5)
    {
        I = 5;
    }

    lastTime = currTime;
    lastError = error;

    increment = P + I + D;

    outputR = desiredPWM + increment;
    outputL = desiredPWM - increment;

    outputR = constrain(outputR, -255, 255);
    outputL = constrain(outputL, -255, 255);
}

void rComputePD()
{
    // Compute error for the left time of flight sensor
    error = rTarget - rSensor;

    currTime = millis();
    P = 1.5 * kp * error;
    //I += ki * error * ((currTime - lastTime) / 1000);
    D = 2 * kd * (error - lastError);

    if (I > 5)
    {
        I = 5;
    }

    lastTime = currTime;
    lastError = error;

    increment = P + I + D;

    outputR = desiredPWM + increment;
    outputL = desiredPWM - increment;

    outputR = constrain(outputR, -255, 255);
    outputL = constrain(outputL, -255, 255);
}

bool rangeDataReady()
{
    return ((sensor.readReg(VL6180X::RESULT__INTERRUPT_STATUS_GPIO) & 0x04) != 0);
}

uint8_t readRangeNonBlocking()
{
    uint8_t range = sensor.readReg(VL6180X::RESULT__RANGE_VAL);
    sensor.writeReg(VL6180X::SYSTEM__INTERRUPT_CLEAR, 0x01);

    return range;
}

uint8_t readRangeNonBlockingMillimeters()
{
    return readRangeNonBlocking() * sensor.getScaling();
}

void eraTriggered()
{
    eraCount++;
}

void elaTriggered()
{
    elaCount++;
}
#pragma endregion Sensors

// Initializer functions
#pragma region Initializers
// Initialize pins for input/output
void initPinMode()
{
    // Set pin modes for ultrasonics
    pinMode(rultTrigPin, OUTPUT);
    pinMode(rultEchoPin, INPUT);
    pinMode(fultTrigPin, OUTPUT);
    pinMode(fultEchoPin, INPUT);

    // Set pin modes
    pinMode(lDirPin, OUTPUT);
    pinMode(rDirPin, OUTPUT);
    pinMode(lPwmPin, OUTPUT);
    pinMode(rPwmPin, OUTPUT);
    pinMode(ledModePin, OUTPUT);
    pinMode(LED_BUILTIN, OUTPUT);

    // Turn LED off by default
    digitalWrite(LED_BUILTIN, LOW);
    digitalWrite(ledModePin, LOW);
}

// Set up time of flight sensor
void initTOF()
{
    // Initiate the Wire library and join the I2C bus as a master or slave.
    //  his should normally be called only once.  If not argument is passed
    // then is join the bus as master.
    Wire.begin();
    // Join the wire library as a master
    sensor.init();
    // Reset time out period so the sensor will abort if not ready
    sensor.configureDefault();
    sensor.setTimeout(500);
    // Stop continuous mode if already active
    sensor.stopContinuous();
    // Reduce range max convergence time and ALS integration
    // time to 30 ms and 50 ms, respectively, to allow 10 Hz
    // operation (as suggested by Table 6 ("Interleaved mode
    // limits (10 Hz operation)") in the datasheet). 
    sensor.writeReg(VL6180X::SYSRANGE__MAX_CONVERGENCE_TIME, 30);
    sensor.writeReg16Bit(VL6180X::SYSALS__INTEGRATION_PERIOD, 50);
    sensor.setTimeout(500);
    // stop continuous mode if already active
    sensor.stopContinuous();
    // in case stopContinuous() triggered a single-shot
    // measurement, wait for it to complete
    delay(300);
    // Connect to GPIO1
    sensor.writeReg(VL6180X::SYSTEM__MODE_GPIO1, 0x10);
    // Clear any existing interrupts
    sensor.writeReg(VL6180X::SYSTEM__INTERRUPT_CLEAR, 0x03);
    // Start interleaved continuous mode with period of 100 ms
    sensor.startRangeContinuous(100);
}

// Initialize ela and era pins and interrupts
void initEncoder()
{
    // Initialize pins as pullup so they don't float
    pinMode(eraPin, INPUT_PULLUP);
    pinMode(elaPin, INPUT_PULLUP);

    // Attach interupts to corresponding encoder pins
    attachInterrupt(digitalPinToInterrupt(eraPin), eraTriggered, CHANGE);
    attachInterrupt(digitalPinToInterrupt(elaPin), elaTriggered, CHANGE);
}
#pragma endregion Initializers