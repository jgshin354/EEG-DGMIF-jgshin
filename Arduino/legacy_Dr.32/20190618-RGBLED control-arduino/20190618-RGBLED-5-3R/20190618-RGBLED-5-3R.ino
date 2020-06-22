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
