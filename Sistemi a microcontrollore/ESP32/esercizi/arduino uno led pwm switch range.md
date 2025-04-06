//https://wokwi.com/arduino/projects/324373633606615635

const int buttonPin1 = 2;
const int buttonPin2 = 3;
const int ledPin =  13;
const int ledLight =  8;

int buttonState1 = 0;
int previousMillis1  = 0;
int currentMillis1   = 0;

int buttonState2 = 0;
int previousMillis2  = 0;
int currentMillis2   = 0;

int luce = 0;

void setup()
{
  Serial.begin(9600);

  pinMode(ledPin, OUTPUT);
  pinMode(ledLight, OUTPUT);
  pinMode(buttonPin1, INPUT);
  pinMode(buttonPin2, INPUT);

}

void loop()
{

  buttonState1 = digitalRead(buttonPin1);
  if (buttonState1 == HIGH  )
  {
    digitalWrite(ledPin, HIGH);

    currentMillis1  = millis();
    //Serial.println(currentMillis1 - previousMillis1);
    //luce = luce + 1;
    delay(200);

    int var = currentMillis1 - previousMillis1;
    switch (var)
    {
      case 0 ... 100  :
        luce = luce + 1;
        break;
      case 101 ... 200  :
        luce = luce + 5;
        break;
      case 201 ... 500  :
        luce = luce + 10;
        break;
      default:
        luce = luce + 20;
        break;
    }
  }
  else
  {
    digitalWrite(ledPin, LOW);
    previousMillis1 = millis();
  }




  buttonState2 = digitalRead(buttonPin2);
  if (buttonState2 == HIGH)
  {
    digitalWrite(ledPin, HIGH);

    currentMillis2  = millis();
    //Serial.println(currentMillis2 - previousMillis2);
    //luce = luce - 1;
    delay(200);

    int var = currentMillis1 - previousMillis1;
    switch (var)
    {
      case 0 ... 100  :
        luce = luce - 1;
        break;
      case 101 ... 200  :
        luce = luce - 5;
        break;
      case 201 ... 500  :
        luce = luce - 10;
        break;
      default:
        luce = luce - 20;
        break;
    }
  }
  else
  {
    digitalWrite(ledPin, LOW);
    previousMillis2 = millis();
  }


  if (luce > 254) luce = 255;
  if (luce < 1) luce = 0;

  Serial.println(luce);
  analogWrite(ledLight, luce);


}
