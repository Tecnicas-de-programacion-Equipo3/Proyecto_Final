#include <OneWire.h>
#include <DallasTemperature.h>
int led_1 = 13;
int led_2 = 12;
int led_3 = 11;
int led_4 = 10;
int fan = 9;
int fan_2 = 5;
int sensorPIR = 8;
int garage_motor_up = 7;
int garage_motor_down = 6;
String sensor_reading = "";
String activate_sensor = "False";
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
   pinMode(fan_2, OUTPUT);
   digitalWrite(fan_2, LOW);


   sensors.begin();

   pinMode(sensorPIR, INPUT);

}

void loop(void) {
    if (activate_sensor == "True"){
        sensor_reading = proximitySensor();
        }

    sensors.requestTemperatures();

    sendData(sensor_reading,sensors.getTempCByIndex(0));
  }

void sendData(String proximity_sensor, int temperature_sensor){
  Serial.print("{");
  Serial.print("'ProximitySensor':'");
  Serial.print(proximity_sensor);
  Serial.print("',");
  Serial.print("'TemperatureSensor':");
  Serial.print(temperature_sensor);
  Serial.println("}");
}

String proximitySensor(){
  int readingPIR = digitalRead(sensorPIR);
  if (readingPIR == HIGH){
    delay(1000);
    return "True";
    }
  else{
    delay(1000);
    return "False";
  }
}

void serialEvent() {
    char inChar = (char)Serial.read();

    if (inChar == '1')
    {char state = (char)Serial.read();
    int state_led = state;
    if (state_led == '1') state_led = HIGH;
    else if (state_led == '0') state_led = LOW;
    digitalWrite(led_1, state_led);    }

    if (inChar == '2')
    {char state = (char)Serial.read();
    int state_led = state;
    if (state_led == '1') state_led = HIGH;
    else if (state_led == '0') state_led = LOW;
    digitalWrite(led_2, state_led);    }

    if (inChar == '3')
    {char state = (char)Serial.read();
    int state_led = state;
    if (state_led == '1') state_led = HIGH;
    else if (state_led == '0') state_led = LOW;
    digitalWrite(led_3, state_led);    }

    if (inChar == '4')
    {char state = (char)Serial.read();
    int state_led = state;
    if (state_led == '1') state_led = HIGH;
    else if (state_led == '0') state_led = LOW;
    digitalWrite(led_4, state_led);    }


    if (inChar == '5')
    {char state = (char)Serial.read();
    int state_fan = state;
    if (state_fan == '1') state_fan = HIGH;
    else if (state_fan == '0') state_fan = LOW;
    digitalWrite(fan, state_fan);    }

    if (inChar == '6')
    {char state = (char)Serial.read();
    int state_fan = state;
    if (state_fan == '1') state_fan = HIGH;
    else if (state_fan == '0') state_fan = LOW;
    digitalWrite(fan_2, state_fan);    }


    if (inChar == '7'){
    digitalWrite(garage_motor_down,HIGH);
    delay(350);
    digitalWrite(garage_motor_down,LOW);
    }
    if (inChar == '8') {
    digitalWrite(garage_motor_down,HIGH);
    delay(400);
    digitalWrite(garage_motor_down,LOW);
    }

    if (inChar == 'T')
        activate_sensor = "True";
    if (inChar == 'F')
        activate_sensor = "False";
    
}

