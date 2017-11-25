
#include <OneWire.h> 
#include <DallasTemperature.h>


int led_1 = 13;
int led_2 = 12;
int led_3 = 11;
int led_4 = 10;
int vent = 9;
int state1 = 0;
int state2 = 0;
int state3 = 0;
int state4 = 0;
int state5 = 0;
int Temp = 2;
OneWire oneWire(Temp); 
DallasTemperature sensors(&oneWire);


void setup() {
   Serial.begin(115200);
   
   pinMode(led_1, OUTPUT);
   digitalWrite(led_1, LOW);
   pinMode(led_2, OUTPUT);
   digitalWrite(led_2, LOW);
   pinMode(led_3, OUTPUT);
   digitalWrite(led_3, LOW);
   pinMode(led_4, OUTPUT);
   digitalWrite(led_4, LOW);

   pinMode(vent, OUTPUT);
   digitalWrite(vent, LOW);
   sensors.begin(); 
   

}

void loop(void) { 
  
  sensors.requestTemperatures();
  Serial.print("\n"); 
  Serial.print(sensors.getTempCByIndex(0));
  }

void serialEvent() {
    char inChar = (char)Serial.read();
    if (inChar == '1') state1 = HIGH;
    if (inChar == 'a') state1 = LOW;
    digitalWrite(led_1, state1);    
     
    if (inChar == '2') state2 = HIGH;
    if (inChar == 'b') state2 = LOW;
    digitalWrite(led_2, state2); 
    
    if (inChar == '3') state3 = HIGH;
    if (inChar == 'c') state3 = LOW;
    digitalWrite(led_3, state3); 
    
    if (inChar == '4') state4 = HIGH;
    if (inChar == 'd') state4 = LOW;
    digitalWrite(led_4, state4); 

    if (inChar == '5') state5 = HIGH;
    if (inChar == 'e') state5 = LOW;
    digitalWrite(vent, state5); 

    
}
