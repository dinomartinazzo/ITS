# FORMULE GEOMETRICHE E CONVERSIONI FISICHE - RIFERIMENTO COMPLETO

> **Guida completa per programmatori, studenti e ingegneri**
> Versione 2.0 - Formato Markdown

---

## 📑 INDICE

### [PARTE 1: FIGURE PIANE (2D)](#parte-1-figure-piane-2d)
- [1.1 Cerchio](#11-cerchio)
- [1.2 Quadrato](#12-quadrato)
- [1.3 Rettangolo](#13-rettangolo)
- [1.4 Triangolo](#14-triangolo)
- [1.5 Trapezio](#15-trapezio)
- [1.6 Rombo](#16-rombo)
- [1.7 Parallelogramma](#17-parallelogramma)
- [1.8 Poligoni Regolari](#18-poligoni-regolari)
- [1.9 Ellisse](#19-ellisse)
- [1.10 Settore Circolare](#110-settore-circolare)
- [1.11 Corona Circolare](#111-corona-circolare)

### [PARTE 2: SOLIDI (3D)](#parte-2-solidi-3d)
- [2.1 Cubo](#21-cubo)
- [2.2 Parallelepipedo Rettangolare](#22-parallelepipedo-rettangolare)
- [2.3 Cilindro](#23-cilindro)
- [2.4 Cono](#24-cono)
- [2.5 Sfera](#25-sfera)
- [2.6 Piramide](#26-piramide)
- [2.7 Prisma](#27-prisma)
- [2.8 Tronco di Cono](#28-tronco-di-cono)
- [2.9 Tronco di Piramide](#29-tronco-di-piramide)
- [2.10 Toro (Ciambella)](#210-toro-ciambella)
- [2.11 Calotta Sferica](#211-calotta-sferica)

### [PARTE 3: CONVERSIONI FISICHE](#parte-3-conversioni-fisiche)
- [3.1 Lunghezza](#31-lunghezza)
- [3.2 Area (Superficie)](#32-area-superficie)
- [3.3 Volume](#33-volume)
- [3.4 Massa/Peso](#34-massapeso)
- [3.5 Temperatura](#35-temperatura)
- [3.6 Tempo](#36-tempo)
- [3.7 Velocità](#37-velocità)
- [3.8 Accelerazione](#38-accelerazione)
- [3.9 Forza](#39-forza)
- [3.10 Pressione](#310-pressione)
- [3.11 Energia/Lavoro](#311-energialavoro)
- [3.12 Potenza](#312-potenza)
- [3.13 Angoli](#313-angoli)
- [3.14 Frequenza](#314-frequenza)
- [3.15 Densità](#315-densità)

### [PARTE 4: SENSORI DI TEMPERATURA - TERMOCOPPIE](#parte-4-sensori-di-temperatura---termocoppie)
- [4.1 Introduzione alle Termocoppie](#41-introduzione-alle-termocoppie)
- [4.2 Tipi di Termocoppie Standard](#42-tipi-di-termocoppie-standard)
- [4.3 Termocoppia Tipo J](#43-termocoppia-tipo-j)
- [4.4 Termocoppia Tipo K](#44-termocoppia-tipo-k)
- [4.5 Termocoppia Tipo S](#45-termocoppia-tipo-s)
- [4.6 Altri Tipi di Termocoppie](#46-altri-tipi-di-termocoppie)
- [4.7 Tabella Comparativa](#47-tabella-comparativa)
- [4.8 Conversione Tensione-Temperatura](#48-conversione-tensione-temperatura)
- [4.9 Compensazione Giunto Freddo](#49-compensazione-giunto-freddo)

### [PARTE 5: COSTANTI FISICHE E MATEMATICHE](#parte-5-costanti-fisiche-e-matematiche)

---

## PARTE 1: FIGURE PIANE (2D)

### 1.1 Cerchio

**Parametri:**
- Raggio: `r`
- Diametro: `d = 2r`

**Formule:**

| Grandezza | Formula |
|-----------|---------|
| **Perimetro (Circonferenza)** | `P = 2πr = πd` |
| **Area** | `A = πr² = πd²/4` |
| **Lunghezza arco** (angolo θ in radianti) | `L = rθ` |
| **Area settore circolare** (angolo θ in radianti) | `A_settore = (r²θ)/2` |

**Esempio in C:**
```c
double perimetro_cerchio(double raggio) {
    return 2.0 * M_PI * raggio;
}

double area_cerchio(double raggio) {
    return M_PI * raggio * raggio;
}
```

---

### 1.2 Quadrato

**Parametri:**
- Lato: `l`

**Formule:**

| Grandezza | Formula |
|-----------|---------|
| **Perimetro** | `P = 4l` |
| **Area** | `A = l²` |
| **Diagonale** | `d = l√2` |
| **Raggio cerchio inscritto** | `r = l/2` |
| **Raggio cerchio circoscritto** | `R = (l√2)/2` |

---

### 1.3 Rettangolo

**Parametri:**
- Base: `b`
- Altezza: `h`

**Formule:**

| Grandezza | Formula |
|-----------|---------|
| **Perimetro** | `P = 2(b + h)` |
| **Area** | `A = b × h` |
| **Diagonale** | `d = √(b² + h²)` |

---

### 1.4 Triangolo

**Parametri:**
- Lati: `a`, `b`, `c`
- Base: `b`
- Altezza: `h`
- Semiperimetro: `s = (a+b+c)/2`

#### Triangolo Generico

| Grandezza | Formula |
|-----------|---------|
| **Perimetro** | `P = a + b + c` |
| **Area (base e altezza)** | `A = (b × h)/2` |
| **Area (Formula di Erone)** | `A = √[s(s-a)(s-b)(s-c)]` dove `s = (a+b+c)/2` |

#### Triangolo Equilatero (lato `l`)

| Grandezza | Formula |
|-----------|---------|
| **Perimetro** | `P = 3l` |
| **Area** | `A = (l²√3)/4` |
| **Altezza** | `h = (l√3)/2` |

#### Triangolo Rettangolo (cateti `a`, `b`; ipotenusa `c`)

| Grandezza | Formula |
|-----------|---------|
| **Teorema di Pitagora** | `c² = a² + b²` |
| **Area** | `A = (a × b)/2` |

---

### 1.5 Trapezio

**Parametri:**
- Base maggiore: `B`
- Base minore: `b`
- Altezza: `h`
- Lati obliqui: `l₁`, `l₂`

**Formule:**

| Grandezza | Formula |
|-----------|---------|
| **Perimetro** | `P = B + b + l₁ + l₂` |
| **Area** | `A = [(B + b) × h]/2` |

**Trapezio Isoscele:**
- Diagonale: `d = √[h² + ((B+b)/2)²]`

---

### 1.6 Rombo

**Parametri:**
- Lato: `l`
- Diagonale maggiore: `D`
- Diagonale minore: `d`

**Formule:**

| Grandezza | Formula |
|-----------|---------|
| **Perimetro** | `P = 4l` |
| **Area (con diagonali)** | `A = (D × d)/2` |
| **Area (con lato e altezza h)** | `A = l × h` |
| **Relazione lato-diagonali** | `l = √[(D/2)² + (d/2)²]` |

---

### 1.7 Parallelogramma

**Parametri:**
- Base: `b`
- Altezza: `h`
- Lato: `l`

**Formule:**

| Grandezza | Formula |
|-----------|---------|
| **Perimetro** | `P = 2(b + l)` |
| **Area** | `A = b × h` |

---

### 1.8 Poligoni Regolari

**Parametri:**
- Numero lati: `n`
- Lato: `l`
- Apotema: `a` (distanza dal centro al centro di un lato)

**Formule:**

| Grandezza | Formula |
|-----------|---------|
| **Perimetro** | `P = n × l` |
| **Area** | `A = (P × a)/2 = (n × l × a)/2` |
| **Angolo interno** | `α = [(n-2) × 180°]/n` |
| **Angolo esterno** | `β = 360°/n` |
| **Apotema (dal lato)** | `a = l/[2 tan(180°/n)]` |

#### Casi Specifici:

**Pentagono Regolare (lato `l`):**
- `A = (l²√25+10√5)/4 ≈ 1.72048 l²`

**Esagono Regolare (lato `l`):**
- `A = (3l²√3)/2 ≈ 2.598 l²`
- `P = 6l`

---

### 1.9 Ellisse

**Parametri:**
- Semiasse maggiore: `a`
- Semiasse minore: `b`

**Formule:**

| Grandezza | Formula |
|-----------|---------|
| **Area** | `A = πab` |
| **Perimetro (approssimazione Ramanujan)** | `P ≈ π[3(a+b) - √((3a+b)(a+3b))]` |

---

### 1.10 Settore Circolare

**Parametri:**
- Raggio: `r`
- Angolo al centro: `θ` (in radianti)

**Formule:**

| Grandezza | Formula |
|-----------|---------|
| **Area** | `A = (r²θ)/2` |
| **Lunghezza arco** | `L = rθ` |

**Conversione angoli:**
- Gradi → Radianti: `θ_rad = (θ_gradi × π)/180`

---

### 1.11 Corona Circolare

**Parametri:**
- Raggio esterno: `R`
- Raggio interno: `r`

**Formula:**

| Grandezza | Formula |
|-----------|---------|
| **Area** | `A = π(R² - r²) = π(R+r)(R-r)` |

---

## PARTE 2: SOLIDI (3D)

### 2.1 Cubo

**Parametri:**
- Spigolo: `l`

**Formule:**

| Grandezza | Formula |
|-----------|---------|
| **Area superficie totale** | `A_tot = 6l²` |
| **Volume** | `V = l³` |
| **Diagonale cubo** | `d = l√3` |
| **Diagonale faccia** | `d_f = l√2` |

---

### 2.2 Parallelepipedo Rettangolare

**Parametri:**
- Lunghezza: `l`
- Larghezza: `w`
- Altezza: `h`

**Formule:**

| Grandezza | Formula |
|-----------|---------|
| **Area superficie totale** | `A_tot = 2(lw + lh + wh)` |
| **Volume** | `V = l × w × h` |
| **Diagonale** | `d = √(l² + w² + h²)` |

---

### 2.3 Cilindro

**Parametri:**
- Raggio base: `r`
- Altezza: `h`

**Formule:**

| Grandezza | Formula |
|-----------|---------|
| **Area base** | `A_base = πr²` |
| **Area laterale** | `A_lat = 2πrh` |
| **Area superficie totale** | `A_tot = 2πr² + 2πrh = 2πr(r + h)` |
| **Volume** | `V = πr²h` |

---

### 2.4 Cono

**Parametri:**
- Raggio base: `r`
- Altezza: `h`
- Apotema (generatrice): `a = √(r² + h²)`

**Formule:**

| Grandezza | Formula |
|-----------|---------|
| **Area base** | `A_base = πr²` |
| **Area laterale** | `A_lat = πra = πr√(r² + h²)` |
| **Area superficie totale** | `A_tot = πr² + πra = πr(r + a)` |
| **Volume** | `V = (πr²h)/3` |

---

### 2.5 Sfera

**Parametri:**
- Raggio: `r`
- Diametro: `d = 2r`

**Formule:**

| Grandezza | Formula |
|-----------|---------|
| **Area superficie** | `A = 4πr² = πd²` |
| **Volume** | `V = (4πr³)/3 = (πd³)/6` |

---

### 2.6 Piramide

**Parametri:**
- Area base: `A_b`
- Altezza: `h`
- Perimetro base: `P`
- Apotema: `a` (altezza faccia laterale)

**Formule:**

| Grandezza | Formula |
|-----------|---------|
| **Area superficie laterale** | `A_lat = (P × a)/2` |
| **Area superficie totale** | `A_tot = A_b + A_lat` |
| **Volume** | `V = (A_b × h)/3` |

**Piramide a base quadrata (lato base `l`):**
- `V = (l²h)/3`
- `A_lat = 2l√(h² + (l/2)²)`

---

### 2.7 Prisma

**Parametri:**
- Area base: `A_b`
- Altezza: `h`
- Perimetro base: `P`

**Formule:**

| Grandezza | Formula |
|-----------|---------|
| **Area superficie laterale** | `A_lat = P × h` |
| **Area superficie totale** | `A_tot = 2A_b + A_lat` |
| **Volume** | `V = A_b × h` |

---

### 2.8 Tronco di Cono

**Parametri:**
- Raggio base maggiore: `R`
- Raggio base minore: `r`
- Altezza: `h`
- Apotema: `a = √[h² + (R-r)²]`

**Formule:**

| Grandezza | Formula |
|-----------|---------|
| **Area laterale** | `A_lat = π(R + r)a` |
| **Area superficie totale** | `A_tot = π(R² + r² + (R+r)a)` |
| **Volume** | `V = (πh/3)(R² + Rr + r²)` |

---

### 2.9 Tronco di Piramide

**Parametri:**
- Area base maggiore: `A₁`
- Area base minore: `A₂`
- Altezza: `h`

**Formula:**

| Grandezza | Formula |
|-----------|---------|
| **Volume** | `V = (h/3)(A₁ + A₂ + √(A₁A₂))` |

---

### 2.10 Toro (Ciambella)

**Parametri:**
- Raggio maggiore (dal centro al tubo): `R`
- Raggio minore (raggio del tubo): `r`

**Formule:**

| Grandezza | Formula |
|-----------|---------|
| **Area superficie** | `A = 4π²Rr` |
| **Volume** | `V = 2π²Rr²` |

---

### 2.11 Calotta Sferica

**Parametri:**
- Raggio sfera: `R`
- Altezza calotta: `h`

**Formule:**

| Grandezza | Formula |
|-----------|---------|
| **Area superficie** | `A = 2πRh` |
| **Volume** | `V = (πh²/3)(3R - h)` |

---

## PARTE 3: CONVERSIONI FISICHE

### 3.1 Lunghezza

#### Sistema Metrico

| Unità | Conversione |
|-------|-------------|
| 1 km | = 1000 m |
| 1 m | = 100 cm = 1000 mm |
| 1 cm | = 10 mm |
| 1 mm | = 1000 μm (micrometri) |
| 1 μm | = 1000 nm (nanometri) |

#### Sistema Imperiale

| Unità | Conversione metrica |
|-------|---------------------|
| 1 miglio (mile) | = 1.60934 km = 1609.34 m |
| 1 iarda (yard) | = 0.9144 m = 91.44 cm |
| 1 piede (foot, ft) | = 0.3048 m = 30.48 cm |
| 1 pollice (inch, in) | = 2.54 cm = 25.4 mm |

#### Marino e Astronomico

| Unità | Conversione |
|-------|-------------|
| 1 miglio nautico | = 1.852 km = 1852 m |
| 1 unità astronomica (AU) | = 149,597,870.7 km |
| 1 anno luce | = 9.461 × 10¹² km |
| 1 parsec | = 3.0857 × 10¹³ km ≈ 3.26 anni luce |

#### Conversioni Rapide

```c
// Esempi in C
double metri_to_feet(double m) { return m * 3.28084; }
double km_to_miles(double km) { return km * 0.621371; }
double inches_to_cm(double in) { return in * 2.54; }
```

---

### 3.2 Area (Superficie)

#### Sistema Metrico

| Unità | Conversione |
|-------|-------------|
| 1 km² | = 1,000,000 m² = 100 ha |
| 1 ha (ettaro) | = 10,000 m² |
| 1 m² | = 10,000 cm² |
| 1 cm² | = 100 mm² |

#### Sistema Imperiale

| Unità | Conversione metrica |
|-------|---------------------|
| 1 miglio² (square mile) | = 2.58999 km² |
| 1 acro (acre) | = 4046.86 m² ≈ 0.404686 ha |
| 1 yard² | = 0.836127 m² |
| 1 ft² | = 0.092903 m² = 929.03 cm² |
| 1 inch² | = 6.4516 cm² |

---

### 3.3 Volume

#### Sistema Metrico

| Unità | Conversione |
|-------|-------------|
| 1 m³ | = 1000 L = 1,000,000 cm³ |
| 1 L (litro) | = 1000 mL = 1000 cm³ = 1 dm³ |
| 1 mL | = 1 cm³ |
| 1 hL (ettolitro) | = 100 L |

#### Sistema Imperiale (USA)

| Unità | Conversione metrica |
|-------|---------------------|
| 1 gallone (gallon, gal) | = 3.78541 L |
| 1 quarto (quart, qt) | = 0.946353 L |
| 1 pinta (pint, pt) | = 0.473176 L |
| 1 tazza (cup) | = 236.588 mL |
| 1 oncia fluida (fl oz) | = 29.5735 mL |
| 1 cucchiaio (tablespoon) | = 14.7868 mL |
| 1 cucchiaino (teaspoon) | = 4.92892 mL |

#### Sistema Imperiale (UK)

| Unità | Conversione metrica |
|-------|---------------------|
| 1 gallone UK | = 4.54609 L |
| 1 pinta UK | = 0.568261 L |

#### Altro

| Unità | Conversione |
|-------|-------------|
| 1 ft³ (piede cubo) | = 28.3168 L = 0.0283168 m³ |
| 1 in³ (pollice cubo) | = 16.3871 cm³ |

---

### 3.4 Massa/Peso

#### Sistema Metrico

| Unità | Conversione |
|-------|-------------|
| 1 tonnellata (t) | = 1000 kg |
| 1 kg | = 1000 g |
| 1 g | = 1000 mg |
| 1 mg | = 1000 μg (microgrammi) |

#### Sistema Imperiale

| Unità | Conversione metrica |
|-------|---------------------|
| 1 libbra (pound, lb) | = 0.453592 kg = 453.592 g |
| 1 oncia (ounce, oz) | = 28.3495 g |
| 1 stone | = 6.35029 kg = 14 lb |
| 1 ton (USA, short ton) | = 907.185 kg |
| 1 ton (UK, long ton) | = 1016.05 kg |

#### Note
> **Massa ≠ Peso**
> Peso = Massa × Accelerazione di gravità
> `P = m × g` (g ≈ 9.81 m/s² sulla Terra)

---

### 3.5 Temperatura

#### Scale di Temperatura

| Scala | Simbolo | Zero Assoluto |
|-------|---------|---------------|
| Celsius | °C | -273.15°C |
| Fahrenheit | °F | -459.67°F |
| Kelvin | K | 0 K |
| Rankine | °R | 0°R |

#### Formule di Conversione

| Da | A | Formula |
|----|---|---------|
| **Celsius** | Fahrenheit | `°F = (°C × 9/5) + 32` |
| **Fahrenheit** | Celsius | `°C = (°F - 32) × 5/9` |
| **Celsius** | Kelvin | `K = °C + 273.15` |
| **Kelvin** | Celsius | `°C = K - 273.15` |
| **Fahrenheit** | Kelvin | `K = (°F - 32) × 5/9 + 273.15` |
| **Kelvin** | Fahrenheit | `°F = (K - 273.15) × 9/5 + 32` |

#### Punti di Riferimento

| Evento | Celsius | Fahrenheit | Kelvin |
|--------|---------|------------|--------|
| Zero assoluto | -273.15°C | -459.67°F | 0 K |
| Acqua congela | 0°C | 32°F | 273.15 K |
| Temperatura corpo | 37°C | 98.6°F | 310.15 K |
| Acqua bolle | 100°C | 212°F | 373.15 K |

**Esempio in C:**
```c
double celsius_to_fahrenheit(double c) {
    return (c * 9.0/5.0) + 32.0;
}

double fahrenheit_to_celsius(double f) {
    return (f - 32.0) * 5.0/9.0;
}
```

---

### 3.6 Tempo

| Unità | Conversione |
|-------|-------------|
| 1 millennio | = 1000 anni |
| 1 secolo | = 100 anni |
| 1 decennio | = 10 anni |
| 1 anno | ≈ 365.25 giorni (anno medio) |
| 1 anno | = 12 mesi = 52 settimane |
| 1 mese | ≈ 30.44 giorni (medio) |
| 1 settimana | = 7 giorni |
| 1 giorno | = 24 ore |
| 1 ora (h) | = 60 minuti = 3600 secondi |
| 1 minuto (min) | = 60 secondi (s) |
| 1 secondo (s) | = 1000 millisecondi (ms) |
| 1 ms | = 1000 microsecondi (μs) |
| 1 μs | = 1000 nanosecondi (ns) |

---

### 3.7 Velocità

#### Sistema Metrico

| Conversione |
|-------------|
| 1 m/s = 3.6 km/h |
| 1 km/h = 0.277778 m/s |

#### Conversioni Internazionali

| Da | A | Fattore |
|----|---|---------|
| km/h | mph | × 0.621371 |
| mph | km/h | × 1.60934 |
| m/s | mph | × 2.23694 |
| m/s | ft/s | × 3.28084 |

#### Velocità Speciali

| Descrizione | Valore |
|-------------|--------|
| Velocità del suono (a 20°C) | ≈ 343 m/s ≈ 1235 km/h |
| Mach 1 | = velocità del suono |
| Velocità della luce | c = 299,792,458 m/s ≈ 300,000 km/s |
| 1 nodo (nautico) | = 1 miglio nautico/ora = 1.852 km/h |

---

### 3.8 Accelerazione

| Unità | Valore |
|-------|--------|
| Accelerazione di gravità (Terra) | g = 9.80665 m/s² ≈ 9.81 m/s² |
| 1 m/s² | = 3.28084 ft/s² |
| 1 g | = 9.80665 m/s² = 32.174 ft/s² |

---

### 3.9 Forza

#### Unità SI: Newton (N)

| Unità | Conversione |
|-------|-------------|
| 1 N | = 1 kg·m/s² |
| 1 kN (kilonewton) | = 1000 N |
| 1 dyne | = 10⁻⁵ N |

#### Sistema Imperiale

| Unità | Conversione |
|-------|-------------|
| 1 libbra-forza (lbf) | = 4.44822 N |
| 1 kgf (kilogrammo-forza) | = 9.80665 N |

---

### 3.10 Pressione

#### Unità SI: Pascal (Pa)

| Unità | Conversione |
|-------|-------------|
| 1 Pa | = 1 N/m² |
| 1 kPa (kilopascal) | = 1000 Pa |
| 1 MPa (megapascal) | = 1,000,000 Pa |
| 1 bar | = 100,000 Pa = 100 kPa |

#### Atmosfera

| Unità | Valore |
|-------|--------|
| 1 atmosfera standard (atm) | = 101,325 Pa = 101.325 kPa = 1.01325 bar |

#### Altre Unità

| Unità | Conversione |
|-------|-------------|
| 1 mmHg (millimetro di mercurio) | = 133.322 Pa |
| 1 torr | ≈ 1 mmHg = 133.322 Pa |
| 1 psi (pound per square inch) | = 6894.76 Pa ≈ 6.895 kPa |

#### Conversioni Rapide

```
1 atm = 760 mmHg = 760 torr = 14.696 psi = 1.01325 bar
1 bar = 14.5038 psi
1 MPa = 145.038 psi
```

---

### 3.11 Energia/Lavoro

#### Unità SI: Joule (J)

| Unità | Conversione |
|-------|-------------|
| 1 J | = 1 N·m = 1 kg·m²/s² |
| 1 kJ (kilojoule) | = 1000 J |
| 1 MJ (megajoule) | = 1,000,000 J |

#### Calorie

| Unità | Conversione |
|-------|-------------|
| 1 caloria (cal) | = 4.184 J |
| 1 kilocaloria (kcal o Cal) | = 4184 J = 4.184 kJ |

> **Nota:** 1 Cal alimentare = 1 kcal

#### Elettricità

| Unità | Conversione |
|-------|-------------|
| 1 kilowattora (kWh) | = 3.6 MJ = 3,600,000 J |
| 1 elettronvolt (eV) | = 1.60218 × 10⁻¹⁹ J |

#### Sistema Imperiale

| Unità | Conversione |
|-------|-------------|
| 1 BTU (British Thermal Unit) | = 1055.06 J ≈ 1.055 kJ |
| 1 foot-pound (ft·lb) | = 1.35582 J |

---

### 3.12 Potenza

#### Unità SI: Watt (W)

| Unità | Conversione |
|-------|-------------|
| 1 W | = 1 J/s = 1 kg·m²/s³ |
| 1 kW (kilowatt) | = 1000 W |
| 1 MW (megawatt) | = 1,000,000 W |
| 1 GW (gigawatt) | = 1,000,000,000 W |

#### Sistema Imperiale

| Unità | Conversione |
|-------|-------------|
| 1 cavallo vapore (HP, horsepower) | = 745.7 W ≈ 0.746 kW |
| 1 cavallo vapore metrico (CV) | = 735.5 W |

#### Conversioni

```
1 kW = 1.341 HP
1 HP = 550 ft·lb/s
1 kW = 3412.14 BTU/h
```

---

### 3.13 Angoli

#### Unità

| Sistema | Cerchio completo | Angolo retto | Angolo piatto |
|---------|------------------|--------------|---------------|
| **Gradi** | 360° | 90° | 180° |
| **Radianti** | 2π rad | π/2 rad | π rad |

#### Gradi Sessagesimali

```
1° = 60' (minuti d'arco)
1' = 60" (secondi d'arco)
```

#### Formule di Conversione

| Da | A | Formula |
|----|---|---------|
| Gradi | Radianti | `rad = (deg × π)/180` |
| Radianti | Gradi | `deg = (rad × 180)/π` |

#### Conversioni Comuni

| Gradi | Radianti | Valore numerico radianti |
|-------|----------|--------------------------|
| 360° | 2π | ≈ 6.28319 |
| 180° | π | ≈ 3.14159 |
| 90° | π/2 | ≈ 1.5708 |
| 60° | π/3 | ≈ 1.0472 |
| 45° | π/4 | ≈ 0.7854 |
| 30° | π/6 | ≈ 0.5236 |
| 1° | - | ≈ 0.0174533 rad |
| 1 rad | - | ≈ 57.2958° |

---

### 3.14 Frequenza

#### Unità SI: Hertz (Hz)

| Unità | Conversione |
|-------|-------------|
| 1 Hz | = 1 ciclo/secondo = 1 s⁻¹ |
| 1 kHz (kilohertz) | = 1000 Hz |
| 1 MHz (megahertz) | = 1,000,000 Hz |
| 1 GHz (gigahertz) | = 1,000,000,000 Hz |

#### Relazione con Periodo

```
f = 1/T
T = 1/f
```
dove `f` = frequenza, `T` = periodo

#### Esempi Pratici

| Applicazione | Frequenza |
|--------------|-----------|
| Rete elettrica (Europa) | 50 Hz |
| Rete elettrica (USA) | 60 Hz |
| Radio FM | 88-108 MHz |
| WiFi | 2.4 GHz o 5 GHz |
| Processori CPU | 1-5 GHz |

---

### 3.15 Densità

#### Unità SI

- `kg/m³` (kilogrammo per metro cubo)
- `g/cm³` (grammo per centimetro cubo)

#### Conversioni

| Unità | Conversione |
|-------|-------------|
| 1 g/cm³ | = 1000 kg/m³ |
| 1 kg/L | = 1000 kg/m³ = 1 g/cm³ |

#### Sistema Imperiale

| Unità | Conversione |
|-------|-------------|
| 1 lb/ft³ | = 16.0185 kg/m³ |
| 1 lb/in³ | = 27,679.9 kg/m³ |

#### Densità di Materiali Comuni

| Materiale | Densità (kg/m³) |
|-----------|-----------------|
| Acqua (4°C) | 1000 |
| Aria (20°C, 1 atm) | 1.204 |
| Ghiaccio | 917 |
| Alluminio | 2700 |
| Ferro | 7874 |
| Rame | 8960 |
| Piombo | 11,340 |
| Oro | 19,300 |
| Platino | 21,450 |
| Legno (quercia) | 600-900 |
| Calcestruzzo | 2400 |

---

## PARTE 4: SENSORI DI TEMPERATURA - TERMOCOPPIE

### 4.1 Introduzione alle Termocoppie

#### Cos'è una Termocoppia?

Una **termocoppia** è un sensore di temperatura che sfrutta l'**effetto Seebeck**: quando due metalli diversi sono uniti e i loro giunti sono a temperature diverse, si genera una **tensione elettrica** (dell'ordine dei millivolt) proporzionale alla differenza di temperatura.

#### Principio di Funzionamento

```
Metallo A ──┬─────────────┬── Metallo A
            │             │
        Giunto     Giunto freddo
         caldo   (riferimento)
           │             │
         (T_hot)      (T_cold)
           │             │
           └─── ΔV ──────┘
```

**Formula base:**
```
V = α × (T_hot - T_cold)
```
dove:
- `V` = tensione generata (mV)
- `α` = coefficiente Seebeck (dipende dai metalli)
- `T_hot` = temperatura del giunto caldo (punto di misura)
- `T_cold` = temperatura del giunto freddo (riferimento)

#### Vantaggi

✅ Ampio range di temperatura (-200°C a +2300°C)
✅ Robuste e durature
✅ Economiche
✅ Auto-alimentate (non servono batterie)
✅ Risposta rapida
✅ Piccole dimensioni possibili

#### Svantaggi

❌ Bassa accuratezza (±1-3°C tipico)
❌ Tensione molto bassa (μV/mV)
❌ Non lineari
❌ Necessitano compensazione giunto freddo
❌ Sensibili a interferenze elettromagnetiche

---

### 4.2 Tipi di Termocoppie Standard

Le termocoppie sono classificate secondo standard internazionali (ANSI, IEC) con lettere che identificano la combinazione di metalli.

#### Classificazione per Utilizzo

| Categoria | Tipi | Applicazioni |
|-----------|------|--------------|
| **Base Metal** | J, K, T, E, N | Uso generale, industriale |
| **Noble Metal** | R, S, B | Alta temperatura, laboratorio |
| **Specializzate** | C, D, G | Applicazioni specifiche |

---

### 4.3 Termocoppia Tipo J

#### Caratteristiche

| Parametro | Valore |
|-----------|--------|
| **Materiali** | **Ferro (+)** vs **Costantana (-)** |
| **Colore fili** | Positivo: Bianco / Negativo: Rosso (USA) |
| **Range temperatura** | -40°C a +750°C |
| **Range consigliato** | 0°C a +500°C |
| **Sensibilità (Seebeck)** | ≈ 50-60 μV/°C |
| **Accuratezza** | ±2.2°C o ±0.75% (standard) |
| **Atmosfera** | Riducente, inerte (non ossidante) |

#### Applicazioni Tipiche

- Industria plastica (estrusori)
- Forni industriali
- Motori diesel
- Industria alimentare (limitata a <500°C)
- Apparecchiature di processo generale

#### Vantaggi e Svantaggi

**Vantaggi:**
- ✅ Economica
- ✅ Ampio range
- ✅ Buona sensibilità
- ✅ Robusta

**Svantaggi:**
- ❌ Ferro si ossida sopra 540°C
- ❌ Corrosione in ambiente umido
- ❌ Vita limitata ad alta temperatura
- ❌ Non per ambienti ossidanti

#### Tensione Output (Giunto freddo a 0°C)

| Temperatura | Tensione (mV) |
|-------------|---------------|
| 0°C | 0.000 |
| 100°C | 5.268 |
| 200°C | 10.777 |
| 300°C | 16.325 |
| 400°C | 21.846 |
| 500°C | 27.388 |
| 600°C | 33.102 |
| 700°C | 39.130 |

---

### 4.4 Termocoppia Tipo K

#### Caratteristiche

| Parametro | Valore |
|-----------|--------|
| **Materiali** | **Chromel (+)** (Ni-Cr) vs **Alumel (-)** (Ni-Al) |
| **Colore fili** | Positivo: Giallo / Negativo: Rosso (USA) |
| **Range temperatura** | -200°C a +1350°C |
| **Range consigliato** | -40°C a +1000°C |
| **Sensibilità (Seebeck)** | ≈ 41 μV/°C |
| **Accuratezza** | ±2.2°C o ±0.75% (standard) |
| **Atmosfera** | Ossidante o inerte (non riducente) |

#### Applicazioni Tipiche

- **Più comune in assoluto** (70% mercato)
- Forni industriali ad alta temperatura
- Trattamenti termici metalli
- Fonderie
- Turbine a gas
- Industria alimentare
- HVAC (riscaldamento/raffreddamento)
- Automotive
- Laboratori generici

#### Vantaggi e Svantaggi

**Vantaggi:**
- ✅ **Standard de facto** (più usata)
- ✅ Ampio range temperatura
- ✅ Buona accuratezza
- ✅ Economica
- ✅ Resistente ossidazione
- ✅ Ottima linearità

**Svantaggi:**
- ❌ Non adatta ad atmosfere riducenti
- ❌ Sensibile a contaminazione (deriva nel tempo)
- ❌ Non per atmosfere solfuree
- ❌ "Green rot" (corrosione) in certe condizioni

#### Tensione Output (Giunto freddo a 0°C)

| Temperatura | Tensione (mV) |
|-------------|---------------|
| -200°C | -5.891 |
| -100°C | -3.554 |
| 0°C | 0.000 |
| 100°C | 4.095 |
| 200°C | 8.137 |
| 300°C | 12.207 |
| 400°C | 16.395 |
| 500°C | 20.640 |
| 600°C | 24.902 |
| 700°C | 29.128 |
| 800°C | 33.275 |
| 900°C | 37.325 |
| 1000°C | 41.269 |
| 1100°C | 45.108 |
| 1200°C | 48.838 |
| 1300°C | 52.398 |

#### Polinomio di Approssimazione (Tipo K, 0-1372°C)

Per convertire temperatura → tensione:
```
V = c₀ + c₁T + c₂T² + c₃T³ + ... + c₉T⁹
```

Coefficienti (0-1372°C):
- c₀ = 0.000000000000E+00
- c₁ = 3.945012802514E-02
- c₂ = 2.362237359873E-05
- c₃ = -3.285890678698E-07
- c₄ = 9.916080034248E-10
- (e altri...)

> Per implementazione in C, usare tabelle NIST ufficiali con interpolazione.

---

### 4.5 Termocoppia Tipo S

#### Caratteristiche

| Parametro | Valore |
|-----------|--------|
| **Materiali** | **Platino-10% Rodio (+)** vs **Platino (-)** |
| **Colore fili** | Positivo: Nero / Negativo: Rosso (USA) |
| **Range temperatura** | -50°C a +1768°C |
| **Range consigliato** | 600°C a +1600°C |
| **Sensibilità (Seebeck)** | ≈ 10 μV/°C (molto bassa!) |
| **Accuratezza** | ±1.5°C o ±0.25% (alta precisione) |
| **Atmosfera** | Ossidante o inerte |

#### Applicazioni Tipiche

- **Standard di laboratorio** (alta precisione)
- Calibrazione strumenti
- Forni ad altissima temperatura
- Industria ceramica
- Trattamenti termici metalli nobili
- Industria del vetro
- Ricerca scientifica
- Fonderie (metalli preziosi)

#### Vantaggi e Svantaggi

**Vantaggi:**
- ✅ **Altissima temperatura** (fino 1768°C)
- ✅ **Alta accuratezza e stabilità**
- ✅ Eccellente ripetibilità
- ✅ Standard internazionale (ITS-90)
- ✅ Resistente ossidazione
- ✅ Inerzia chimica (platino)

**Svantaggi:**
- ❌ **Molto costosa** (platino!)
- ❌ Sensibilità molto bassa (10 μV/°C)
- ❌ Richiede amplificazione maggiore
- ❌ Fragile meccanicamente
- ❌ Contaminazione da metalli comuni
- ❌ Non per atmosfere riducenti o con metalli vapori

#### Tensione Output (Giunto freddo a 0°C)

| Temperatura | Tensione (mV) |
|-------------|---------------|
| 0°C | 0.000 |
| 100°C | 0.645 |
| 200°C | 1.440 |
| 300°C | 2.323 |
| 400°C | 3.259 |
| 500°C | 4.233 |
| 600°C | 5.237 |
| 700°C | 6.274 |
| 800°C | 7.345 |
| 900°C | 8.448 |
| 1000°C | 9.585 |
| 1100°C | 10.754 |
| 1200°C | 11.951 |
| 1300°C | 13.173 |
| 1400°C | 14.416 |
| 1500°C | 15.576 |
| 1600°C | 17.445 |

#### Note Importanti

⚠️ La termocoppia tipo S è **sensibilissima alla contaminazione** da metalli base (ferro, nichel, rame). Anche piccole tracce possono alterare le misure.

⚠️ Richiede **protezione ceramica** ad alta purezza (allumina 99.7%+).

---

### 4.6 Altri Tipi di Termocoppie

#### Tipo T (Rame-Costantana)

| Parametro | Valore |
|-----------|--------|
| **Range** | -200°C a +400°C |
| **Sensibilità** | ≈ 43 μV/°C |
| **Applicazioni** | Criogenia, laboratori, alimentare |
| **Vantaggi** | Ottima per basse temperature, resistente umidità |

#### Tipo E (Chromel-Costantana)

| Parametro | Valore |
|-----------|--------|
| **Range** | -200°C a +900°C |
| **Sensibilità** | ≈ 68 μV/°C (massima!) |
| **Applicazioni** | Forni, laboratori |
| **Vantaggi** | Output altissimo, buona per basse temperature |

#### Tipo N (Nicrosil-Nisil)

| Parametro | Valore |
|-----------|--------|
| **Range** | -270°C a +1300°C |
| **Sensibilità** | ≈ 39 μV/°C |
| **Applicazioni** | Alternativa migliorata al tipo K |
| **Vantaggi** | Più stabile del K, resistente ossidazione |

#### Tipo R (Platino-13% Rodio vs Platino)

| Parametro | Valore |
|-----------|--------|
| **Range** | -50°C a +1768°C |
| **Sensibilità** | ≈ 10 μV/°C |
| **Applicazioni** | Simile a tipo S, laboratori |
| **Note** | Più stabile di S ad alta temperatura |

#### Tipo B (Platino-30% Rodio vs Platino-6% Rodio)

| Parametro | Valore |
|-----------|--------|
| **Range** | 200°C a +1820°C |
| **Sensibilità** | ≈ 10 μV/°C |
| **Applicazioni** | Altissime temperature |
| **Vantaggi** | Output quasi nullo sotto 50°C (auto-compensazione parziale) |

#### Tipo C (Tungsteno-5% Renio vs Tungsteno-26% Renio)

| Parametro | Valore |
|-----------|--------|
| **Range** | 0°C a +2315°C |
| **Applicazioni** | Forni sottovuoto, aerospaziale |
| **Vantaggi** | Temperature estreme |
| **Svantaggi** | Fragile, costosa, solo vuoto o inerte |

---

### 4.7 Tabella Comparativa

| Tipo | Materiali | Range (°C) | Sensibilità (μV/°C) | Costo | Applicazione Principale |
|------|-----------|------------|---------------------|-------|-------------------------|
| **J** | Fe vs Const | -40 a 750 | 50-60 | € | Uso generale, industriale |
| **K** | Chromel vs Alumel | -200 a 1350 | 41 | € | **PIÙ COMUNE** - generale |
| **T** | Cu vs Const | -200 a 400 | 43 | € | Basse temperature, criogenia |
| **E** | Chromel vs Const | -200 a 900 | 68 | € | Alta sensibilità |
| **N** | Nicrosil vs Nisil | -270 a 1300 | 39 | €€ | Alternativa K migliorata |
| **R** | Pt-13%Rh vs Pt | -50 a 1768 | 10 | €€€€ | Laboratorio, precisione |
| **S** | Pt-10%Rh vs Pt | -50 a 1768 | 10 | €€€€ | **STANDARD** laboratorio |
| **B** | Pt-30%Rh vs Pt-6%Rh | 200 a 1820 | 10 | €€€€€ | Altissime temperature |
| **C** | W-5%Re vs W-26%Re | 0 a 2315 | varia | €€€€€ | Temperature estreme |

**Legenda costo:**
- € = Economica (<10€)
- €€ = Media (10-50€)
- €€€€ = Costosa (100-500€)
- €€€€€ = Molto costosa (>500€)

---

### 4.8 Conversione Tensione-Temperatura

#### Metodi di Conversione

Esistono 3 metodi principali per convertire tensione ↔ temperatura:

##### 1. **Tabelle di Lookup (LUT)**

Usare tabelle NIST ufficiali con interpolazione lineare.

**Vantaggi:** Semplice, accurato
**Svantaggi:** Richiede memoria

**Esempio in C:**
```c
// Tabella semplificata tipo K (ogni 100°C)
const float tipo_k_lut[][2] = {
    {0.000, 0.0},     // 0°C
    {4.095, 100.0},   // 100°C
    {8.137, 200.0},   // 200°C
    {12.207, 300.0},  // 300°C
    // ... continua
};

float tipo_k_mv_to_celsius(float mv) {
    // Interpolazione lineare tra punti tabella
    // (codice semplificato)
    for (int i = 0; i < TABLE_SIZE-1; i++) {
        if (mv >= tipo_k_lut[i][0] && mv <= tipo_k_lut[i+1][0]) {
            float t0 = tipo_k_lut[i][1];
            float t1 = tipo_k_lut[i+1][1];
            float v0 = tipo_k_lut[i][0];
            float v1 = tipo_k_lut[i+1][0];
            return t0 + (mv - v0) * (t1 - t0) / (v1 - v0);
        }
    }
    return -999.0; // Errore
}
```

##### 2. **Polinomi di Approssimazione**

NIST fornisce polinomi di grado 5-10 per ogni tipo.

**Formula generale:**
```
T = c₀ + c₁V + c₂V² + c₃V³ + ... + cₙVⁿ
```

**Vantaggi:** Accurato, poco codice
**Svantaggi:** Calcolo pesante (pow), range limitati

##### 3. **Approssimazioni Lineari (Semplificate)**

Per range ridotti, approssimazione lineare:
```
T ≈ T₀ + (V / S)
```
dove S = sensibilità (μV/°C)

**Vantaggi:** Velocissimo
**Svantaggi:** Accuratezza ridotta (±5-10°C)

**Esempio tipo K (semplificato, 0-1000°C):**
```c
float tipo_k_mv_to_celsius_approx(float mv) {
    // Approssimazione lineare: ~41 μV/°C
    return mv / 0.041;  // mV to °C
}
```

---

### 4.9 Compensazione Giunto Freddo

#### Problema

Le termocoppie misurano la **differenza** di temperatura tra giunto caldo e giunto freddo. Se il giunto freddo non è a 0°C, la lettura è errata!

```
V_misurata = α × (T_hot - T_cold)
```

Se `T_cold ≠ 0°C`, dobbiamo compensare.

#### Soluzione: Cold Junction Compensation (CJC)

**Metodo 1: Bagno di ghiaccio**
- Giunto freddo in acqua+ghiaccio → 0°C garantito
- Usato in laboratorio (scomodo)

**Metodo 2: Termometro di riferimento**
- Misura T_cold con sensore accurato (RTD, termistor, IC)
- Calcola correzione software

**Formula:**
```
T_hot = T_misurata + T_cold
```

dove:
- `T_misurata` = temperatura calcolata da V_misurata (assumendo T_cold = 0)
- `T_cold` = temperatura effettiva giunto freddo (misurata)

#### Implementazione Pratica

**Hardware:** Usare IC specializzati (es: MAX31855, AD8495, LTC2983)
- Hanno CJC integrato
- Linearizzazione automatica
- Output digitale (SPI/I2C) o analogico

**Software:**
```c
float leggi_temperatura_tipo_k(float mv_termocoppia, float temp_giunto_freddo) {
    // 1. Converti mV a temperatura (assumendo giunto freddo a 0°C)
    float temp_misurata = tipo_k_mv_to_celsius(mv_termocoppia);

    // 2. Aggiungi compensazione giunto freddo
    float temp_reale = temp_misurata + temp_giunto_freddo;

    return temp_reale;
}
```

#### Esempio Numerico

```
Situazione:
- Termocoppia misura: 10 mV
- Tabella tipo K: 10 mV → 243.6°C (se giunto freddo a 0°C)
- Ma giunto freddo è a 25°C!

Compensazione:
- Temperatura effettiva = 243.6°C + 25°C = 268.6°C

Senza compensazione: ERRORE di 25°C!
```

---

### 4.10 Circuiti di Condizionamento

#### Componenti Necessari

1. **Amplificatore differenziale** (segnale piccolo, 10-50 μV/°C)
2. **Filtro anti-aliasing** (riduce rumore 50/60 Hz)
3. **ADC ad alta risoluzione** (16-24 bit)
4. **Sensore temperatura CJC** (termistor, IC)
5. **Protezione ESD**

#### Schema Semplificato

```
Termocoppia (+) ──┬───[Protezione ESD]───┐
                  │                       │
                  │                   [Amplif.]──[Filtro]──[ADC]──[μC]
                  │                       │
Termocoppia (-) ──┴───[Protezione ESD]───┘
                  │
           [Sensore CJC]──────────────────────────[ADC]──[μC]
```

#### IC Specializzati Consigliati

| IC | Tipo | Risoluzione | Caratteristiche |
|----|------|-------------|-----------------|
| **MAX31855** | SPI | 14-bit | Tipo K, economico, CJC integrato |
| **MAX6675** | SPI | 12-bit | Solo tipo K, base |
| **AD8495** | Analogico | - | Tipo K, output 5mV/°C, semplice |
| **AD595** | Analogico | - | Tipo K, output 10mV/°C |
| **LTC2983** | SPI | 24-bit | Multi-tipo (J,K,S,T,E,N,R,B), precisione |
| **MCP9600** | I2C | 16-bit | Tipo K,J,T,N,S,E,B,R, economico |

**Esempio con MAX31855 (popolare):**
```c
// Pseudo-codice Arduino
#include <MAX31855.h>

MAX31855 termocoppia(CLK_PIN, CS_PIN, DO_PIN);

void loop() {
    float temp_celsius = termocoppia.readCelsius();
    float temp_giunto_freddo = termocoppia.readInternal();

    if (isnan(temp_celsius)) {
        Serial.println("Errore lettura termocoppia");
    } else {
        Serial.print("Temperatura: ");
        Serial.print(temp_celsius);
        Serial.println(" °C");
    }

    delay(1000);
}
```

---

### 4.11 Considerazioni Pratiche

#### Cavi e Connettori

⚠️ **IMPORTANTE:** Usare **cavi di estensione specifici** per ogni tipo!

- Cavi standard: fino al giunto freddo (connettore/terminali)
- Cavi di compensazione: hanno caratteristiche simili alla termocoppia
- Cavi sbagliati → errori enormi!

**Connettori standard:**
- **USA:** ANSI MC96.1 (forme specifiche per tipo)
- **Europa:** IEC 60584-3 (colori standard)

**Colori USA (ANSI):**
- Tipo J: Bianco(+) / Rosso(-)
- Tipo K: Giallo(+) / Rosso(-)
- Tipo T: Blu(+) / Rosso(-)
- Tipo E: Viola(+) / Rosso(-)

#### Errori Comuni

❌ **Giunto freddo non compensato** → errore = T_ambiente
❌ **Cavi di estensione sbagliati** → errori imprevedibili
❌ **Messa a terra errata** → loop di massa, rumore 50/60 Hz
❌ **Ossidazione contatti** → drift, letture instabili
❌ **Gradiente termico su connettori** → giunto freddo "falso"
❌ **Amplificazione insufficiente** → risoluzione bassa
❌ **Ambiente chimico incompatibile** → corrosione, deriva

#### Best Practices

✅ Usare IC specializzati (MAX31855, LTC2983...)
✅ Protezione ESD su ingressi
✅ Filtraggio 50/60 Hz (notch filter)
✅ Cavi schermati e twisted
✅ Giunto freddo isotermico (blocco terminale)
✅ Calibrazione periodica (vs standard)
✅ Guaine protettive adeguate all'ambiente
✅ Evitare loop di massa

---

### 4.12 Risorse e Riferimenti

#### Tabelle Ufficiali

- **NIST ITS-90 Thermocouple Database**
  https://srdata.nist.gov/its90/main/

- **NIST Monograph 175** (Tabelle complete)
  https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf

#### Standard

- **ANSI MC96.1** (USA) - Termocoppie e colori cavi
- **IEC 60584** (Europa) - Specifiche termocoppie
- **ASTM E230** - Tabelle e tolleranze

#### Libri Consigliati

- "Manual on the Use of Thermocouples in Temperature Measurement" (ASTM)
- "Temperature Measurement" - L. Michalski et al.

#### Datasheets IC Utili

- Maxim MAX31855 (tipo K, SPI, economico)
- Analog Devices AD8495 (tipo K, analogico)
- Linear Technology LTC2983 (multi-tipo, precisione)
- Microchip MCP9600 (multi-tipo, I2C)

---

## PARTE 5: COSTANTI FISICHE E MATEMATICHE

### 5.1 Costanti Matematiche

| Costante | Simbolo | Valore (10 cifre) |
|----------|---------|-------------------|
| **Pi greco** | π | 3.1415926536 |
| **Numero di Eulero** | e | 2.7182818285 |
| **Sezione aurea** | φ | 1.6180339887 |
| **Radice di 2** | √2 | 1.4142135624 |
| **Radice di 3** | √3 | 1.7320508076 |
| **Radice di 5** | √5 | 2.2360679775 |

#### Definizioni

**π (Pi greco):**
- Rapporto tra circonferenza e diametro di un cerchio
- `π = C/d`

**e (Numero di Eulero):**
- Base del logaritmo naturale
- `e = lim(n→∞) (1 + 1/n)ⁿ`

**φ (Sezione aurea):**
- `φ = (1 + √5)/2`
- Rapporto aureo in arte e natura

---

### 5.2 Costanti Fisiche Fondamentali

| Costante | Simbolo | Valore | Unità |
|----------|---------|--------|-------|
| **Velocità della luce** (vuoto) | c | 299,792,458 | m/s |
| **Costante di Planck** | h | 6.62607015 × 10⁻³⁴ | J·s |
| **Costante gravitazionale** | G | 6.67430 × 10⁻¹¹ | m³/(kg·s²) |
| **Carica elementare** | e | 1.602176634 × 10⁻¹⁹ | C (coulomb) |
| **Costante di Boltzmann** | k_B | 1.380649 × 10⁻²³ | J/K |
| **Numero di Avogadro** | N_A | 6.02214076 × 10²³ | mol⁻¹ |
| **Costante dei gas ideali** | R | 8.314462618 | J/(mol·K) |
| **Massa elettrone** | m_e | 9.1093837015 × 10⁻³¹ | kg |
| **Massa protone** | m_p | 1.67262192369 × 10⁻²⁷ | kg |
| **Accelerazione gravità std** | g | 9.80665 | m/s² |
| **Permittività vuoto** | ε₀ | 8.8541878128 × 10⁻¹² | F/m |
| **Permeabilità vuoto** | μ₀ | 1.25663706212 × 10⁻⁶ | H/m |

---

### 5.3 Costanti in C/C++

**Standard <math.h> / <cmath>:**

```c
#include <math.h>

// Costanti disponibili (con -D_USE_MATH_DEFINES in alcuni compilatori)
M_E        // e = 2.71828...
M_LOG2E    // log₂(e)
M_LOG10E   // log₁₀(e)
M_LN2      // ln(2)
M_LN10     // ln(10)
M_PI       // π = 3.14159...
M_PI_2     // π/2
M_PI_4     // π/4
M_1_PI     // 1/π
M_2_PI     // 2/π
M_2_SQRTPI // 2/√π
M_SQRT2    // √2
M_SQRT1_2  // 1/√2
```

**Definizione manuale (se necessario):**

```c
#ifndef M_PI
    #define M_PI 3.14159265358979323846
#endif

#ifndef M_E
    #define M_E 2.71828182845904523536
#endif

// Costanti fisiche
#define SPEED_OF_LIGHT_M_S 299792458.0  // m/s
#define GRAVITY_M_S2 9.80665             // m/s²
#define AVOGADRO_MOL 6.02214076e23       // mol⁻¹
```

---

## 📝 NOTE FINALI

### Precisione dei Calcoli

- **Approssimativi:** π ≈ 3.14
- **Normali:** π ≈ 3.14159
- **Alta precisione:** Usare costanti `M_PI` del linguaggio

### Arrotondamenti

I valori di conversione sono arrotondati a 5-6 cifre significative per praticità. Per calcoli scientifici critici, usare più cifre.

### Sistemi di Unità

- **SI** (Sistema Internazionale): standard scientifico mondiale
- **Imperiale**: USA, UK parziale
- **CGS**: alcuni campi scientifici specifici

### Validità delle Formule

Tutte le formule geometriche assumono figure perfette in geometria euclidea. Nel mondo reale, misure possono variare per:
- Imperfezioni materiali
- Temperatura
- Pressione
- Tolleranze di fabbricazione

---

## 📚 RISORSE AGGIUNTIVE

### Per Programmatori

- **NIST Reference on Constants** - valori ufficiali costanti fisiche
- **Wolfram MathWorld** - formule matematiche
- **ISO 80000** - standard unità di misura

### Librerie C/C++

```c
#include <math.h>      // Funzioni matematiche, costanti
#include <tgmath.h>    // Type-generic math (C99)
#include <complex.h>   // Numeri complessi (C99)
```

---

## ⚖️ LICENZA E USO

📖 **Questo documento è materiale didattico.**

**Puoi:**
- ✅ Studiare e consultare liberamente
- ✅ Usare in progetti personali e commerciali
- ✅ Condividere con studenti e colleghi
- ✅ Implementare in codice (librerie, programmi)

**Nota:**
- ⚠️ Per applicazioni critiche (mediche, aerospaziali, industriali), verificare sempre i valori con fonti ufficiali (NIST, BIPM, ISO)
- ⚠️ Le formule termocoppie sono semplificate; per implementazioni reali usare tabelle NIST complete

---

## 📮 FEEDBACK

Hai trovato errori o imprecisioni? Hai suggerimenti per migliorare questo riferimento?

Questo documento è in continua evoluzione per servire meglio studenti, programmatori e ingegneri.

---

**Versione:** 2.0
**Formato:** Markdown
**Ultimo aggiornamento:** 2025
**Autore:** Materiale didattico per programmazione scientifica

---

## 🔗 LINK RAPIDI

- [Torna all'indice ↑](#-indice)
- [Figure Piane](#parte-1-figure-piane-2d)
- [Solidi 3D](#parte-2-solidi-3d)
- [Conversioni Fisiche](#parte-3-conversioni-fisiche)
- [Termocoppie](#parte-4-sensori-di-temperatura---termocoppie)
- [Costanti](#parte-5-costanti-fisiche-e-matematiche)

---

**📐 Buon calcolo e buona programmazione! 🚀**
