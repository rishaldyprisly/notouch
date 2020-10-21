int val = 0;

void setup() {
  Serial.begin(115200);
  pinMode(15, INPUT);
  // put your setup code here, to run once:

}

void loop() {

  val = digitalRead(15);
  
  if (val == 1 ) {
    Serial.println("Touch");
    delay(500);
  }
  else {
    Serial.println("None");
    delay(500);
  }
}
