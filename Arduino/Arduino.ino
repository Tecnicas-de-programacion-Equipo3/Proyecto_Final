int led_1 = 13;
int state1 = 0;

void setup() {
   Serial.begin(115200);
   
   pinMode(led_1, OUTPUT);
   digitalWrite(led_1, LOW);

}

void loop() { }

void serialEvent() {
    char inChar = (char)Serial.read();
    if (inChar == '1') state1 = HIGH;
    if (inChar == 'a') state1 = LOW;
    digitalWrite(led_1, state1);     
    
}
