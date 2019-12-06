#include "SoftwareSerial.h"
SoftwareSerial serial_connection(0, 1);

int in1 = 11; //motor A forward when set to high
int in2 = 10; //motor A backward when set to high

int in3 = 9; //motor B forward when set to high
int in4 = 6; //motor B backward when set to high

int data; //initilizing variables
int power;

void setup() {
  Serial.begin(9600); //sets connection up on 9600 freq
  serial_connection.begin(9600); //starts connection
  pinMode(in1, OUTPUT); //sets up tbe pin modes
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);

}

void loop() {


  data = Serial.read(); //reads the recieved data
  power = 110;
  //below are movement commands based on what the arduino recieves
  //the numbers are the ascii values of what was sent from computer
  if(data == 49){//forward
       analogWrite(in1, HIGH);
       analogWrite(in3, HIGH);
       analogWrite(in2, power);
       analogWrite(in4, power);
  }else if(data == 50){//right

       analogWrite(in1, HIGH);
       analogWrite(in3, HIGH);
       analogWrite(in2, 200);
       analogWrite(in4, 50);
       
  }else if(data == 51){//back
       analogWrite(in2, HIGH);
       analogWrite(in4, HIGH);
       analogWrite(in1, power);
       analogWrite(in3, power);
       
  }else if(data == 52){//left

       analogWrite(in1, HIGH);
       analogWrite(in3, HIGH);
       analogWrite(in2, 10);
       analogWrite(in4, 200);
  }else if(data == 53){
       analogWrite(in2, LOW);//stop
       analogWrite(in4, LOW);
       analogWrite(in1, LOW);
       analogWrite(in3, LOW);
  }else if(data == 54){
       analogWrite(in1, HIGH);//hard right
       analogWrite(in4, HIGH);
       analogWrite(in2, 110);
       analogWrite(in3, 60);
  }else if(data == 55){
       analogWrite(in2, HIGH);//hard left
       analogWrite(in3, HIGH);
       analogWrite(in1, 110);
       analogWrite(in4, 60);
  }else if(data == 56){
       analogWrite(in1, HIGH);//full forward
       analogWrite(in3, HIGH);
       analogWrite(in2, 255);
       analogWrite(in4, 255);
  }else if(data == 57){
       analogWrite(in2, HIGH);//full backward
       analogWrite(in4, HIGH);
       analogWrite(in1, 255);
       analogWrite(in3, 255);
  }else if(data == 58){//back right
       analogWrite(in2, HIGH);
       analogWrite(in4, HIGH);
       analogWrite(in1, 250);
       analogWrite(in3, 5);
  }else if(data == 59){//back left
       analogWrite(in2, HIGH);
       analogWrite(in4, HIGH);
       analogWrite(in1, 5);
       analogWrite(in3, 250);
  }
}
