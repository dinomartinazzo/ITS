``` c
unsigned long  taskTime
void readAnalogSensor(){
  if (millis()<taskTime) return; // time is not expired yet
  taskTime += 50; // set time for the following execution
  // .... more code for the task that is done every 50 ms
}


void readAnalogSensor() {
   if( millis() % 50 != 0 )
       return;
   .
   .  // Do your sensor read and processing here
   .
}
```