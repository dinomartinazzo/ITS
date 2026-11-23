"""Configurazione della produzione del PDF: percorsi, metadati, parametri di Chrome."""
import os
import shutil

AQUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(AQUI)

HTML_IN = os.path.join(RADICE, "dispensa_simulatore_ponte_348.html")
PDF_OUT = os.path.join(RADICE, "dispensa_simulatore_ponte_348.pdf")
CSS_STAMPA = os.path.join(AQUI, "stampa.css")
CHROME = shutil.which("google-chrome") or "/usr/bin/google-chrome"

TITOLO = "Simulatore di cella di carico a ponte da 348 Ω"
AUTORE = "Dino Martinazzo"
OGGETTO = ("Dispensa di laboratorio per ITS: ponte resistivo che simula una cella di carico da 350 Ω, "
           "calcoli, costruzione, taratura e collaudo con modulo HX711")
PAROLE_CHIAVE = "cella di carico, ponte di Wheatstone, HX711, simulatore, sense a sei fili, misure elettroniche"

# La copertina è la pagina fisica 1: i numeri dell'indice e quelli stampati a piè di pagina la contano.
PAGINE_COPERTINA = 1

TIMEOUT_CHROME = 300
