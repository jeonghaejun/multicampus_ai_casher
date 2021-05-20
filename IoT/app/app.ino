void setup() {
  pinMode(D1, OUTPUT);
  digitalWrite(D1, LOW);
  Serial.begin(9600);
}

void loop() {
  int value_ = analogRead(A0);
  Serial.println(value_);
  if(value_ >= 512) {
    digitalWrite(13, HIGH); 
  } else {
    digitalWrite(13, LOW);
  }
  Serial.println(analogRead(A0));
}
