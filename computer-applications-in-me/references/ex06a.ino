#include "lcdhelperv2.h"
#include "irhelper.h"
//
// The PIN numbers of the LED pins
//
const int ledPins[4] =  {5,6,7,15}; 
//
//  Setup button pins
//
const int swPins[4] =  {17,18,8,3}; 
//
//  Create an instance of the lcdhelper class named lcd
//
lcdhelper oLCD(ILI9163_4L,3,2,9,10,7);
//
//  Create an instance of irhelper class named oIR.
//
irhelper oIR;
//
//  Speaker pin.
//
const int spkChannel = 1;
const int spkPin = 4;
//
//  Setup bin for master button press
//
const int interruptPin = 21;
//
//  Set variable to control game start
//
volatile bool newGame = false;
//
//  Set sequence count
//
int sequencecount = 0;
//
//  Setup array to hold sequences.
//
int sequences[20];

unsigned short int currentIndex = 0;

void BUTTON_ISR(){
    newGame = true;
}

void ProcessMove(int quadrant){
    // Get width of TFT display in pixels
    int x = oLCD.getViewportWidth();
    // Get height of TFT display in pixels
    int y = oLCD.getViewportHeight();
    // Define a spacer to represent margins and spacing between elements.
    int m=8;
    int w = (x-3*m)/2.0;
    int h = (y-3*m)/2.0;
    // Store colors
    int colors[4] = {RCB_GREEN,RCB_BLUE,RCB_YELLOW,RCB_RED};
    int xCoords[4]={(x+m)/2, (x+m)/2, m, m};
    int yCoords[4]={m, (y+m)/2, (y+m)/2, m};

    blinkLED(ledPins[quadrant],100);
   
    blinkLED(ledPins[quadrant],200);   
    oLCD.fillRect(m, m, x - 2*m, y - 2*m,RCB_PURPLE);
    // Fill a rounded rectangle with a green background.
    oLCD.fillRect(xCoords[quadrant], yCoords[quadrant], w, h,colors[quadrant]);
    ledcWriteTone(spkChannel,100*(quadrant+1)); 
    delay(200);
    ledcWriteTone(spkChannel,0); 
    delay(500);
}
//
//  Implement a function such that returns true if game play should continue.  
//  and returns false if game play should be suspended.  
//	    Accepts a single argument signed short integer argument named userAction.
//
bool ProcessUserSelections(signed short int action){
  if (action == sequences[currentIndex]){
     currentIndex++;
     return true;
  }  
  return false;
}


//
//  Method to display menus on TFT display
//
void ShowDisplay(screen val, char optionstate, char keypressed)
{
    char text[20];
 
    oLCD.LCDInitialize(PORTRAIT,false);
    if (val == SC_MAIN){
        sprintf(text,"WELCOME");
        oLCD.print(text,CENTER,20);
        sprintf(text,"TO");
        oLCD.print(text,CENTER,40);
        sprintf(text,"SIMON SAYS");
        oLCD.print(text,CENTER,60);
    }
    else if (val == SC_SUB1)
    {
        sprintf(text,"NEW GAME");
        oLCD.print(text,CENTER,40);
    }
}
//
//  Blink LED
//
void blinkLED(int pin, int ms){
    digitalWrite(pin,HIGH);
    delay(ms);
    digitalWrite(pin, LOW);
}
//
//  Setup(): Perform initialization
//
void setup()
{
    //  Setup Serial Port
    Serial.begin(115200);  
    while(!Serial){  
    // wait for serial to start  
    } 
    //
    //  Initialize the display
    //
    oLCD.LCDInitialize(PORTRAIT,true);
    // Initialize IR Communications
    oIR.IRInitialize();
    //
    // initialize the LED pina as an output:
    //
    pinMode(ledPins[0], OUTPUT);
    pinMode(ledPins[1], OUTPUT);
    pinMode(ledPins[2], OUTPUT);
    pinMode(ledPins[3], OUTPUT);
    //
    //  Initialize the button pins as input
    //
    pinMode(swPins[0], INPUT_PULLUP);
    pinMode(swPins[1], INPUT_PULLUP);
    pinMode(swPins[2], INPUT_PULLUP);
    pinMode(swPins[3], INPUT_PULLUP);
    //
    //  Initialize the speaker pin as output
    //
    pinMode(spkPin,OUTPUT);
    //  Attach speaker pin to speaker channel
    ledcAttachPin(spkPin, spkChannel);
    //
    //  Set interupt pin to input pullup
    //
    pinMode(interruptPin, INPUT_PULLUP);
    //
    //  Setup interrupt.
    //
    attachInterrupt(digitalPinToInterrupt(interruptPin),BUTTON_ISR,FALLING);  
    // Show main menu when Arduino starts
    // for the 1st time or on reset.
    ShowDisplay(SC_MAIN, ' ', ' ');
}
//
//  Loop(): Implement looping logic.
//
void loop()
{
    signed short int userAction = -1;
    unsigned long last_key_processed;
    // Determine which key was pressed.
    last_key_processed = oIR.GetKeyPressed(1000);
    // Return to the main menu any time the
    // menu key is pressed.
    if (last_key_processed == KEY_MENU)
    {
        ShowDisplay(SC_MAIN, ' ', ' ');
    }

    if (newGame){
        ShowDisplay(SC_SUB1, ' ', ' ');
        delay(1000);
        // Set the current number of sequences.
        sequencecount = 4;
        // Randomly select the initial sequences and display them
        // to the user.
        for (int i= 0; i < sequencecount;i++){
            sequences[i] = random(4);
            ProcessMove(sequences[i]);
        }
        newGame = false;
        currentIndex = 0;
    }
    else{
        if (digitalRead(swPins[0])==LOW){
            ProcessMove(0);
            userAction = 0;
        }
        else  if (digitalRead(swPins[1])==LOW){
            ProcessMove(1);
            userAction = 1;
        }
        else  if (digitalRead(swPins[2])==LOW){
            ProcessMove(2);
            userAction = 2;
        }
        else  if (digitalRead(swPins[3])==LOW){
            ProcessMove(3);
            userAction = 3;
        }
        // If any key was pressed, then process it.
        if (userAction > -1){
            //
            //  Call to ProcessUserSelections goes here.
            //
            // See if current key pressed is the correct key in the sequence.
            if (ProcessUserSelections(userAction)==true){
                // Display the current sequence count to the end user.
                //sprintf(text,"   ");oLCD.print(text,CENTER,80);
                oLCD.printNumI(currentIndex,CENTER,80,2,' ');
            }
            else
            {
                // When an incorrect sequence is enterred, then display message to the user.
                char text[15];
                oLCD.fillScreen(RCB_PURPLE);
                sprintf(text,"  YOU LOSE!  ");oLCD.print(text,CENTER,20);
                sprintf(text,"PRESS BUTTON");oLCD.print(text,CENTER,40);
                sprintf(text,"TO PLAY AGAIN");oLCD.print(text,CENTER,60);
                sprintf(text,"   ");oLCD.print(text,CENTER,80);
                ledcWriteTone(spkChannel,100);
                delay(1000);
                ledcWriteTone(spkChannel,0); 
                // Pause until key is pressed.
                while(digitalRead(interruptPin)==HIGH){}
            }
            userAction = -1;
        }

    }
}




