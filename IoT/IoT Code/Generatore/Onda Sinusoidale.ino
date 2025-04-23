#define DEFAULT_SAMPLES 100
#define MAX_AMP_V 10.0
#define MAX_FREQ_HZ 2000.0

// Parametri configurabili
unsigned int N_SAMPLES = DEFAULT_SAMPLES;
float ampV = 1.0;
float offsetV = 1.5;
float freqHz = 2.0;

const float Vref = 5;  // tensione massima DAC (logica), NON l'ampiezza limite
unsigned long sampleIntervalMicros;
unsigned long lastSampleTime = 0;

String inputString = "";
bool stringComplete = false;

// Per misurare frequenza reale
unsigned long lastCycleTime = 0;
int i = 0;

void setup() {
  Serial.begin(115200);
  delay(1000);
  recalculateTiming();
  inputString.reserve(20);
  Serial.println("Sinusoide pronta. Comandi: A=amp O=offset F=freq N=n°campioni");
}

void loop() {
  if (stringComplete) {
    parseCommand(inputString);
    inputString = "";
    stringComplete = false;
  }

  unsigned long now = micros();
  if (now - lastSampleTime >= sampleIntervalMicros) {
    lastSampleTime = now;

    float angle = 2.0 * PI * i / N_SAMPLES;
    float voltage = ampV * sin(angle) + offsetV;
    voltage = constrain(voltage, 0.0, Vref); // evita superare il range analogico

    Serial.println(voltage * 1000.0, 3);  // in millivolt con 3 decimali

    i = (i + 1) % N_SAMPLES;

    // Misura della frequenza effettiva ogni ciclo completo
    if (i == 0) {
      unsigned long cycleDuration = micros() - lastCycleTime;
      lastCycleTime = micros();
      float actualFreq = 1000000.0 / cycleDuration;
      Serial.print("#FreqEffettiva: ");
      Serial.print(actualFreq, 3);
      Serial.println(" Hz");
    }
  }
}

void recalculateTiming() {
  sampleIntervalMicros = (1.0 / (freqHz * N_SAMPLES)) * 1e6;
}

void parseCommand(String cmd) {
  char type = cmd.charAt(0);
  float value = cmd.substring(1).toFloat();

  switch (type) {
    case 'A':
      ampV = constrain(value, 0.0, MAX_AMP_V);
      Serial.print("#Ampiezza: "); Serial.println(ampV);
      break;
    case 'O':
      offsetV = constrain(value, 0.0, Vref);
      Serial.print("#Offset: "); Serial.println(offsetV);
      break;
    case 'F':
      freqHz = constrain(value, 0.1, MAX_FREQ_HZ);
      recalculateTiming();
      Serial.print("#Frequenza: "); Serial.println(freqHz);
      break;
    case 'N':
      if (value >= 10 && value <= 2000) {
        N_SAMPLES = (unsigned int)value;
        recalculateTiming();
        Serial.print("#Campioni: "); Serial.println(N_SAMPLES);
      }
      break;
  }
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    if (inChar == '\n') {
      stringComplete = true;
    } else {
      inputString += inChar;
    }
  }
}
