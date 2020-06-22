#define REDPIN 5
#define GREENPIN 6
#define BLUEPIN 3
#define TDTPIN 9

void setup() {
  pinMode(REDPIN, OUTPUT);
  pinMode(GREENPIN, OUTPUT);
  pinMode(BLUEPIN, OUTPUT);
  pinMode(TDTPIN, OUTPUT);
}

int count=0;
int frequency=40; //Unit: Hz, it should be over 1 Hz.
int treatment_time=10; //Unit: sec.
int count_limit=treatment_time*frequency;
int trigger_time=100; //Unit: msec.

int number_subexp=10; //(Number_subexp) times ON/OFF
int number_subexp_count=0;

void loop() {
  while(number_subexp_count<number_subexp) {
    analogWrite(TDTPIN, 0); //TDT trigger ON to mark START time
    //delay(trigger_time);
    //analogWrite(TDTPIN, 0); //TDT trigger 0.5 sec
    
    while(count<count_limit){
      analogWrite(REDPIN, 0);
      analogWrite(GREENPIN, 255); //GREEN LED ON
      analogWrite(BLUEPIN, 0);
      //analogWrite(TDTPIN, 255);
    
      delay(500/frequency); //(1000 ms / 2)/frequency of LED lighting
    
      analogWrite(REDPIN, 0);
      analogWrite(GREENPIN, 0); //GREEN LED OFF
      analogWrite(BLUEPIN, 0);
      //analogWrite(TDTPIN, 0); 
    
      delay(500/frequency); //(1000 ms / 2)/frequency of LED lighting
      count++;
    }
  
    //analogWrite(TDTPIN, 255); //TDT trigger ON to mark END time
    //delay(trigger_time);
    analogWrite(TDTPIN, 255); //TDT trigger 0.5 sec

    delay(treatment_time*1000);

    count=0; //counter reset
    number_subexp_count++;
  }
}
