# 📘 MODULO 4 ALTERNATIVO
# Programmazione Python con Supporto di Intelligenza Artificiale
## Corso ITS - Dal Linguaggio Base all'IA Assistita
### Durata: 3 ore | Livello: Base-Intermedio

---

## 📑 Indice del Modulo

1. [Introduzione e Obiettivi](#1-introduzione-e-obiettivi)
2. [Fondamenti Python](#2-fondamenti-python)
3. [Strutture Dati Python](#3-strutture-dati-python)
4. [Funzioni e Moduli](#4-funzioni-e-moduli)
5. [Programmazione Orientata agli Oggetti](#5-programmazione-orientata-agli-oggetti)
6. [Gestione File e I/O](#6-gestione-file-e-io)
7. [Prompt Tecnici per Python](#7-prompt-tecnici-per-python)
8. [Librerie Essenziali](#8-librerie-essenziali)
9. [Progetti Completi Guidati](#9-progetti-completi-guidati)
10. [Testing e Debugging](#10-testing-e-debugging)
11. [Errori Comuni con IA in Python](#11-errori-comuni-con-ia-in-python)
12. [Best Practices Python](#12-best-practices-python)

---

## 1. Introduzione e Obiettivi

### 1.1 Perché Python

Python è il linguaggio più richiesto in ambito:
- **Data Science & AI** (machine learning, deep learning)
- **Automation** (scripting, DevOps)
- **Web Development** (Django, Flask)
- **Embedded** (Raspberry Pi, MicroPython)
- **Scientific Computing** (simulazioni, analisi)

**Caratteristiche chiave:**
- ✅ Sintassi leggibile e intuitiva
- ✅ Tipizzazione dinamica
- ✅ Ecosistema librerie enorme
- ✅ Cross-platform
- ✅ Ottimo per prototipazione rapida

### 1.2 Python vs C (Confronto per Studenti ITS)

```
┌─────────────────────────────────────────────┐
│         C              vs      PYTHON       │
├─────────────────────────────────────────────┤
│ Compilato              │  Interpretato      │
│ Tipizzazione statica   │  Dinamica          │
│ Gestione memoria man.  │  Automatica (GC)   │
│ Performance alta       │  Media (ma OK!)    │
│ Verboso                │  Conciso           │
│ Embedded/low-level     │  High-level/rapid  │
│                                              │
│ QUANDO USARE:                                │
│ C    → Embedded, OS, drivers, real-time     │
│ Python → Automation, ML, web, scripting     │
└─────────────────────────────────────────────┘
```

### 1.3 Obiettivi di Apprendimento

Al termine di questo modulo sarai in grado di:

✅ **Scrivere** programmi Python funzionali  
✅ **Usare** strutture dati appropriate (liste, dict, set)  
✅ **Creare** funzioni e moduli riutilizzabili  
✅ **Applicare** concetti OOP (classi, ereditarietà)  
✅ **Gestire** file e I/O  
✅ **Usare** IA per generare/debuggare codice Python  
✅ **Applicare** best practices PEP 8  
✅ **Testare** codice con unittest/pytest  
✅ **Integrare** librerie esterne  

### 1.4 Setup Ambiente

```bash
# 1. INSTALLA PYTHON (3.10+ raccomandato)
# Windows: https://python.org/downloads
# Linux: sudo apt install python3 python3-pip
# Mac: brew install python3

# 2. VERIFICA INSTALLAZIONE
python3 --version  # Output: Python 3.10.x o superiore
pip3 --version

# 3. INSTALLA IDE/EDITOR
# Opzione 1: VSCode + Python extension (raccomandato)
# Opzione 2: PyCharm Community Edition
# Opzione 3: Jupyter Notebook (per data science)

# 4. CREA VIRTUAL ENVIRONMENT (buona pratica)
python3 -m venv myproject_env
source myproject_env/bin/activate  # Linux/Mac
myproject_env\Scripts\activate     # Windows

# 5. INSTALLA STRUMENTI SVILUPPO
pip install black flake8 pytest ipython

# 6. TEST
python3 -c "print('Hello, Python!')"
```

---

## 2. Fondamenti Python

### 2.1 Sintassi Base

#### **Hello World e Commenti**

```python
# Questo è un commento singola riga

"""
Questo è un commento
multi-riga (docstring)
"""

# Print di base
print("Hello, World!")
print("Python", "è", "fantastico!")  # Output: Python è fantastico!

# Print formattato
name = "Mario"
age = 20
print(f"Ciao {name}, hai {age} anni")  # f-string (Python 3.6+)
print("Ciao {}, hai {} anni".format(name, age))  # format()
```

#### **Variabili e Tipi**

```python
# Python è TIPIZZAZIONE DINAMICA
# Non serve dichiarare tipo esplicitamente

# Interi
x = 10
y = -5
big_num = 1_000_000  # Underscore per leggibilità

# Float
pi = 3.14159
scientific = 1.5e-3  # Notazione scientifica: 0.0015

# Stringhe
name = "Python"
multiline = """Questa
è una stringa
multi-riga"""

# Booleani
is_active = True
is_done = False

# NoneType (equivalente NULL in C)
result = None

# Type checking
print(type(x))      # <class 'int'>
print(type(pi))     # <class 'float'>
print(isinstance(x, int))  # True
```

#### **Operatori**

```python
# ARITMETICI
a, b = 10, 3
print(a + b)   # 13 Addizione
print(a - b)   # 7  Sottrazione
print(a * b)   # 30 Moltiplicazione
print(a / b)   # 3.333... Divisione (float)
print(a // b)  # 3  Divisione intera
print(a % b)   # 1  Modulo
print(a ** b)  # 1000 Potenza

# CONFRONTO
print(a == b)  # False Uguaglianza
print(a != b)  # True  Diverso
print(a > b)   # True  Maggiore
print(a <= b)  # False Minore o uguale

# LOGICI
x, y = True, False
print(x and y)  # False AND
print(x or y)   # True  OR
print(not x)    # False NOT

# MEMBERSHIP
lista = [1, 2, 3]
print(2 in lista)      # True
print(5 not in lista)  # True

# IDENTITY
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)      # True (stesso oggetto)
print(a is c)      # False (oggetti diversi)
print(a == c)      # True (stesso valore)
```

### 2.2 Strutture Controllo

#### **If-Elif-Else**

```python
# IF BASE
age = 18
if age >= 18:
    print("Maggiorenne")
else:
    print("Minorenne")

# IF-ELIF-ELSE
score = 75
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"Voto: {grade}")

# OPERATORE TERNARIO
status = "adulto" if age >= 18 else "minore"

# MULTIPLE CONDITIONS
x = 15
if 10 <= x <= 20:  # Pythonic way!
    print("x è tra 10 e 20")

# ANY/ALL con condizioni
numbers = [2, 4, 6, 8]
if all(n % 2 == 0 for n in numbers):
    print("Tutti pari")

if any(n > 5 for n in numbers):
    print("Almeno uno > 5")
```

#### **Cicli For**

```python
# FOR BASE - iterazione su sequenza
fruits = ["mela", "banana", "arancia"]
for fruit in fruits:
    print(fruit)

# FOR con RANGE
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 8):  # 2, 3, 4, 5, 6, 7
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8 (step 2)
    print(i)

# ENUMERATE - accesso indice e valore
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# FOR con DIZIONARI
student = {"name": "Mario", "age": 20, "city": "Roma"}
for key in student:
    print(key)  # name, age, city

for key, value in student.items():
    print(f"{key}: {value}")

# LIST COMPREHENSION (Pythonic!)
squares = [x**2 for x in range(10)]
# Equivalente a:
# squares = []
# for x in range(10):
#     squares.append(x**2)

evens = [x for x in range(20) if x % 2 == 0]
```

#### **Cicli While**

```python
# WHILE BASE
count = 0
while count < 5:
    print(count)
    count += 1

# WHILE TRUE con break
while True:
    user_input = input("Inserisci 'quit' per uscire: ")
    if user_input == 'quit':
        break
    print(f"Hai scritto: {user_input}")

# CONTINUE
for i in range(10):
    if i % 2 == 0:
        continue  # Salta numeri pari
    print(i)  # Stampa solo dispari

# ELSE con cicli (feature unica Python!)
for i in range(5):
    if i == 10:
        break
else:
    # Eseguito se loop completa SENZA break
    print("Loop completato normalmente")
```

### 2.3 Input/Output Base

```python
# INPUT (sempre stringa)
name = input("Come ti chiami? ")
print(f"Ciao {name}!")

# Conversione tipo
age = int(input("Età: "))
height = float(input("Altezza (m): "))

# Input validation
while True:
    try:
        num = int(input("Inserisci numero: "))
        break
    except ValueError:
        print("Errore: inserisci un numero valido!")

# OUTPUT formattato
# f-string (Python 3.6+, RACCOMANDATO)
print(f"Nome: {name}, Età: {age}")
print(f"Pi greco: {3.14159:.2f}")  # 3.14 (2 decimali)
print(f"Numero: {42:05d}")  # 00042 (padding)
print(f"Percentuale: {0.856:.1%}")  # 85.6%

# format()
print("Nome: {}, Età: {}".format(name, age))

# % formatting (vecchio stile, evitare)
print("Nome: %s, Età: %d" % (name, age))
```

---

## 3. Strutture Dati Python

### 3.1 Liste (List)

```python
# CREAZIONE
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]  # Tipi misti OK
empty = []
nested = [[1, 2], [3, 4], [5, 6]]

# ACCESSO
print(numbers[0])    # 1 (primo)
print(numbers[-1])   # 5 (ultimo)
print(numbers[1:3])  # [2, 3] (slicing)
print(numbers[:3])   # [1, 2, 3] (primi 3)
print(numbers[2:])   # [3, 4, 5] (dal 3° in poi)
print(numbers[::2])  # [1, 3, 5] (ogni 2)
print(numbers[::-1]) # [5, 4, 3, 2, 1] (reverse)

# MODIFICA (liste sono MUTABILI)
numbers[0] = 10
numbers[1:3] = [20, 30]
print(numbers)  # [10, 20, 30, 4, 5]

# METODI
numbers = [1, 2, 3]
numbers.append(4)        # Aggiungi alla fine
numbers.insert(0, 0)     # Inserisci in posizione
numbers.extend([5, 6])   # Aggiungi lista
numbers.remove(3)        # Rimuovi per valore
popped = numbers.pop()   # Rimuovi e ritorna ultimo
popped = numbers.pop(0)  # Rimuovi e ritorna indice 0
numbers.clear()          # Svuota lista

# ORDINAMENTO
nums = [3, 1, 4, 1, 5]
nums.sort()              # In-place (modifica originale)
print(nums)              # [1, 1, 3, 4, 5]

nums = [3, 1, 4, 1, 5]
sorted_nums = sorted(nums)  # Ritorna nuova lista
print(nums)              # [3, 1, 4, 1, 5] (originale intatta)
print(sorted_nums)       # [1, 1, 3, 4, 5]

# RICERCA
print(3 in nums)         # True
print(nums.index(4))     # 2 (indice di 4)
print(nums.count(1))     # 2 (quanti 1)

# COPIA
original = [1, 2, 3]
shallow = original       # ⚠️ Riferimento, non copia!
shallow[0] = 99
print(original)          # [99, 2, 3] - modificato!

original = [1, 2, 3]
copy = original.copy()   # ✅ Copia reale
# oppure: copy = original[:]
# oppure: copy = list(original)
copy[0] = 99
print(original)          # [1, 2, 3] - OK!

# OPERAZIONI
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2      # [1, 2, 3, 4, 5, 6]
repeated = list1 * 3          # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# FUNZIONI UTILI
nums = [1, 2, 3, 4, 5]
print(len(nums))         # 5
print(sum(nums))         # 15
print(min(nums))         # 1
print(max(nums))         # 5
```

### 3.2 Tuple

```python
# CREAZIONE (immutabili!)
coords = (10, 20)
single = (42,)  # ⚠️ Virgola necessaria per singolo elemento!
no_parens = 10, 20  # Parentesi opzionali
empty = ()

# ACCESSO (come liste)
print(coords[0])     # 10
print(coords[-1])    # 20

# UNPACKING
x, y = coords
print(x, y)  # 10 20

# Swap in una riga!
a, b = 10, 20
a, b = b, a  # Swap pythonic
print(a, b)  # 20 10

# Tuple sono IMMUTABILI
# coords[0] = 15  # ❌ TypeError!

# QUANDO USARE TUPLE vs LISTE
# Tuple: Dati immutabili, coordinate, return multipli
# Liste: Collezioni modificabili, dati omogenei

# Return multipli da funzione
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

minimum, maximum, total = get_stats([1, 2, 3, 4, 5])
```

### 3.3 Dizionari (Dict)

```python
# CREAZIONE (key-value pairs)
student = {
    "name": "Mario",
    "age": 20,
    "courses": ["Python", "C", "Arduino"]
}

# Dizionario vuoto
empty = {}
empty_dict = dict()

# ACCESSO
print(student["name"])       # "Mario"
print(student.get("age"))    # 20
print(student.get("grade", "N/A"))  # "N/A" (default se non esiste)

# MODIFICA
student["age"] = 21          # Modifica esistente
student["city"] = "Roma"     # Aggiungi nuova chiave

# RIMOZIONE
del student["city"]          # Rimuovi chiave
popped = student.pop("age")  # Rimuovi e ritorna valore
# student.clear()            # Svuota dizionario

# METODI
keys = student.keys()        # dict_keys(['name', 'courses'])
values = student.values()    # dict_values(['Mario', [...]])
items = student.items()      # dict_items([('name', 'Mario'), ...])

# ITERAZIONE
for key in student:
    print(key, student[key])

for key, value in student.items():
    print(f"{key}: {value}")

# ESISTENZA CHIAVE
if "name" in student:
    print("Nome presente")

# DICT COMPREHENSION
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# UPDATE (merge dizionari)
defaults = {"theme": "dark", "lang": "en"}
user_prefs = {"theme": "light"}
defaults.update(user_prefs)  # defaults ora ha theme="light"

# NESTED DICTS
students = {
    "001": {"name": "Mario", "grade": 28},
    "002": {"name": "Luigi", "grade": 30}
}
print(students["001"]["name"])  # Mario
```

### 3.4 Set

```python
# CREAZIONE (elementi unici, non ordinati)
numbers = {1, 2, 3, 4, 5}
empty_set = set()  # ⚠️ {} è dict vuoto, non set!
from_list = set([1, 2, 2, 3, 3])  # {1, 2, 3} - duplicati rimossi

# OPERAZIONI
numbers.add(6)           # Aggiungi elemento
numbers.remove(3)        # Rimuovi (errore se non esiste)
numbers.discard(3)       # Rimuovi (nessun errore se non esiste)
numbers.clear()          # Svuota set

# OPERAZIONI INSIEMISTICHE
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

union = a | b            # {1, 2, 3, 4, 5, 6, 7, 8}
intersection = a & b     # {4, 5}
difference = a - b       # {1, 2, 3}
sym_diff = a ^ b         # {1, 2, 3, 6, 7, 8}

# METODI
union = a.union(b)
inter = a.intersection(b)
diff = a.difference(b)

# TEST APPARTENENZA (velocissimo!)
print(3 in a)            # True - O(1) average!

# CASO D'USO: Rimozione duplicati
numbers = [1, 2, 2, 3, 3, 4]
unique = list(set(numbers))  # [1, 2, 3, 4]

# SET COMPREHENSION
evens = {x for x in range(10) if x % 2 == 0}
```

### 3.5 Confronto Strutture Dati

```python
"""
QUANDO USARE COSA?

LIST []
- Collezione ordinata
- Elementi duplicati OK
- Accesso per indice
- Modificabile
Esempio: [1, 2, 3, 2, 1]

TUPLE ()
- Collezione ordinata IMMUTABILE
- Return multipli funzioni
- Chiavi dizionari
- Dati che non devono cambiare
Esempio: (10, 20), ("Mario", 20, "Roma")

DICT {key: value}
- Associazioni key-value
- Accesso per chiave (non indice)
- Chiavi uniche
- Lookup veloce O(1)
Esempio: {"name": "Mario", "age": 20}

SET {elementi}
- Collezione non ordinata
- Elementi UNICI
- Operazioni insiemistiche
- Test appartenenza veloce
Esempio: {1, 2, 3, 4, 5}
"""

# PERFORMANCE
import time

# List: ricerca lenta per grandi dataset
big_list = list(range(100000))
start = time.time()
99999 in big_list  # O(n)
print(f"List: {time.time() - start:.4f}s")

# Set: ricerca velocissima
big_set = set(range(100000))
start = time.time()
99999 in big_set  # O(1) average
print(f"Set: {time.time() - start:.4f}s")
```

---

## 4. Funzioni e Moduli

### 4.1 Definizione Funzioni

```python
# FUNZIONE BASE
def greet(name):
    """Saluta una persona per nome."""  # Docstring
    print(f"Ciao {name}!")

greet("Mario")  # Chiamata

# PARAMETRI DEFAULT
def greet(name, greeting="Ciao"):
    print(f"{greeting} {name}!")

greet("Mario")              # Ciao Mario!
greet("Luigi", "Buongiorno")  # Buongiorno Luigi!

# RETURN
def add(a, b):
    return a + b

result = add(3, 5)  # 8

# Return multipli (in realtà ritorna tupla)
def stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

minimum, maximum, total = stats([1, 2, 3, 4, 5])

# RETURN EARLY (guard clauses)
def divide(a, b):
    if b == 0:
        return None  # Early return se errore
    return a / b

# PARAMETRI KEYWORD
def create_user(name, age, city="Unknown"):
    return {"name": name, "age": age, "city": city}

# Chiamate equivalenti:
user = create_user("Mario", 20, "Roma")
user = create_user(name="Mario", age=20, city="Roma")
user = create_user(age=20, name="Mario")  # Ordine irrilevante con keyword

# *args - argomenti variabili posizionali
def sum_all(*args):
    """Somma qualsiasi numero di argomenti."""
    return sum(args)

print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5))  # 15

# **kwargs - argomenti variabili keyword
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Mario", age=20, city="Roma")

# COMBINAZIONE
def complex_func(required, *args, default="value", **kwargs):
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Default: {default}")
    print(f"Kwargs: {kwargs}")

complex_func("must", 1, 2, 3, default="custom", extra="data")
```

### 4.2 Lambda Functions

```python
# LAMBDA - funzioni anonime inline
square = lambda x: x**2
print(square(5))  # 25

# Equivalente a:
def square(x):
    return x**2

# USO TIPICO: con map, filter, sorted
numbers = [1, 2, 3, 4, 5]

# map() - applica funzione a ogni elemento
squares = list(map(lambda x: x**2, numbers))
# [1, 4, 9, 16, 25]

# filter() - filtra elementi
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4]

# sorted() con key
students = [
    {"name": "Mario", "grade": 28},
    {"name": "Luigi", "grade": 30},
    {"name": "Anna", "grade": 25}
]
sorted_students = sorted(students, key=lambda s: s["grade"], reverse=True)
# Ordinati per voto decrescente

# QUANDO USARE LAMBDA
# ✅ Funzioni semplici, una riga
# ✅ Callback/sorting keys
# ❌ Logica complessa (usa def)
```

### 4.3 Moduli

```python
# CREARE MODULO
# File: math_utils.py
"""Utility matematiche."""

def add(a, b):
    """Somma due numeri."""
    return a + b

def multiply(a, b):
    """Moltiplica due numeri."""
    return a * b

PI = 3.14159

# USARE MODULO
# File: main.py

# Import intero modulo
import math_utils
result = math_utils.add(3, 5)
print(math_utils.PI)

# Import specifico
from math_utils import add, PI
result = add(3, 5)

# Import con alias
import math_utils as mu
result = mu.add(3, 5)

# Import tutto (sconsigliato!)
from math_utils import *

# LIBRERIA STANDARD
import math
print(math.sqrt(16))    # 4.0
print(math.pi)          # 3.141592653589793

import random
print(random.randint(1, 10))  # Numero casuale 1-10
print(random.choice(['a', 'b', 'c']))  # Elemento casuale

import datetime
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

import os
print(os.getcwd())      # Directory corrente
files = os.listdir('.')  # Lista file directory

import sys
print(sys.version)      # Versione Python
print(sys.argv)         # Argomenti linea comando

# __name__ trick
# File: my_module.py
def main():
    print("Eseguito come script")

if __name__ == "__main__":
    # Eseguito solo se file è script principale
    # Non eseguito se importato come modulo
    main()
```

### 4.4 Packages

```
Struttura Package:

mypackage/
├── __init__.py       # Rende directory un package
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py
```

```python
# __init__.py (può essere vuoto o contenere inizializzazione)
from .module1 import function1
from .module2 import function2

__all__ = ['function1', 'function2']  # Cosa esporta "from package import *"

# Uso
from mypackage import function1
# oppure
import mypackage.module1
result = mypackage.module1.function1()
```

---

## 5. Programmazione Orientata agli Oggetti

### 5.1 Classi Base

```python
# DEFINIZIONE CLASSE
class Student:
    """Rappresenta uno studente."""
    
    # Class variable (condivisa da tutte le istanze)
    school = "ITS Informatica"
    
    # Constructor
    def __init__(self, name, age, student_id):
        """Inizializza studente."""
        # Instance variables (specifiche per istanza)
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = []
    
    # Instance method
    def add_grade(self, grade):
        """Aggiunge voto."""
        if 0 <= grade <= 30:
            self.grades.append(grade)
        else:
            raise ValueError("Voto deve essere 0-30")
    
    def average_grade(self):
        """Calcola media voti."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def __str__(self):
        """String representation."""
        return f"Student({self.name}, {self.age})"
    
    def __repr__(self):
        """Developer representation."""
        return f"Student('{self.name}', {self.age}, '{self.student_id}')"

# CREARE OGGETTI
student1 = Student("Mario", 20, "S001")
student2 = Student("Luigi", 21, "S002")

# Accesso attributi
print(student1.name)        # Mario
print(student1.school)      # ITS Informatica

# Chiamata metodi
student1.add_grade(28)
student1.add_grade(30)
student1.add_grade(25)
print(student1.average_grade())  # 27.666...

# String representation
print(student1)         # Student(Mario, 20)
print(repr(student1))   # Student('Mario', 20, 'S001')
```

### 5.2 Incapsulamento

```python
class BankAccount:
    """Conto bancario con saldo privato."""
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private (name mangling)
    
    def deposit(self, amount):
        """Deposita denaro."""
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        """Preleva denaro."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    
    @property  # Getter
    def balance(self):
        """Ritorna saldo (read-only)."""
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        """Setter con validazione."""
        if value < 0:
            raise ValueError("Saldo non può essere negativo")
        self.__balance = value

# Uso
account = BankAccount("Mario", 1000)
account.deposit(500)
print(account.balance)  # 1500 - accesso via property

# account.__balance  # ❌ AttributeError (privato!)
# Ma Python non è davvero privato:
# print(account._BankAccount__balance)  # 1500 - name mangling

# Property setter
# account.balance = -100  # ❌ ValueError
account.balance = 2000    # ✅ OK
```

### 5.3 Ereditarietà

```python
# CLASSE BASE
class Person:
    """Persona generica."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Ciao, sono {self.name} e ho {self.age} anni"

# CLASSE DERIVATA
class Student(Person):
    """Studente (eredita da Person)."""
    
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Chiama constructor base
        self.student_id = student_id
        self.grades = []
    
    def introduce(self):
        # Override metodo base
        base_intro = super().introduce()
        return f"{base_intro}. Sono studente {self.student_id}"
    
    def add_grade(self, grade):
        self.grades.append(grade)

# EREDITARIETÀ MULTIPLA
class Employee:
    def __init__(self, employee_id, salary):
        self.employee_id = employee_id
        self.salary = salary
    
    def work(self):
        return f"Lavoro come dipendente {self.employee_id}"

class StudentEmployee(Student, Employee):
    """Studente lavoratore."""
    
    def __init__(self, name, age, student_id, employee_id, salary):
        Student.__init__(self, name, age, student_id)
        Employee.__init__(self, employee_id, salary)
    
    def introduce(self):
        return f"{super().introduce()} e lavoro part-time"

# USO
person = Person("Anna", 30)
print(person.introduce())

student = Student("Mario", 20, "S001")
print(student.introduce())
student.add_grade(28)

# Check tipo
print(isinstance(student, Student))  # True
print(isinstance(student, Person))   # True (eredita)
print(issubclass(Student, Person))   # True
```

### 5.4 Metodi Speciali (Magic Methods)

```python
class Vector:
    """Vettore 2D con operator overloading."""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """String per utenti."""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """String per sviluppatori."""
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        """Overload operatore +"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Overload operatore -"""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Overload operatore * (scalare)"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        """Overload operatore =="""
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        """Overload len()"""
        return 2  # Vettore 2D
    
    def __getitem__(self, index):
        """Overload indicizzazione []"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")

# USO
v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)       # Vector(4, 6)
print(v1 * 3)        # Vector(3, 6)
print(v1 == v2)      # False
print(len(v1))       # 2
print(v1[0], v1[1])  # 1 2

# Altri magic methods utili:
# __call__()     - rende oggetto callable come funzione
# __enter__/__exit__() - context manager (with statement)
# __iter__/__next__() - rendere oggetto iterabile
# __lt__, __le__, __gt__, __ge__ - comparison operators
```

---

## 6. Gestione File e I/O

### 6.1 Lettura/Scrittura File

```python
# SCRITTURA FILE
# Metodo 1: Manuale (NON raccomandato)
file = open("output.txt", "w")
file.write("Ciao mondo!\n")
file.close()  # ⚠️ Devi ricordare di chiudere!

# Metodo 2: Context Manager (RACCOMANDATO)
with open("output.txt", "w") as file:
    file.write("Ciao mondo!\n")
    file.write("Seconda riga\n")
# File chiuso automaticamente anche in caso di errore!

# LETTURA FILE
# Leggi tutto
with open("input.txt", "r") as file:
    content = file.read()
    print(content)

# Leggi riga per riga
with open("input.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() rimuove \n

# Leggi tutte le righe in lista
with open("input.txt", "r") as file:
    lines = file.readlines()
    # lines = ['riga1\n', 'riga2\n', ...]

# MODALITÀ APERTURA
# 'r'  - Read (default)
# 'w'  - Write (sovrascrive!)
# 'a'  - Append (aggiunge alla fine)
# 'r+' - Read & Write
# 'b'  - Binary mode (es. 'rb', 'wb')

# APPEND
with open("log.txt", "a") as file:
    file.write("Nuova entry di log\n")

# FILE BINARI
with open("image.png", "rb") as file:
    data = file.read()

with open("copy.png", "wb") as file:
    file.write(data)
```

### 6.2 Gestione CSV

```python
import csv

# SCRITTURA CSV
data = [
    ["Nome", "Età", "Città"],
    ["Mario", 20, "Roma"],
    ["Luigi", 21, "Milano"],
    ["Anna", 19, "Napoli"]
]

with open("students.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)  # Scrive tutte le righe
    # oppure:
    # for row in data:
    #     writer.writerow(row)

# LETTURA CSV
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # ['Mario', '20', 'Roma']

# CSV CON DIZIONARI (più pythonic!)
data = [
    {"name": "Mario", "age": 20, "city": "Roma"},
    {"name": "Luigi", "age": 21, "city": "Milano"}
]

with open("students.csv", "w", newline='') as file:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

# Lettura con dizionari
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["age"])
```

### 6.3 Gestione JSON

```python
import json

# SCRITTURA JSON
data = {
    "students": [
        {"name": "Mario", "age": 20, "grades": [28, 30, 25]},
        {"name": "Luigi", "age": 21, "grades": [27, 29, 26]}
    ],
    "school": "ITS Informatica"
}

# Scrivi su file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)  # indent=4 per formato leggibile

# Converti a stringa JSON
json_string = json.dumps(data, indent=2)
print(json_string)

# LETTURA JSON
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data["students"][0]["name"])  # Mario

# Parse stringa JSON
json_string = '{"name": "Mario", "age": 20}'
data = json.loads(json_string)
print(data["name"])  # Mario

# GESTIONE ERRORI
try:
    with open("data.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    print("File non trovato")
except json.JSONDecodeError:
    print("JSON non valido")
```

### 6.4 Gestione Path e Directory

```python
import os
from pathlib import Path  # Moderno (Python 3.4+)

# OS MODULE (vecchio stile)
current_dir = os.getcwd()
print(current_dir)

os.chdir("/path/to/directory")  # Cambia directory

files = os.listdir(".")  # Lista file
for file in files:
    print(file)

# Check esistenza
if os.path.exists("file.txt"):
    print("Esiste")

if os.path.isfile("file.txt"):
    print("È un file")

if os.path.isdir("directory"):
    print("È una directory")

# Crea directory
os.mkdir("new_dir")  # Singola directory
os.makedirs("path/to/nested/dir")  # Con parents

# Rimuovi
os.remove("file.txt")   # Rimuovi file
os.rmdir("empty_dir")   # Rimuovi directory vuota

# Path operations
file_path = "data/students.csv"
dir_name = os.path.dirname(file_path)   # "data"
base_name = os.path.basename(file_path) # "students.csv"
name, ext = os.path.splitext(base_name) # ("students", ".csv")

# PATHLIB (moderno, raccomandato!)
path = Path("data/students.csv")

# Proprietà
print(path.name)       # "students.csv"
print(path.stem)       # "students"
print(path.suffix)     # ".csv"
print(path.parent)     # Path("data")
print(path.absolute()) # Path assoluto

# Check
print(path.exists())
print(path.is_file())
print(path.is_dir())

# Operazioni
path.mkdir(parents=True, exist_ok=True)  # Crea dir

# Iterare file
data_dir = Path("data")
for file in data_dir.iterdir():
    if file.is_file():
        print(file)

# Glob pattern
for txt_file in data_dir.glob("*.txt"):
    print(txt_file)

# Lettura/scrittura
path = Path("output.txt")
path.write_text("Contenuto file")
content = path.read_text()

# Join paths (cross-platform!)
base = Path("data")
file_path = base / "students" / "info.txt"  # Operatore /!
print(file_path)  # data/students/info.txt
```

---

## 7. Prompt Tecnici per Python

### 7.1 Template Funzione Base

```
Scrivi in Python 3.10+ una funzione:

FIRMA:
def nome_funzione(parametri) -> tipo_ritorno:

COMPORTAMENTO:
- [Cosa fa]
- [Gestione errori/edge cases]
- [Tipo ritorno e quando]

VINCOLI:
- Python 3.10+
- Type hints
- Docstring Google style
- Gestione esplicita eccezioni

OUTPUT RICHIESTO:
1. Funzione completa con:
   - Type hints
   - Docstring dettagliato
   - Gestione errori
   - Esempi d'uso in docstring
2. Almeno 5 test con pytest:
   - Casi normali (2)
   - Edge cases (2)
   - Casi errore (1)

ESEMPIO USO:
[Mostra chiamata tipica con output]
```

**Esempio Compilato:**

```
Scrivi in Python 3.10+ una funzione:

FIRMA:
def calculate_average(numbers: list[float]) -> float:

COMPORTAMENTO:
- Calcola media aritmetica di lista numeri
- Solleva ValueError se lista vuota
- Gestisce liste con negativi, zero, float

VINCOLI:
- Python 3.10+ (usa list[float] non List[float])
- Type hints completi
- Docstring Google style
- raise ValueError per input invalidi

OUTPUT RICHIESTO:
[come template]

ESEMPIO USO:
avg = calculate_average([1.5, 2.5, 3.0])
print(avg)  # 2.333...
```

### 7.2 Template Classe

```
Scrivi in Python 3.10+ una classe:

NOME CLASSE: [NomeClasse]

ATTRIBUTI:
- [attributo1]: [tipo] - [descrizione]
- [attributo2]: [tipo] - [descrizione]

METODI RICHIESTI:
1. __init__(self, ...) - costruttore
2. [metodo1](self, ...) - [cosa fa]
3. [metodo2](self, ...) - [cosa fa]
4. __str__(self) - rappresentazione stringa
5. __repr__(self) - rappresentazione debug

COMPORTAMENTO:
- [Funzionalità chiave]
- [Validazioni]
- [Edge cases]

VINCOLI:
- Type hints completi
- Docstring per classe e ogni metodo
- Properties per attributi privati (se necessario)
- Magic methods appropriati

OUTPUT:
1. Classe completa
2. Script esempio d'uso
3. Test unittest/pytest (5+ test)
```

### 7.3 Template Script Completo

```
Scrivi script Python per [SCOPO].

FUNZIONALITÀ:
1. [Feature 1]
2. [Feature 2]
3. [Feature 3]

INPUT:
- [Fonte dati: file/stdin/API]
- [Formato]

OUTPUT:
- [Destinazione: file/stdout/database]
- [Formato]

STRUTTURA RICHIESTA:
- Funzioni separate per ogni task
- main() come entry point
- if __name__ == "__main__": main()
- Gestione argomenti CLI (argparse)
- Logging appropriato
- Error handling robusto

VINCOLI:
- Python 3.10+
- Solo libreria standard (o specifica quali esterne)
- Docstring per ogni funzione
- Type hints

ESEMPIO ESECUZIONE:
python script.py --input data.csv --output result.json
```

### 7.4 Template Debugging

```
Ho questo codice Python che non funziona:

```python
[PASTE CODICE]
```

PROBLEMA OSSERVATO:
[Errore/comportamento anomalo]

TRACEBACK (se presente):
[Stack trace completo]

INPUT TEST:
[Input che causa problema]

OUTPUT ATTESO:
[Cosa dovrebbe fare]

OUTPUT OTTENUTO:
[Cosa fa invece]

COMPITI:
1. Identifica TUTTI i bug
2. Spiega PERCHÉ ogni bug causa il problema
3. Fornisci versione corretta
4. Suggerisci come prevenire bug simili
5. Aggiungi test che catturerebbero il bug
```

### 7.5 Template Ottimizzazione

```
Ho questo codice Python funzionante ma lento:

```python
[CODICE]
```

PROFILING (se disponibile):
[Output cProfile o tempo esecuzione]

DIMENSIONI DATI:
[Es: lista 1M elementi, file 100MB, etc]

OBIETTIVO OTTIMIZZAZIONE:
- Target: ridurre tempo da [X] a [Y]
- Vincoli memoria: [limite]
- Vincoli compatibilità: [versione Python, librerie]

COMPITI:
1. Analizza complessità attuale (Big O)
2. Identifica bottleneck
3. Proponi ottimizzazioni specifiche:
   - Algoritmi più efficienti
   - Strutture dati migliori
   - Caching
   - Parallelizzazione (se applicabile)
4. Fornisci codice ottimizzato
5. Benchmarking: confronta prima/dopo
```

---

## 8. Librerie Essenziali

### 8.1 NumPy (Calcolo Numerico)

```python
import numpy as np

# CREAZIONE ARRAY
arr = np.array([1, 2, 3, 4, 5])
print(arr)  # [1 2 3 4 5]
print(type(arr))  # <class 'numpy.ndarray'>

# Array multidimensionale
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(matrix.shape)  # (2, 3)

# Array speciali
zeros = np.zeros((3, 3))      # Matrice 3x3 di zeri
ones = np.ones((2, 4))        # Matrice 2x4 di uni
identity = np.eye(3)          # Matrice identità 3x3
random = np.random.rand(3, 3) # Matrice random 3x3

# Range
arr = np.arange(0, 10, 2)     # [0 2 4 6 8]
arr = np.linspace(0, 1, 5)    # [0.   0.25 0.5  0.75 1.  ]

# OPERAZIONI (element-wise, velocissime!)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)   # [5 7 9]
print(a * b)   # [4 10 18]
print(a ** 2)  # [1 4 9]

# STATISTICHE
arr = np.array([1, 2, 3, 4, 5])
print(arr.mean())   # 3.0
print(arr.std())    # 1.414...
print(arr.min())    # 1
print(arr.max())    # 5
print(arr.sum())    # 15

# INDICIZZAZIONE
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(matrix[0, 1])    # 2
print(matrix[:, 1])    # [2 5 8] (colonna)
print(matrix[1, :])    # [4 5 6] (riga)
print(matrix[0:2, 1:3])  # [[2 3]
                         #  [5 6]]

# BROADCASTING
arr = np.array([1, 2, 3])
print(arr * 2)  # [2 4 6]

# PERCHÉ NumPy?
# Liste Python vs NumPy array
import time

# Liste (lente)
list_a = list(range(1000000))
start = time.time()
list_c = [a * 2 for a in list_a]
print(f"List: {time.time() - start:.4f}s")

# NumPy (veloce!)
arr_a = np.arange(1000000)
start = time.time()
arr_c = arr_a * 2
print(f"NumPy: {time.time() - start:.4f}s")
# NumPy è ~50-100x più veloce!
```

### 8.2 Pandas (Data Analysis)

```python
import pandas as pd

# CREARE DATAFRAME
data = {
    'Name': ['Mario', 'Luigi', 'Anna'],
    'Age': [20, 21, 19],
    'Grade': [28, 30, 27]
}
df = pd.DataFrame(data)
print(df)
#     Name  Age  Grade
# 0  Mario   20     28
# 1  Luigi   21     30
# 2   Anna   19     27

# LEGGERE CSV
df = pd.read_csv('students.csv')

# SCRIVERE CSV
df.to_csv('output.csv', index=False)

# INFO BASE
print(df.head())       # Prime 5 righe
print(df.tail())       # Ultime 5 righe
print(df.info())       # Info colonne/tipi
print(df.describe())   # Statistiche numeriche
print(df.shape)        # (righe, colonne)

# ACCESSO DATI
print(df['Name'])             # Colonna singola (Series)
print(df[['Name', 'Age']])    # Colonne multiple (DataFrame)
print(df.loc[0])              # Riga per label/index
print(df.iloc[0])             # Riga per posizione
print(df.iloc[0:2, 1:3])      # Slicing

# FILTRAGGIO
high_grades = df[df['Grade'] >= 28]
young_students = df[df['Age'] < 21]
combined = df[(df['Age'] < 21) & (df['Grade'] > 27)]

# ORDINAMENTO
sorted_df = df.sort_values('Grade', ascending=False)

# AGGREGAZIONI
print(df['Grade'].mean())    # Media voti
print(df['Age'].min())       # Età minima
print(df.groupby('Age')['Grade'].mean())  # Media per età

# AGGIUNGERE COLONNE
df['Pass'] = df['Grade'] >= 18
df['Grade_Squared'] = df['Grade'] ** 2

# MISSING DATA
df.dropna()              # Rimuovi righe con NaN
df.fillna(0)             # Riempi NaN con 0
df['Age'].fillna(df['Age'].mean())  # Fill con media

# MERGE/JOIN
df1 = pd.DataFrame({'ID': [1, 2], 'Name': ['Mario', 'Luigi']})
df2 = pd.DataFrame({'ID': [1, 2], 'Grade': [28, 30]})
merged = pd.merge(df1, df2, on='ID')
```

### 8.3 Requests (HTTP)

```python
import requests

# GET REQUEST
response = requests.get('https://api.github.com')
print(response.status_code)  # 200
print(response.json())        # Parse JSON automaticamente

# Con parametri
params = {'q': 'python', 'sort': 'stars'}
response = requests.get('https://api.github.com/search/repositories', 
                       params=params)

# Headers personalizzati
headers = {'User-Agent': 'MyApp/1.0'}
response = requests.get('https://api.github.com', headers=headers)

# POST REQUEST
data = {'username': 'mario', 'password': 'secret'}
response = requests.post('https://example.com/login', data=data)

# JSON POST
json_data = {'key': 'value'}
response = requests.post('https://api.example.com', json=json_data)

# GESTIONE ERRORI
try:
    response = requests.get('https://api.example.com', timeout=5)
    response.raise_for_status()  # Solleva eccezione se 4xx/5xx
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Errore: {e}")

# DOWNLOAD FILE
url = 'https://example.com/file.pdf'
response = requests.get(url)
with open('downloaded.pdf', 'wb') as f:
    f.write(response.content)
```

### 8.4 Altre Librerie Utili

```python
# DATETIME avanzato
from datetime import datetime, timedelta

now = datetime.now()
yesterday = now - timedelta(days=1)
print(yesterday.strftime('%Y-%m-%d'))

# COLLECTIONS (strutture dati extra)
from collections import Counter, defaultdict, namedtuple

# Counter - conta elementi
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counts = Counter(words)
print(counts['apple'])  # 3
print(counts.most_common(2))  # [('apple', 3), ('banana', 2)]

# defaultdict - dict con valori default
from collections import defaultdict
word_freq = defaultdict(int)  # default 0
for word in words:
    word_freq[word] += 1

# namedtuple - tuple con nomi
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)  # 10 20

# ITERTOOLS (iteratori efficienti)
from itertools import combinations, permutations, product

# Combinazioni
print(list(combinations([1, 2, 3], 2)))  # [(1, 2), (1, 3), (2, 3)]

# Prodotto cartesiano
print(list(product([1, 2], ['a', 'b'])))  # [(1,'a'),(1,'b'),(2,'a'),(2,'b')]

# RE (Regular Expressions)
import re

text = "Email: mario@example.com"
email = re.search(r'[\w\.-]+@[\w\.-]+', text)
print(email.group())  # mario@example.com

# ARGPARSE (CLI arguments)
import argparse

parser = argparse.ArgumentParser(description='My script')
parser.add_argument('--input', required=True, help='Input file')
parser.add_argument('--verbose', action='store_true')
args = parser.parse_args()

print(args.input)
if args.verbose:
    print("Verbose mode")
```

---

## 9. Progetti Completi Guidati

### 9.1 Progetto: Gestione Studenti CLI

```python
"""
Sistema gestione studenti da linea comando.
Funzionalità:
- Aggiungi studente
- Lista studenti
- Cerca studente
- Aggiorna voti
- Statistiche
- Persistenza JSON
"""

import json
from pathlib import Path
from typing import List, Optional

# === CLASSE STUDENT ===
class Student:
    """Rappresenta uno studente."""
    
    def __init__(self, student_id: str, name: str, age: int):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grades: List[int] = []
    
    def add_grade(self, grade: int) -> None:
        """Aggiunge voto (0-30)."""
        if not 0 <= grade <= 30:
            raise ValueError("Voto deve essere tra 0 e 30")
        self.grades.append(grade)
    
    def average_grade(self) -> float:
        """Calcola media voti."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)
    
    def to_dict(self) -> dict:
        """Converte a dizionario per JSON."""
        return {
            'student_id': self.student_id,
            'name': self.name,
            'age': self.age,
            'grades': self.grades
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Student':
        """Crea Student da dizionario."""
        student = cls(data['student_id'], data['name'], data['age'])
        student.grades = data.get('grades', [])
        return student
    
    def __str__(self) -> str:
        avg = self.average_grade()
        return f"{self.student_id} - {self.name} ({self.age} anni) - Media: {avg:.2f}"

# === CLASSE DATABASE ===
class StudentDatabase:
    """Gestisce collezione studenti con persistenza."""
    
    def __init__(self, filepath: str = "students.json"):
        self.filepath = Path(filepath)
        self.students: dict[str, Student] = {}
        self.load()
    
    def add_student(self, student: Student) -> None:
        """Aggiunge studente."""
        if student.student_id in self.students:
            raise ValueError(f"Studente {student.student_id} già esistente")
        self.students[student.student_id] = student
        self.save()
    
    def get_student(self, student_id: str) -> Optional[Student]:
        """Recupera studente per ID."""
        return self.students.get(student_id)
    
    def list_students(self) -> List[Student]:
        """Ritorna lista tutti studenti."""
        return list(self.students.values())
    
    def remove_student(self, student_id: str) -> bool:
        """Rimuove studente."""
        if student_id in self.students:
            del self.students[student_id]
            self.save()
            return True
        return False
    
    def search_by_name(self, name: str) -> List[Student]:
        """Cerca studenti per nome (case-insensitive)."""
        name_lower = name.lower()
        return [s for s in self.students.values() 
                if name_lower in s.name.lower()]
    
    def get_statistics(self) -> dict:
        """Calcola statistiche generali."""
        if not self.students:
            return {}
        
        all_grades = []
        for student in self.students.values():
            all_grades.extend(student.grades)
        
        if not all_grades:
            return {'total_students': len(self.students)}
        
        return {
            'total_students': len(self.students),
            'average_grade': sum(all_grades) / len(all_grades),
            'highest_grade': max(all_grades),
            'lowest_grade': min(all_grades),
            'total_grades': len(all_grades)
        }
    
    def save(self) -> None:
        """Salva database su file JSON."""
        data = {
            'students': [s.to_dict() for s in self.students.values()]
        }
        with open(self.filepath, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load(self) -> None:
        """Carica database da file JSON."""
        if not self.filepath.exists():
            return
        
        try:
            with open(self.filepath, 'r') as f:
                data = json.load(f)
            
            for student_data in data.get('students', []):
                student = Student.from_dict(student_data)
                self.students[student.student_id] = student
        except json.JSONDecodeError:
            print("⚠️ Errore lettura database, creato nuovo database")

# === CLI INTERFACE ===
def print_menu():
    """Stampa menu principale."""
    print("\n" + "="*50)
    print("SISTEMA GESTIONE STUDENTI")
    print("="*50)
    print("1. Aggiungi studente")
    print("2. Lista studenti")
    print("3. Cerca studente")
    print("4. Aggiungi voto")
    print("5. Statistiche")
    print("6. Rimuovi studente")
    print("0. Esci")
    print("="*50)

def add_student(db: StudentDatabase) -> None:
    """Aggiunge nuovo studente."""
    print("\n--- Aggiungi Studente ---")
    student_id = input("ID Studente: ").strip()
    name = input("Nome: ").strip()
    
    try:
        age = int(input("Età: "))
        if age < 0:
            print("❌ Età deve essere positiva")
            return
        
        student = Student(student_id, name, age)
        db.add_student(student)
        print(f"✅ Studente {name} aggiunto con successo!")
    except ValueError as e:
        print(f"❌ Errore: {e}")

def list_students(db: StudentDatabase) -> None:
    """Lista tutti gli studenti."""
    students = db.list_students()
    if not students:
        print("\n📭 Nessuno studente presente")
        return
    
    print(f"\n📚 Studenti ({len(students)}):")
    print("-" * 60)
    for student in sorted(students, key=lambda s: s.name):
        print(student)

def search_student(db: StudentDatabase) -> None:
    """Cerca studente per nome o ID."""
    query = input("\nCerca (nome o ID): ").strip()
    
    # Cerca per ID
    student = db.get_student(query)
    if student:
        print(f"\n✅ Trovato: {student}")
        return
    
    # Cerca per nome
    results = db.search_by_name(query)
    if results:
        print(f"\n✅ Trovati {len(results)} studenti:")
        for student in results:
            print(f"  - {student}")
    else:
        print("❌ Nessuno studente trovato")

def add_grade(db: StudentDatabase) -> None:
    """Aggiunge voto a studente."""
    student_id = input("\nID Studente: ").strip()
    student = db.get_student(student_id)
    
    if not student:
        print("❌ Studente non trovato")
        return
    
    try:
        grade = int(input("Voto (0-30): "))
        student.add_grade(grade)
        db.save()
        print(f"✅ Voto {grade} aggiunto. Nuova media: {student.average_grade():.2f}")
    except ValueError as e:
        print(f"❌ Errore: {e}")

def show_statistics(db: StudentDatabase) -> None:
    """Mostra statistiche generali."""
    stats = db.get_statistics()
    
    if not stats:
        print("\n📭 Nessun dato disponibile")
        return
    
    print("\n📊 STATISTICHE GENERALI")
    print("-" * 40)
    print(f"Studenti totali: {stats.get('total_students', 0)}")
    
    if 'average_grade' in stats:
        print(f"Media generale: {stats['average_grade']:.2f}")
        print(f"Voto più alto: {stats['highest_grade']}")
        print(f"Voto più basso: {stats['lowest_grade']}")
        print(f"Voti totali: {stats['total_grades']}")

def remove_student(db: StudentDatabase) -> None:
    """Rimuove studente."""
    student_id = input("\nID Studente da rimuovere: ").strip()
    
    confirm = input(f"⚠️ Confermi rimozione studente {student_id}? (s/n): ")
    if confirm.lower() != 's':
        print("❌ Operazione annullata")
        return
    
    if db.remove_student(student_id):
        print(f"✅ Studente {student_id} rimosso")
    else:
        print("❌ Studente non trovato")

def main():
    """Entry point principale."""
    db = StudentDatabase()
    
    while True:
        print_menu()
        choice = input("\nScelta: ").strip()
        
        if choice == '1':
            add_student(db)
        elif choice == '2':
            list_students(db)
        elif choice == '3':
            search_student(db)
        elif choice == '4':
            add_grade(db)
        elif choice == '5':
            show_statistics(db)
        elif choice == '6':
            remove_student(db)
        elif choice == '0':
            print("\n👋 Arrivederci!")
            break
        else:
            print("❌ Scelta non valida")

if __name__ == "__main__":
    main()
```

### 9.2 Progetto: Web Scraper

```python
"""
Web scraper per estrarre dati da siti web.
Esempio: scraping job postings.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from typing import List, Dict
import time

class JobScraper:
    """Scraper per annunci lavoro."""
    
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.jobs: List[Dict] = []
    
    def fetch_page(self, url: str) -> str:
        """Fetch HTML di una pagina."""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Errore fetch {url}: {e}")
            return ""
    
    def parse_job_listing(self, html: str) -> List[Dict]:
        """Parse HTML per estrarre job listings."""
        soup = BeautifulSoup(html, 'html.parser')
        jobs = []
        
        # Esempio: cerca job cards (adatta al sito target!)
        job_cards = soup.find_all('div', class_='job-card')
        
        for card in job_cards:
            try:
                job = {
                    'title': card.find('h3').text.strip(),
                    'company': card.find('span', class_='company').text.strip(),
                    'location': card.find('span', class_='location').text.strip(),
                    'salary': card.find('span', class_='salary').text.strip() if card.find('span', class_='salary') else 'N/A',
                    'link': card.find('a')['href']
                }
                jobs.append(job)
            except AttributeError:
                continue
        
        return jobs
    
    def scrape(self, num_pages: int = 5) -> None:
        """Scrape multiple pages."""
        for page in range(1, num_pages + 1):
            url = f"{self.base_url}?page={page}"
            print(f"Scraping pagina {page}...")
            
            html = self.fetch_page(url)
            if not html:
                continue
            
            page_jobs = self.parse_job_listing(html)
            self.jobs.extend(page_jobs)
            
            print(f"  Trovati {len(page_jobs)} annunci")
            
            # Rispetta rate limiting
            time.sleep(2)
        
        print(f"\n✅ Totale annunci: {len(self.jobs)}")
    
    def save_to_csv(self, filename: str = 'jobs.csv') -> None:
        """Salva risultati in CSV."""
        if not self.jobs:
            print("Nessun dato da salvare")
            return
        
        df = pd.DataFrame(self.jobs)
        df.to_csv(filename, index=False)
        print(f"✅ Dati salvati in {filename}")
    
    def get_statistics(self) -> Dict:
        """Calcola statistiche."""
        if not self.jobs:
            return {}
        
        df = pd.DataFrame(self.jobs)
        return {
            'total_jobs': len(df),
            'unique_companies': df['company'].nunique(),
            'top_locations': df['location'].value_counts().head(5).to_dict(),
            'top_companies': df['company'].value_counts().head(5).to_dict()
        }

def main():
    # Esempio uso (adatta URL al sito reale!)
    scraper = JobScraper("https://example-jobs.com/search")
    scraper.scrape(num_pages=3)
    scraper.save_to_csv('jobs.csv')
    
    stats = scraper.get_statistics()
    print("\n📊 STATISTICHE:")
    print(f"Annunci totali: {stats['total_jobs']}")
    print(f"Aziende uniche: {stats['unique_companies']}")
    print("\nTop 5 Locations:")
    for loc, count in stats['top_locations'].items():
        print(f"  {loc}: {count}")

if __name__ == "__main__":
    main()
```

---

## 10. Testing e Debugging

### 10.1 Unit Testing con pytest

```python
# File: calculator.py
def add(a, b):
    """Somma due numeri."""
    return a + b

def divide(a, b):
    """Divide a per b."""
    if b == 0:
        raise ValueError("Divisione per zero")
    return a / b

def factorial(n):
    """Calcola fattoriale."""
    if n < 0:
        raise ValueError("n deve essere >= 0")
    if n == 0:
        return 1
    return n * factorial(n - 1)

# File: test_calculator.py
import pytest
from calculator import add, divide, factorial

# Test base
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    
    # Test eccezione
    with pytest.raises(ValueError):
        divide(10, 0)

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    
    with pytest.raises(ValueError):
        factorial(-1)

# Parametrized test
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (10, -5, 5)
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected

# Fixture
@pytest.fixture
def sample_numbers():
    return [1, 2, 3, 4, 5]

def test_with_fixture(sample_numbers):
    assert sum(sample_numbers) == 15

# Esegui test:
# pytest test_calculator.py -v
```

### 10.2 Debugging Tecniche

```python
# PRINT DEBUGGING (base)
def buggy_function(x):
    print(f"DEBUG: x = {x}")  # Debug print
    result = x * 2
    print(f"DEBUG: result = {result}")
    return result

# ASSERT per assumption checking
def process_list(items):
    assert isinstance(items, list), "items deve essere lista"
    assert len(items) > 0, "lista non può essere vuota"
    # ... resto codice

# LOGGING (professionale)
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def process_data(data):
    logger.debug(f"Processing data: {data}")
    try:
        result = complex_operation(data)
        logger.info(f"Success: {result}")
        return result
    except Exception as e:
        logger.error(f"Error processing data: {e}", exc_info=True)
        raise

# DEBUGGER (pdb)
import pdb

def buggy_function(x, y):
    pdb.set_trace()  # Breakpoint
    result = x / y
    return result

# Comandi pdb:
# n - next line
# s - step into
# c - continue
# p variable - print variable
# q - quit

# TRACEBACK analysis
import traceback

try:
    result = risky_operation()
except Exception as e:
    print("Errore catturato!")
    traceback.print_exc()  # Stack trace completo
```

---

## 11. Errori Comuni con IA in Python

### 11.1 Errore: Import Librerie Inesistenti

```python
# ❌ IA potrebbe suggerire:
import numpy_advanced  # Non esiste!

# ✅ VERIFICA sempre:
# pip search numpy
# oppure cerca su PyPI: https://pypi.org
```

### 11.2 Errore: Codice Python 2

```python
# ❌ IA potrebbe generare sintassi Python 2:
print "Hello"  # Python 2 syntax!
x = raw_input()  # Python 2

# ✅ Python 3:
print("Hello")
x = input()
```

### 11.3 Errore: Type Hints Errati

```python
# ❌ IA vecchia potrebbe usare:
from typing import List, Dict  # Vecchio stile

def func(items: List[int]) -> Dict[str, int]:
    pass

# ✅ Python 3.10+ (moderno):
def func(items: list[int]) -> dict[str, int]:
    pass
```

### 11.4 Errore: Mutabilità Default Arguments

```python
# ❌ IA potrebbe generare (BUG COMUNE!):
def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list

# Problema: lista default è CONDIVISA tra chiamate!
print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] - ⚠️ Contiene anche 1!

# ✅ CORRETTO:
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list
```

### 11.5 Errore: Exception Handling Troppo Generico

```python
# ❌ IA potrebbe generare:
try:
    result = risky_operation()
except:  # Cattura TUTTO, anche KeyboardInterrupt!
    pass

# ✅ CORRETTO:
try:
    result = risky_operation()
except ValueError as e:
    print(f"Errore valore: {e}")
except FileNotFoundError as e:
    print(f"File non trovato: {e}")
except Exception as e:
    print(f"Errore generico: {e}")
    raise  # Re-raise per debugging
```

---

## 12. Best Practices Python

### 12.1 PEP 8 Style Guide

```python
# NAMING CONVENTIONS

# Variabili e funzioni: snake_case
user_name = "Mario"
def calculate_average():
    pass

# Classi: PascalCase
class StudentDatabase:
    pass

# Costanti: UPPER_CASE
MAX_STUDENTS = 100
API_KEY = "secret"

# INDENTAZIONE: 4 spazi (NON tab!)

# LINEE VUOTE
class MyClass:
    
    def method1(self):
        pass
    
    def method2(self):  # 1 riga vuota tra metodi
        pass

# 2 righe vuote tra classi/funzioni top-level

# LUNGHEZZA RIGA: max 79 caratteri

# IMPORTS: sempre in cima, ordine:
# 1. Standard library
# 2. Third-party
# 3. Local
import os
import sys

import numpy as np
import pandas as pd

from mymodule import myfunction

# SPAZI
# ✅ Corretto
x = 1
y = 2
result = function(x, y)

# ❌ Sbagliato
x=1
y = 2
result = function( x,y )

# STRINGHE: preferisci singoli apici
name = 'Mario'
# tranne per testo con apici
text = "It's a beautiful day"
```

### 12.2 Pythonic Code

```python
# LIST COMPREHENSIONS
# ❌ Non pythonic
squares = []
for x in range(10):
    squares.append(x**2)

# ✅ Pythonic
squares = [x**2 for x in range(10)]

# ENUMERATE
# ❌ Non pythonic
for i in range(len(items)):
    print(i, items[i])

# ✅ Pythonic
for i, item in enumerate(items):
    print(i, item)

# WITH STATEMENTS
# ❌ Non pythonic
f = open('file.txt')
data = f.read()
f.close()

# ✅ Pythonic
with open('file.txt') as f:
    data = f.read()

# MULTIPLE ASSIGNMENT
# ❌ Non pythonic
x = 1
y = 2
x = 2
y = 1

# ✅ Pythonic
x, y = 1, 2
x, y = y, x  # Swap

# STRING CONCATENATION
# ❌ Non pythonic
result = "Hello" + " " + name + "!"

# ✅ Pythonic
result = f"Hello {name}!"

# CHECK EMPTY
# ❌ Non pythonic
if len(my_list) == 0:
    pass

# ✅ Pythonic
if not my_list:
    pass

# DEFAULT VALUES
# ❌ Non pythonic
if value is None:
    value = default

# ✅ Pythonic
value = value or default
# oppure (più sicuro):
value = default if value is None else value
```

### 12.3 Checklist Qualità Codice

```
✅ LEGGIBILITÀ
[ ] Nomi variabili descrittivi
[ ] Funzioni brevi (<50 righe)
[ ] Commenti per logica complessa
[ ] Docstring per funzioni/classi pubbliche
[ ] PEP 8 compliant

✅ ROBUSTEZZA
[ ] Gestione errori appropriata
[ ] Validazione input
[ ] Test unitari presenti
[ ] Edge cases considerati

✅ MANUTENIBILITÀ
[ ] Funzioni singola responsabilità
[ ] No codice duplicato
[ ] Configurazione separata da logica
[ ] Logging appropriato

✅ PERFORMANCE
[ ] Algoritmi efficienti (Big O ragionevole)
[ ] No operazioni ripetute inutili
[ ] Uso strutture dati appropriate
[ ] Profile se critico

✅ SICUREZZA
[ ] No password/secrets in codice
[ ] Input sanitization
[ ] Dependencies sicure e aggiornate
[ ] Error messages non rivelano info sensibili
```

---

## ✅ Checklist Completamento Modulo

- [ ] Conosco sintassi base Python
- [ ] So usare strutture dati (list, dict, set, tuple)
- [ ] Scrivo funzioni con type hints
- [ ] Applico concetti OOP (classi, ereditarietà)
- [ ] Gestisco file e I/O correttamente
- [ ] Uso IA efficacemente per generare codice Python
- [ ] Riconosco errori comuni nell'output IA
- [ ] Scrivo test con pytest
- [ ] Applico PEP 8 e best practices
- [ ] Ho completato almeno 1 progetto completo
- [ ] Mi sento pronto per sviluppo autonomo Python

---

## 📚 Risorse per Approfondimento

**Documentazione:**
- Python.org: https://docs.python.org/3/
- PEP 8: https://pep8.org
- Real Python: https://realpython.com

**Libri:**
- "Python Crash Course" - Eric Matthes
- "Fluent Python" - Luciano Ramalho
- "Effective Python" - Brett Slatkin

**Pratica:**
- LeetCode: https://leetcode.com (problemi algoritmici)
- HackerRank: https://hackerrank.com
- Project Euler: https://projecteuler.net

**Community:**
- r/learnpython
- Stack Overflow
- Python Discord

---

**Fine Modulo 4 Alternativo - Python**

*Prossimo passo: Applicare Python a progetti reali ITS!*

---

**Versione documento:** 1.0  
**Ultimo aggiornamento:** Dicembre 2024  
**Corso ITS:** IA e Programmazione Assistita  
**Modulo:** 4 Alternativo - Python con IA

