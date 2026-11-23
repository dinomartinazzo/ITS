# Revisione del 4 ottobre 2026

- Configurazione A: corretta la polarità; resistenza differenziale 0–199,6 Ω distinta dall'impedenza verso massa. C1 da 100 nF opzionale, polo minimo circa 8 kHz.
- Configurazione B: C1 mantenuto per prove statiche, polo circa 64 Hz; spiegati assestamento ed errore di carico. Calcoli con eccitazione ideale, senza carico ADC né filtri del modulo.
- Aggiornate etichette SVG, procedura con/senza C1 e diagnostica. I condensatori di disaccoppiamento e CAP restano previsti.
- ADS131M04: chiariti limiti del rapporto software, filtraggio antialias, carico della sorgente e del partitore. Il filtro per segnali dinamici richiede un dimensionamento dedicato.
- Prova di simultaneità: gradino controllato con ingressi sempre collegati; chiarito che lo streaming seriale periodico non valida l'allineamento temporale.
- Firmware ADS131M04: configurazione non valida blocca la misura; saturazione, CRC errato, bassa eccitazione e timeout invalidano dati e filtri e annullano tara/statistiche in corso. Gli offset già salvati sono preservati. Cambio configurazione annulla la raccolta. Una tara completata svuota il filtro precedente.
- Aggiornato il sorgente incorporato nell'HTML e rigenerato firmware_dispensa.zip.

## Verifiche

Prove native C++ con stub superate (vedere tests/README.md). Tutti i 31 sorgenti nell'HTML confrontati con i file; identificativi HTML univoci e link interni verificati. Contenuti dello ZIP firmware confrontati con i sorgenti.

Compilazione ESP32 e prove hardware non eseguite. Le dichiarazioni storiche di compilazione presenti nella dispensa sono attribuite alla versione originale. L'efficacia reale di C1 va verificata con le misure descritte nel capitolo 11.

Lo ZIP originale sul Desktop è conservato; il pacchetto aggiornato è Simulare una cella di carico - revisionato.zip.
