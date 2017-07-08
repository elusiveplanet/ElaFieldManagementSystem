/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.

  Most Arduinos have an on-board LED you can control. On the UNO, MEGA and ZERO 
  it is attached to digital pin 13, on MKR1000 on pin 6. pin is set to
  the correct LED pin independent of which board is used.
  If you want to know what pin the on-board LED is connected to on your Arduino model, check
  the Technical Specs of your board  at https://www.arduino.cc/en/Main/Products
  
  This example code is in the public domain.

  modified 8 May 2014
  by Scott Fitzgerald
  
  modified 2 Sep 2016
  by Arturo Guadalupi
  
  modified 8 Sep 2016
  by Colby Newman
*/

#include <Wire.h> // Enable this line if using Arduino Uno, Mega, etc.
#include <Adafruit_GFX.h>
#include "Adafruit_LEDBackpack.h"

Adafruit_7segment matrix = Adafruit_7segment();

int greenPin = 46;
int yellowPin = 48;
int buzzerPin = 50;
int redPin = 52;
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

void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:

}
