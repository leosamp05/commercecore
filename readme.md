# CommerceCore

CommerceCore è un'applicazione Python da terminale per la gestione di prodotti, inventario e ordini di un piccolo e-commerce.

Il progetto è stato realizzato per mettere in pratica OOP, gestione dei dati e organizzazione di un'applicazione Python su più livelli.

## Funzionalità

* Creazione, modifica ed eliminazione dei prodotti
* Validazione dei dati e controllo degli SKU
* Persistenza dei dati tramite JSON
* Creazione e consultazione degli ordini
* Ricerca degli ordini tramite ID
* Aggiornamento dello stock
* Annullamento degli ordini
* Interfaccia CLI

## Struttura

```text
commercecore/
├── cli/            # Interazione con l'utente
├── models/         # Entità del dominio
├── services/       # Logica applicativa
├── repositories/   # Lettura e salvataggio dei dati
├── data/           # File JSON
└── main.py
```

## Tecnologie

* Python 3
* JSON
* Git

## Avvio

```bash
git clone https://github.com/leosamp05/commercecore.git
cd commercecore
python main.py
```

## Autore

**Leonardo Sampaoli**
