# AstroBlog

## Descrizione

AstroBlog è un sito web statico dedicato alla divulgazione astronomica. Il progetto propone una homepage informativa sul sistema solare e sull'universo, oltre a una pagina di approfondimento dedicata al pianeta Marte, con l'obiettivo di offrire contenuti chiari e visivamente curati agli appassionati di astronomia.

## Screenshot

> Lo screenshot del progetto verrà aggiunto dopo la pubblicazione su GitHub Pages.

## Funzionalità principali

- **Homepage** con sezione hero, presentazione del progetto e delle fonti di riferimento (NASA, ESA, ASI, INAF).
- **Carousel di immagini** (Bootstrap) sia in homepage sia nella pagina dedicata a Marte, con didascalie descrittive.
- **Sezione "Ultime News"** e **"Articoli in Evidenza"** con card informative e immagini.
- **Sezione community** con elenco delle iniziative proposte (serate osservative, webinar, forum, concorsi fotografici).
- **Pagina dedicata a Marte** (`marte.html`) con box "Dati principali" (diametro, massa) e galleria di immagini della superficie del pianeta.
- **Navbar con menu a tendina** per le categorie Sistema Solare, Galassia e Universo.
- **Design responsive**, basato sul sistema a griglia di Bootstrap e su media query personalizzate in `style.css`.

## Tecnologie utilizzate

- **HTML5** per la struttura semantica delle pagine.
- **CSS3** per lo stile personalizzato (variabili CSS, gradienti, animazioni, media query).
- **Bootstrap 5.3.2** (CSS e JS bundle via CDN) per componenti UI come navbar, carousel e card.
- **Git / GitHub** per il versionamento del codice.

## Struttura del progetto

```
blog-astronomia/
├── index.html      # Homepage del sito
├── marte.html       # Pagina di approfondimento dedicata a Marte
├── style.css         # Fogli di stile personalizzati
└── img/              # Immagini utilizzate nel sito (loghi, foto, illustrazioni)
```

## Come eseguire il progetto in locale

Il progetto è un sito statico e non richiede alcuna installazione o build.

1. Clona il repository:
   ```bash
   git clone https://github.com/andrea-bartiromo/blog-astronomia.git
   ```
2. Entra nella cartella del progetto:
   ```bash
   cd blog-astronomia
   ```
3. Apri `index.html` direttamente nel browser, oppure avvia un server locale (ad esempio con l'estensione "Live Server" di VS Code) per una navigazione ottimale tra le pagine.

## Competenze dimostrate

- Realizzazione di pagine HTML semantiche e ben strutturate.
- Scrittura di CSS personalizzato con variabili, gradienti e animazioni.
- Utilizzo di un framework CSS (Bootstrap) per la realizzazione di componenti UI responsive.
- Organizzazione ordinata dei file di un progetto front-end statico.
- Gestione del codice tramite Git e GitHub, con workflow basato su commit incrementali.

## Possibili sviluppi futuri

- Completamento delle pagine dedicate agli altri corpi celesti già presenti nel menu di navigazione (attualmente collegati con link segnaposto).
- Sostituzione delle immagini segnaposto residue (`/api/placeholder/...`) con asset definitivi.
- Miglioramento dell'accessibilità e della SEO delle pagine.
- Eventuale introduzione di contenuti dinamici o di un backend per la gestione degli articoli.

## Autore

**Andrea Bartiromo**
GitHub: [@andrea-bartiromo](https://github.com/andrea-bartiromo)
