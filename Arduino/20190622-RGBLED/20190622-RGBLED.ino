#define REDPIN 5
#define GREENPIN 6
#define BLUEPIN 3
//#define RST 2 //jgshin Add
#define STATE 7 //jgshin Add
#define OPERATE 12 // jgshin ADD
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
  pinMode(OPERATE, INPUT);
  digitalWrite(REDPIN, LOW);
  digitalWrite(GREENPIN, LOW);
  digitalWrite(BLUEPIN, LOW);
}

//boolean bRST = false;
boolean bSTATE = false;
boolean bOPERATE = false;
int state_n = 0; // 0: Green, 1: Red, 2: Blue 
int out_pin = GREENPIN;

int count=0;
int frequency=40; //Unit: Hz, it should be over 1 Hz.
int treatment_time=10; //Unit: sec.
int count_limit=treatment_time*frequency;
int trigger_time=500; //Unit: msec.
int number_subexp=10; //(Number_subexp) times ON/OFF
int number_subexp_count=0;


void loop() {
  if(digitalRead(STATE) == HIGH){
    if(bSTATE == false){
      bSTATE = true;
      state_n = (state_n + 1) % 3;
      stateRef();
    }
  }
  else{
    bSTATE = false;
  }


  if(digitalRead(OPERATE) == HIGH){
    if(bOPERATE == false){
      bOPERATE = true;
      operationCode();
      endRef();
    }
  }
  else{
    bOPERATE = false;
  }
}

void operationCode()
{
}


void stateRef()
{
  switch(state_n){
    case 0: out_pin = GREENPIN;  break;
    case 1: out_pin = REDPIN;    break;
    case 2: out_pin = BLUEPIN;   break;
    default:out_pin = GREENPIN;  break;
  }
  
  if(state_n == 0) {     //green blinking
    for (int i = 0; i < 3; i++) {
      digitalWrite(out_pin, HIGH);
      delay(100);
      digitalWrite(out_pin, LOW);
      delay(100);
    }
  } 
}


void endRef()
{
  if(state_n == 0){     //green blinking
    for (int i = 0; i < 5; i++) {
      digitalWrite(out_pin, HIGH);
      delay(500);
      digitalWrite(out_pin, LOW);
      delay(500);
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
