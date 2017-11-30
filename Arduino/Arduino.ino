#include <OneWire.h>
#include <DallasTemperature.h>
int led_1 = 13;
int led_2 = 12;
int led_3 = 11;
int led_4 = 10;
int fan = 9;
int sensorPIR = 8;
int garage_motor_up = 7;
int garage_motor_down = 6;
int state_led_1 = 0;
int state_led_2 = 0;
int state_led_3 = 0;
int state_led_4 = 0;
int state_fan = 0;
String sensor_reading = "";
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
   pinMode(garage_motor_up,OUTPUT);
   digitalWrite(garage_motor_up,LOW);
   pinMode(garage_motor_down, OUTPUT);
   digitalWrite(garage_motor_down,LOW);

   pinMode(fan, OUTPUT);
   digitalWrite(fan, LOW);
   sensors.begin();

   pinMode(sensorPIR, INPUT);

}

void loop(void) { 
  sensor_reading = proximitySensor();

  sensors.requestTemperatures();

  sendData(sensor_reading,sensors.getTempCByIndex(0));
  }

void sendData(String proximity_sensor, int temperature_sensor){
  Serial.print("{");
  Serial.print("ProximitySensor: ");
  Serial.print(proximity_sensor);
  Serial.print(", ");
  Serial.print("TemperatureSensor: ");
  Serial.print(temperature_sensor);
  Serial.println("}");
}

String proximitySensor(){
  int readingPIR = digitalRead(sensorPIR);
  if (readingPIR == HIGH){
    delay(1500);
    return "True";
    }
  else{
    delay(1500);
    return "False";
  }
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

    if (inChar == '7'){
    digitalWrite(garage_motor_down,HIGH);
    delay(10000);
    digitalWrite(garage_motor_down,LOW);
    }
    if (inChar == '8') {
    digitalWrite(garage_motor_up,HIGH);
    delay(10000);
    digitalWrite(garage_motor_up,LOW);
    }

    
}
