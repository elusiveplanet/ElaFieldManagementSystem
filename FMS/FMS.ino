#include <Wire.h> // Enable this line if using Arduino Uno, Mega, etc.
#include <Adafruit_GFX.h>
#include "Adafruit_LEDBackpack.h"

Adafruit_7segment matrix = Adafruit_7segment();

int greenPin = 4;
int yellowPin = 5;
int buzzerPin = 6;
int redPin = 7;
int timeLeft = 120;
boolean drawDots = false;

// the setup function runs once when you press reset or power the board
void setup() {
  matrix.begin(0x70);

  pinMode(greenPin, OUTPUT);
  pinMode(yellowPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  pinMode(redPin, OUTPUT);
    matrix.println(120);
    matrix.drawColon(true);
    matrix.writeDisplay();
}

// the loop function runs over and over again forever
void loop() {
  tick();
  tick();
  tick();
  tickBeg();
  digitalWrite(greenPin, HIGH);
  digitalWrite(yellowPin, LOW);
  digitalWrite(buzzerPin, LOW);
  digitalWrite(redPin, LOW);
  for (uint16_t counter = 0; counter < 100; counter++){
    matrix.println(timeLeft);
    matrix.writeDisplay();
    delay(1000);
    timeLeft--;
  }
  digitalWrite(greenPin, LOW);
  digitalWrite(yellowPin, HIGH);
  digitalWrite(buzzerPin, HIGH);
  digitalWrite(redPin, LOW);
  delay(500);
  digitalWrite(greenPin, LOW);
  digitalWrite(yellowPin, HIGH);
  digitalWrite(buzzerPin, LOW);
  digitalWrite(redPin, LOW);
  delay(500);
  for (uint16_t counter = 0; counter <= 20; counter++){
    matrix.println(timeLeft);
    matrix.writeDisplay();
    delay(1000);
    timeLeft--;
  }
  digitalWrite(greenPin, LOW);
  digitalWrite(yellowPin, LOW);
  digitalWrite(buzzerPin, HIGH);
  digitalWrite(redPin, HIGH);
  delay(1500);
  digitalWrite(greenPin, LOW);
  digitalWrite(yellowPin, LOW);
  digitalWrite(buzzerPin, LOW);
  digitalWrite(redPin, HIGH);
  while(true);
}

void tick() {
  digitalWrite(greenPin, LOW);
  digitalWrite(yellowPin, LOW);
  digitalWrite(buzzerPin, LOW);
  digitalWrite(redPin, HIGH);
  delay(500);
  digitalWrite(greenPin, LOW);
  digitalWrite(yellowPin, LOW);
  digitalWrite(buzzerPin, HIGH);
  digitalWrite(redPin, LOW);
  delay(500);
}
void tickBeg() {
  digitalWrite(greenPin, LOW);
  digitalWrite(yellowPin, LOW);
  digitalWrite(buzzerPin, LOW);
  digitalWrite(redPin, HIGH);
  delay(500);
  digitalWrite(greenPin, HIGH);
  digitalWrite(yellowPin, LOW);
  digitalWrite(buzzerPin, HIGH);
  digitalWrite(redPin, LOW);
  delay(1000);
}
