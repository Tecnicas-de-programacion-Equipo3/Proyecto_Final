
#include <OneWire.h> 
#include <DallasTemperature.h>


int led_1 = 13;
int led_2 = 12;
int led_3 = 11;
int led_4 = 10;
int fan = 9;
int state_led_1 = 0;
int state_led_2 = 0;
int state_led_3 = 0;
int state_led_4 = 0;
int state_fan = 0;
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

   pinMode(fan, OUTPUT);
   digitalWrite(fan, LOW);
   sensors.begin(); 
   

}

void loop(void) { 
  
  sensors.requestTemperatures();
  Serial.print(sensors.getTempCByIndex(0));
  Serial.print("\n"); 
  }

void serialEvent() {
    char inChar = (char)Serial.read();
    if (inChar == '1') state_led_1 = HIGH;
    if (inChar == 'a') state_led_1 = LOW;
    digitalWrite(led_1, state_led_1);    
     
    if (inChar == '2') state_led_2 = HIGH;
    if (inChar == 'b') state_led_2 = LOW;
    digitalWrite(led_2, state_led_2); 
    
    if (inChar == '3') state_led_3 = HIGH;
    if (inChar == 'c') state_led_3 = LOW;
    digitalWrite(led_3, state_led_3); 
    
    if (inChar == '4') state_led_4 = HIGH;
    if (inChar == 'd') state_led_4 = LOW;
    digitalWrite(led_4, state_led_4); 

    if (inChar == '5') state_fan = HIGH;
    if (inChar == 'e') state_fan = LOW;
    digitalWrite(fan, state_fan); 

    
}
