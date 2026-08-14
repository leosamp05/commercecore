# CommerceCore

Un'applicazione Python modulare che simula la logica principale di gestione dell'inventario e degli ordini di un piccolo e-commerce.

Il progetto è sviluppato come applicazione da terminale e si concentra sulla separazione chiara tra modelli di dominio, logica applicativa, persistenza e interazione con l'utente.

> **Stato:** Work in progress

---

## Funzionalità attuali

* Creazione e validazione dei prodotti
* Controllo dell'unicità degli SKU
* Gestione dell'inventario in memoria
* Visualizzazione dei prodotti tramite CLI
* Gestione degli input e degli errori
* Struttura del progetto modulare

---

## Funzionalità previste

* Modifica ed eliminazione dei prodotti
* Persistenza tramite JSON
* Creazione e annullamento degli ordini
* Validazione automatica dello stock
* Aggiornamento automatico delle quantità
* Storico dei movimenti di magazzino
* Importazione del catalogo tramite CSV
* Report su inventario e vendite
* Eccezioni personalizzate

---

## Architettura

CommerceCore separa le responsabilità in diversi livelli:

```text
commercecore/
│
├── models/
│   ├── product.py
│   ├── order.py
│   ├── order_item.py
│   └── stock_movement.py
│
├── services/
│   ├── inventory_service.py
│   ├── order_service.py
│   ├── report_service.py
│   └── import_service.py
│
├── repositories/
│   ├── product_repository.py
│   ├── order_repository.py
│   └── stock_movement_repository.py
│
├── exceptions/
│   └── domain_errors.py
│
├── data/
│   ├── products.json
│   ├── orders.json
│   └── stock_movements.json
│
├── cli/
│   ├── main_menu.py
│   ├── product_menu.py
│   ├── order_menu.py
│   └── report_menu.py
│
└── main.py
```

### Responsabilità

* **Models** — rappresentano le principali entità del dominio
* **Services** — contengono la logica applicativa
* **Repositories** — gestiscono la persistenza dei dati
* **CLI** — gestisce input e output dell'utente
* **Exceptions** — contiene gli errori specifici dell'applicazione
* **Data** — contiene i dati persistenti del programma

---

## Modello Product

Ogni prodotto contiene:

* SKU
* Nome
* Categoria
* Prezzo
* Quantità disponibile

Il modello valida il proprio stato e impedisce valori non validi, come identificativi vuoti, prezzi negativi o quantità di stock non ammesse.

---

## Esempio CLI

```text
========COMMERCECORE========
1. Prodotti
2. Ordini
0. Esci
Scelta: 1

========PRODOTTI========
1. Visualizza Prodotti
2. Aggiungi un Prodotto
0. Indietro
```

Esempio di visualizzazione dei prodotti:

```text
---------------------------------------------------------------------------
SKU                   NOME                          PREZZO       STOCK
---------------------------------------------------------------------------
DIOR-SAUVAGE-100      Dior Sauvage EDT 100ml       €105.00      7
CHANEL-BLEU-100       Bleu de Chanel 100ml          €120.00      3
---------------------------------------------------------------------------
```

---

## Regole di business

La versione finale dovrà applicare regole come:

* Ogni prodotto deve avere uno SKU univoco
* Il prezzo deve essere maggiore di zero
* Lo stock non può essere negativo
* Un ordine può essere confermato solo se tutti gli articoli sono disponibili
* Un ordine non valido non deve modificare parzialmente l'inventario
* L'annullamento di un ordine deve ripristinare lo stock
* Un ordine non può essere annullato due volte
* Gli ordini devono conservare il prezzo originale dei prodotti al momento dell'acquisto

---

## Tecnologie

* Python 3
* Python Standard Library
* JSON
* CSV
* Git

La prima versione non richiede framework web né database esterni.

---

## Avvio del progetto

Clona il repository:

```bash
git clone <repository-url>
cd commercecore
```

Avvia l'applicazione:

```bash
python main.py
```

---

## Roadmap di sviluppo

### Fase 1 — Prodotti

* Modello `Product`
* Inventory service
* CLI prodotti
* Validazione

### Fase 2 — Persistenza

* Repository JSON
* Persistenza dei prodotti

### Fase 3 — Ordini

* Ordini e righe d'ordine
* Validazione dello stock
* Annullamento degli ordini

### Fase 4 — Storico inventario

* Movimenti di magazzino
* Storico dei rifornimenti
* Movimenti generati dagli ordini

### Fase 5 — Dati e report

* Importazione catalogo CSV
* Prodotti con stock basso
* Prodotti esauriti
* Valore dell'inventario
* Statistiche sulle vendite

### Fase 6 — Rifinitura

* Refactoring
* Type hints
* Revisione della gestione degli errori
* Dati di esempio
* Documentazione

---

## Obiettivi del progetto

CommerceCore è pensato per modellare regole applicative reali mantenendo l'implementazione focalizzata sui fondamenti di Python e sulla struttura del software.

Il progetto mette in pratica:

**Python · OOP · Strutture dati · Gestione degli errori · File I/O · JSON · CSV · Software Design · Git**

---

## Autore

**Leonardo Sampaoli**

GitHub: [leosamp05](https://github.com/leosamp05)
