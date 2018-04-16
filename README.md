# DOCUMENTAZIONE FANTAMARCONI
---

### FUNZIONALITÀ
- **Organigramma**: rappresenta l'organizzazione della scuola con uno schema
- **Macroprocessi**: rappresentano tutti i processi all'interno della scuola e il referente responsabile
- **Timeline**: è possibile visualizzare graficamente la durata di tutti i sottoprocessi (ogni sottoprocesso fa riferimento ad un macroprocesso)
- Esempio:
	- Macroprocesso: Orientamento
	- Sottoprocessi: organizzazione, tutti i vari incontri

### Models.py
- **Organogram**:
*Serve per rappresentare l'organigramma della scuola. Ogni record è un elemento dell'organigramma*
	- Il campo ``parent_level`` indica il livello superiore a cui fa riferimento il record nello schema dell'organigramma. Lasciare vuoto se non fa riferimento a nessuno (es. preside)
- **Processes**:
*Ogni record rappresenta un macroprocesso ed il suo referente (che è un utente registrato).*
- **Timeline**:
*Contiene tutti i sottoprocessi, ognuno dei quali fa riferimento ad un macroprocesso.*
	- Il campo ``job`` indica il compito del sottoprocesso, e in caso anche i partecipanti.
	- Le date di inizio e di fine sono necessarie per visualizzare poi correttamente il grafico nella timeline.

---
	Tonin Davide
	Emanuele Feola
	5CI 2017-2018