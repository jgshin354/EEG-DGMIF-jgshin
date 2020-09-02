#define off 0
#define pw 1
#define cw 2
#define REDPIN 5
#define GREENPIN 6
#define BLUEPIN 3
#define FREQPIN 8 //jgshin Add
#define STATEPIN 7 //jgshin Add
#define OPERATEPIN 12 // jgshin ADD
#define TDTPIN0 9
#define TDTPIN1 10 //jgshin Add
#define TDTPIN2 11 //jgshin Add
//0h: LED off
//1h: green PW, 2h: green CW
//3h: red PW,   4h: red CW
//5h: blue PW,  6h: blue CW 


//boolean bRST = false;
boolean bSTATE = false;
boolean bOPERATE = false;
boolean bFREQ = false;
int state_n = 0; // 0: Green, 1: Red, 2: Blue 
int freq_n = 0; // 0: 40Hz, 1: 19Hz, 2: 9Hz, 3: 6Hz
int out_pin = GREENPIN; //Default greenpin
int frequency = 40; //Unit: Hz, it should be over 1 Hz.
int half_period_mil = 1000 / frequency / 2; // (1sec / frequency)
int half_period_micro = (1000000 / frequency / 2) % 1000;
//unsigned long period_half_int = period/2 

//EXPERIMENT PARAMETERS
int active_time = 10; //Unit: sec.
int number_epoc = 10; //(Number_subexp) times ON/OFF
int resting_time = 120; //Unit: sec.

//TEST PARAMETERS
//int active_time = 1; //Unit: sec.
//int number_epoc = 3; //(Number_subexp) times ON/OFF
//int resting_time = 3; //Unit: sec.



void setup() {
  pinMode(REDPIN, OUTPUT);
  pinMode(GREENPIN, OUTPUT);
  pinMode(BLUEPIN, OUTPUT);
  pinMode(TDTPIN0, OUTPUT);
  pinMode(TDTPIN1, OUTPUT);
  pinMode(TDTPIN2, OUTPUT);
  pinMode(FREQPIN, INPUT);
  pinMode(STATEPIN, INPUT);
  pinMode(OPERATEPIN, INPUT);
  digitalWrite(REDPIN, LOW);
  digitalWrite(GREENPIN, LOW);
  digitalWrite(BLUEPIN, LOW);
}


void loop() {
  if(digitalRead(STATEPIN) == HIGH){
    if(bSTATE == false){
      bSTATE = true;
      state_n = (state_n + 1) % 3;
      stateRef();
    }
  }
  else{
    bSTATE = false;
  }
  
  if(digitalRead(OPERATEPIN) == HIGH){
    if(bOPERATE == false){
      bOPERATE = true;
      operationCode();
    }
  }
  else{
    bOPERATE = false;
  }

  if(digitalRead(FREQPIN) == HIGH){
    if(bFREQ == false){
      bFREQ = true;
      freq_n = (freq_n + 1) % 4;
      freqRef();
    }
  }
  else{
    bFREQ = false;
  }  
}


void freqRef(){
  switch(freq_n){ // 0: 40Hz, 1: 19Hz, 2: 9Hz, 3: 6Hz
    case 0: frequency = 40; half_period_mil = (1000/frequency)/2;  half_period_micro = (1000000 / frequency / 2) % 1000; break;
    case 1: frequency = 19; half_period_mil = (1000/frequency)/2; half_period_micro = (1000000 / frequency / 2) % 1000; break;
    case 2: frequency = 9; half_period_mil = (1000/frequency)/2; half_period_micro = (1000000 / frequency / 2) % 1000; break;
    case 3: frequency = 6; half_period_mil = (1000/frequency)/2; half_period_micro = (1000000 / frequency / 2) % 1000; break;
    default: frequency = 40; half_period_mil = (1000/frequency)/2; half_period_micro = (1000000 / frequency / 2) % 1000; break;
  }


  for (int i = 0; i < freq_n+1 ; i++) {
      digitalWrite(REDPIN, HIGH);
      digitalWrite(GREENPIN, HIGH);
      digitalWrite(BLUEPIN, HIGH); 
      delay(100);
      digitalWrite(REDPIN, LOW);
      digitalWrite(GREENPIN, LOW);
      digitalWrite(BLUEPIN, LOW);
      delay(100);
  }  
  
}

void operationCode(){ 
  pwOp();
  resting();
  cwOp();
  resting();
  endRef();
}


void pwOp(){
  for(int epoc_i = 0; epoc_i < number_epoc; epoc_i++){
    prtOut(pw);
    for(int count = 0 ; count < active_time*frequency; count++){
        digitalWrite(out_pin,HIGH);
        delay(half_period_mil);
        delayMicroseconds(half_period_micro);
        digitalWrite(out_pin,LOW);
        delay(half_period_mil);
        delayMicroseconds(half_period_micro);
    }
    prtOut(off);
    delay(active_time * 1000);
  }
}

void cwOp(){ 
  for(int epoc_i = 0; epoc_i < number_epoc; epoc_i++){
    prtOut(cw);
    digitalWrite(out_pin, HIGH);
    delay(active_time*1000);
    prtOut(off);
    digitalWrite(out_pin, LOW);
    delay(active_time*1000);
  }
}

void resting(){
  delay(resting_time*1000);
}


void prtOut(int state){
  if(state == pw){
    switch(state_n){
      case 0: digitalWrite(TDTPIN2, LOW); digitalWrite(TDTPIN1, LOW); digitalWrite(TDTPIN0, HIGH); break; //1h: green PW
      case 1: digitalWrite(TDTPIN2, LOW); digitalWrite(TDTPIN1, HIGH); digitalWrite(TDTPIN0, HIGH); break; //3h: red PW
      case 2: digitalWrite(TDTPIN2, HIGH); digitalWrite(TDTPIN1, LOW); digitalWrite(TDTPIN0, HIGH); break; //5h: blue PW
      default:digitalWrite(TDTPIN2, LOW); digitalWrite(TDTPIN1, LOW); digitalWrite(TDTPIN0, HIGH);  break; //1h: green PW
    }
  }
  else if (state == cw){
    switch(state_n){
      case 0: digitalWrite(TDTPIN2, LOW); digitalWrite(TDTPIN1, HIGH); digitalWrite(TDTPIN0, LOW); break; //2h: green PW
      case 1: digitalWrite(TDTPIN2, HIGH); digitalWrite(TDTPIN1, LOW); digitalWrite(TDTPIN0, LOW); break; //4h: red PW
      case 2: digitalWrite(TDTPIN2, HIGH); digitalWrite(TDTPIN1, HIGH); digitalWrite(TDTPIN0, LOW); break; //6h: blue PW
      default:digitalWrite(TDTPIN2, LOW); digitalWrite(TDTPIN1, HIGH); digitalWrite(TDTPIN0, LOW);  break; //2h: green PW
    }
  }

  else if (state == off){
    digitalWrite(TDTPIN2, LOW); digitalWrite(TDTPIN1, LOW); digitalWrite(TDTPIN0, LOW); //0h: LED off
  }

}

void stateRef(){
  switch(state_n){
    case 0: out_pin = GREENPIN;  break;
    case 1: out_pin = REDPIN;    break;
    case 2: out_pin = BLUEPIN;   break;
    default:out_pin = GREENPIN;  break;
  }
  

  for (int i = 0; i < 3; i++) {
    digitalWrite(out_pin, HIGH);
    delay(100);
    digitalWrite(out_pin, LOW);
    delay(100);
  }

}


void endRef(){
    for (int i = 0; i < 5; i++) {
      digitalWrite(REDPIN, HIGH);
      digitalWrite(GREENPIN, HIGH);
      digitalWrite(BLUEPIN, HIGH); 
      delay(1000);
      digitalWrite(REDPIN, LOW);
      digitalWrite(GREENPIN, LOW);
      digitalWrite(BLUEPIN, LOW);
      delay(500);
    }
}



/*
void stateRef()
{  
  if(state_n == 0){     //green blinking
    for (int i = 0; i < 3; i++) {
      digitalWrite(GREENPIN, HIGH);
      delay(100);
      digitalWrite(GREENPIN, LOW);
      delay(100);
    }
  }
  else if(state_n ==1){ //red blinking
    for (int i = 0; i < 4; i++) {
      digitalWrite(REDPIN, HIGH);
      delay(100);
      digitalWrite(REDPIN, LOW);
      delay(100);
    }
  }
  else if(state_n ==2){ //blue blinking
    for (int i = 0; i < 4; i++) {
      digitalWrite(BLUEPIN, HIGH);
      delay(100);
      digitalWrite(BLUEPIN, LOW);
      delay(100);
    }
  }
}
void endRef()
{
  if(state_n == 0){     //green blinking
    for (int i = 0; i < 5; i++) {
      digitalWrite(GREENPIN, HIGH);
      delay(500);
      digitalWrite(GREENPIN, LOW);
      delay(500);
    }
  }
  else if(state_n ==1){ //red blinking
    for (int i = 0; i < 5; i++) {
      digitalWrite(REDPIN, HIGH);
      delay(500);
      digitalWrite(REDPIN, LOW);
      delay(500);
    }
  }
  else if(state_n ==2){ //blue blinking
    for (int i = 0; i < 5; i++) {
      digitalWrite(BLUEPIN, HIGH);
      delay(500);
      digitalWrite(BLUEPIN, LOW);
      delay(500);
    }
  }
}
*/
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
