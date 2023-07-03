//the code thats working in the ardino

 
#include<stdlib.h>

//M1 M2 left motors
#define M1 3 //forward
#define M2 5 //backward
//M3 M4 right motors
#define M3 6 //forward
#define M4 11 //backward

// //for Ultrasonic sensor
// int trigpin1 = 9;
// int echopin1 = 8;

// int trigpin2 = 13;
// int echopin2 = 12;

// int trigpin3 = 10;
// int echopin3 = 2;

int en1 = 4;
int en2 = 7;

String a,b,c;

float distance, x, y;
void setup()
{
    Serial.begin(9600);

    //   pinMode(trigpin1, OUTPUT);
    //   pinMode(echopin1, INPUT);

    //   pinMode(trigpin2, OUTPUT);
    //   pinMode(echopin2, INPUT);

    pinMode(M1, OUTPUT);
    pinMode(M2, OUTPUT);
    pinMode(M3, OUTPUT);
    pinMode(M4, OUTPUT);

    //pinMode(en1, OUTPUT);
    //pinMode(en2, OUTPUT);
}
void loop()
{
    if (Serial.available()) // checking if we are getting the input from the raspberry pi
    {
        a= Serial.readStringUntil('\n'); // reads the data sent from raspberry pi for the distance
        Serial.println(a);
        distance = atof(a.c_str());
        Serial.read();
        //Serial.println("Distance ",distance);
        b = Serial.readStringUntil('\n');
        x = atof(b.c_str()); // X coordinate of ball
        Serial.read();
        c= Serial.readStringUntil('\n');
        y = atof(c.c_str());

        if (distance > 20)
            {
                //the ring around condition
                if (y<70){
                    ring_around();
                }
                else{
                    
                    if (x > 380 && x < 620)
                    move_right();
                    else if (x < 250 && x > 20)
                    move_left();
                    else if (x >= 250 && x <= 380)
                    move_forward();
                    else if (x >= 620)      //boundary conditions 
                    fast_right();
                    else if (x <= 20)
                    fast_left();
                    
                }

            }
            
            else if (distance <= 20)
            {
                //the ring around condition
                if (y<70){
                    ring_around();
                }
                else{
                    if (x > 620)
                        fast_right;
                    else if (x < 20)
                        fast_left();
                    else
                        chill;
                }
            }
            else{
                chill();
            }
        }

    //Ultrasonic sensor part
    /*long distance1, duration1, distance2, duration2, distance3, duration3;
    digitalWrite(trigpin1, HIGH);
    digitalWrite(trigpin2, HIGH);
    digitalWrite(trigpin3, HIGH);
    delayMicroseconds(100);
    digitalWrite(trigpin1, LOW);
    digitalWrite(trigpin2, LOW);
    digitalWrite(trigpin3, LOW);
    duration1 = pulseIn(echopin1, HIGH);
    distance1 = (duration1 / 2) / 29.1;
    duration2 = pulseIn(echopin2, HIGH);
    distance2 = (duration2 / 2) / 29.1;
    duration3 = pulseIn(echopin3, HIGH);
    distance3 = (duration3 / 2) / 29.1;
    Serial.print(distance1);
    Serial.println("cm");

    long dis = min(distance1, min(distance2, distance3));

    if (dis < 5)      //there is a obstacle
    {   
        // finding which one is the least one 
        if (distance1 < distance2 && distance1 < distance3){
            //if obstacle is in the front
            chill();
        }
        if (distance2 < distance1 && distance2 < distance3){
            //if obstacle is in the front
            move_right();
        }
        if (distance3 < distance1 && distance3 < distance2){
            //if obstacle is in the front
            move_left();
        }

    }*/
}


// functions for the arduino code starts here

void move_forward()
{
    analogWrite(M1, 170);
    analogWrite(M2, 0);
    analogWrite(M3, 170);
    analogWrite(M4, 0);
}

void move_left()
{
    analogWrite(M1, 95);
    analogWrite(M2, 0);
    analogWrite(M3, 195);
    analogWrite(M4, 0);
}

void move_right()
{
    analogWrite(M1, 195);
    analogWrite(M2, 0);
    analogWrite(M3, 95);
    analogWrite(M4, 0);
}
void chill(){
    analogWrite(M1, 0);
    analogWrite(M2, 0);
    analogWrite(M3, 0);
    analogWrite(M4, 0);
}

void ring_around(){
    analogWrite(M1, 0);
    analogWrite(M2, 100);
    analogWrite(M3, 200);
    digitalWrite(M4,0);
}
void fast_left(){
    analogWrite(M1, 70);
    analogWrite(M2, 0);
    analogWrite(M3, 200);
    analogWrite(M4, 0);
    }
void fast_right(){
    analogWrite(M1, 200);
    analogWrite(M2, 0);
    analogWrite(M3, 70);
    analogWrite(M4, 0);

}