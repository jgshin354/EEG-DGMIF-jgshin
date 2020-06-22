#define REDPIN 5
#define GREENPIN 6
#define BLUEPIN 3
//#define RST 2 //jgshin Add
#define STATE 7 //jgshin Add
#define RUN 12 // jgshin ADD
#define TDTPIN0 9
#define TDTPIN1 10 //jgshin Add
#define TDTPIN2 11 //jgshin Add
//0h: LED off
//1h: green PW, 2h: green CW
//3h: red PW,   4h: red CW
//5h: blue PW,  6h: blue CW 

void setup() {
  pinMode(REDPIN, OUTPUT);
  pinMode(GREENPIN, OUTPUT);
  pinMode(BLUEPIN, OUTPUT);
  pinMode(TDTPIN0, OUTPUT);
  pinMode(TDTPIN1, OUTPUT);
  pinMode(TDTPIN2, OUTPUT);
//  pinMode(RST, INPUT);
  pinMode(STATE, INPUT);
  pinMode(STATE, INPUT);

  digitalWrite(REDPIN, LOW);
  digitalWrite(GREENPIN, LOW);
  digitalWrite(BLUEPIN, LOW);
}

//boolean bRST = false;
boolean bSTATE = false;
int state_n = 0; // 0: Green, 1: Red, 2: Blue 

void loop() {

  if(digitalRead(bSTATE) = HIGH){
    if(bSTATE = false){
      bSTATE = true;
      state_n = (state_n + 1) % 3;
      stateRef()
    }
  }
  else{
    bSTATE = false;
  }


}


void stateRef()
{
  if(state_n == 0){     //green blinking
    for (int i = 0; i < 3; i++) {
      digitalWrite(GREENPIN, HIGH)
      delay(125)
      digitalWrite(GREENPIN, LOW)
      delay(125)
    }
  }
  else if(state_n ==1){ //red blinking
    for (int i = 0; i < 4; i++) {
      digitalWrite(REDPIN, HIGH)
      delay(125)
      digitalWrite(REDPIN, LOW)
      delay(125)
    }
  }
  else if(state_n ==2){ //blue blinking
    for (int i = 0; i < 4; i++) {
      digitalWrite(BLUEPIN, HIGH)
      delay(125)
      digitalWrite(BLUEPIN, LOW)
      delay(125)
    }
  }
  
  
}


/*
int count=0;
int frequency=40; //Unit: Hz, it should be over 1 Hz.
int treatment_time=10; //Unit: sec.
int count_limit=treatment_time*frequency;
int trigger_time=500; //Unit: msec.

int number_subexp=10; //(Number_subexp) times ON/OFF
int number_subexp_count=0;




void loop() {
  while(number_subexp_count<number_subexp) {
    analogWrite(TDTPIN, 0); //TDT trigger ON to mark START time
    //delay(trigger_time);
    //analogWrite(TDTPIN, 0); //TDT trigger 0.5 sec

    analogWrite(REDPIN, 255); //Red LED ON
    analogWrite(GREENPIN, 0); 
    analogWrite(BLUEPIN, 0);

    delay(treatment_time*1000);

    analogWrite(REDPIN, 0); //Red LED OFF
    analogWrite(GREENPIN, 0);
    analogWrite(BLUEPIN, 0);
      
    //analogWrite(TDTPIN, 255); //TDT trigger ON to mark END time
    //delay(trigger_time);
    analogWrite(TDTPIN, 255); //TDT trigger 0.5 sec

    delay(treatment_time*1000);

    count=0; //counter reset
    number_subexp_count++;
  }
}
*/
