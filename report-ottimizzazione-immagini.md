# Report ottimizzazione immagini AstroBlog

Branch: `agent/ottimizzazione-immagini`
Base: `main`

## Obiettivo

Ridurre la dipendenza da immagini esterne NASA/JPL/ESA, scaricando quando possibile asset ufficiali, convertendoli in WebP e servendoli dalla cartella `img` con percorsi relativi locali.

## Esito operativo

L'ambiente di lavoro non ha consentito il download automatico degli asset ufficiali esterni: tutti i tentativi di download diretti con `curl -L --fail --max-time 40` e user-agent esplicito hanno restituito `403 Forbidden`.

Per evitare asset non verificati, immagini ricostruite o sostituzioni arbitrarie, non sono stati generati WebP locali per questi URL. Le pagine HTML non sono state modificate: gli URL esterni esistenti restano temporaneamente invariati, ma sono censiti qui per sostituzione manuale o download da ambiente autorizzato.

## File HTML analizzati

- `index.html`
- `sistema-solare.html`
- `sole.html`
- `mercurio.html`
- `venere.html`
- `terra.html`
- `luna.html`
- `marte.html`
- `giove.html`
- `saturno.html`
- `urano.html`
- `nettuno.html`
- `asteroidi.html`
- `comete.html`
- `fascia-kuiper.html`
- `via-lattea.html`
- `nebulose.html`
- `osservare-il-cielo.html`
- `chi-siamo.html`

## Immagini locali gia' presenti e confermate

Asset individuati tramite riferimenti HTML e verificati nella cartella `img`:

- `img/cielo-notturno.webp`
- `img/giove.webp`
- `img/luna-crateri.webp`
- `img/nebulosa-orione.webp`
- `img/olympus-mons.jpg`
- `img/pianeta-marte.webp`
- `img/pilastri-creazione.webp`
- `img/polo-nord-marte.webp`
- `img/saturno.webp`
- `img/via-lattea-4.webp`
- `img/via-lattea-struttura.webp`

## Immagini esterne non scaricate

| Pagina | Uso | URL ufficiale | File locale previsto | Motivo blocco |
| --- | --- | --- | --- | --- |
| `sole.html` | hero / OG / Twitter | `https://svs.gsfc.nasa.gov/vis/a010000/a013600/a013664/Solar_Orbiter_EUI-fullsun01_print.jpg` | `img/sole-hero.webp` | Download automatico bloccato da `403 Forbidden` |
| `sole.html` | immagine interna corona | `https://svs.gsfc.nasa.gov/vis/a010000/a013600/a013664/Solar_Orbiter_EUI-still01.jpg` | `img/sole-corona.webp` | Download automatico bloccato da `403 Forbidden` |
| `urano.html` | hero / OG / Twitter | `https://assets.science.nasa.gov/content/dam/science/psd/photojournal/pia/pia18/pia18182/PIA18182.jpg` | `img/urano-voyager.webp` | Download automatico bloccato da `403 Forbidden` |
| `urano.html` | immagine interna JWST | `https://science.nasa.gov/wp-content/uploads/2024/05/webb-stsci-01hhfq0y3096sav5rzdhxnrsb5-2k.png?w=1024` | `img/urano-webb.webp` | Download automatico bloccato da `403 Forbidden` |
| `nettuno.html` | hero / OG / Twitter | `https://assets.science.nasa.gov/content/dam/science/psd/photojournal/pia/pia01/pia01492/PIA01492.jpg` | `img/nettuno-voyager.webp` | Download automatico bloccato da `403 Forbidden` |
| `nettuno.html` | immagine interna Tritone | `https://assets.science.nasa.gov/dynamicimage/assets/science/psd/solar/internal_resources/438/PIA00317-1.jpg?crop=faces%2Cfocalpoint&fit=clip&h=768&w=990` | `img/tritone-voyager.webp` | Download automatico bloccato da `403 Forbidden` |
| `asteroidi.html` | hero / OG / Twitter | `https://d2pn8kiwq2w21t.cloudfront.net/original_images/jpegPIA12469.jpg` | `img/asteroidi-fascia.webp` | Download automatico bloccato da `403 Forbidden` |
| `asteroidi.html` | immagine interna Bennu | `https://svs.gsfc.nasa.gov/vis/a000000/a004800/a004857/bennu_spin_v3_02.1000_print.jpg` | `img/bennu.webp` | Download automatico bloccato da `403 Forbidden` |
| `comete.html` | hero / OG / Twitter | `https://svs.gsfc.nasa.gov/vis/a010000/a013600/a013661/20200705T020949BW_print.jpg` | `img/neowise-code.webp` | Download automatico bloccato da `403 Forbidden` |
| `comete.html` | immagine interna 67P | `https://svs.gsfc.nasa.gov/vis/a030000/a030700/a030765/MainImage.jpg` | `img/cometa-67p.webp` | Download automatico bloccato da `403 Forbidden` |
| `fascia-kuiper.html` | hero / OG / Twitter | `https://images-assets.nasa.gov/image/PIA22190/PIA22190~orig.jpg` | `img/kuiper-new-horizons.webp` | Download automatico bloccato da `403 Forbidden` |
| `fascia-kuiper.html` | immagine interna Arrokoth | `https://assets.science.nasa.gov/content/dam/science/psd/solar/2023/09/m/mu69_full_vert.png` | `img/arrokoth.webp` | Download automatico bloccato da `403 Forbidden` |
| `terra.html` | hero / OG | `https://eoimages.gsfc.nasa.gov/images/imagerecords/74000/74218/world.200412.3x5400x2700.jpg` | `img/terra-blue-marble.webp` | Download automatico bloccato da `403 Forbidden` |
| `terra.html` | immagine interna Earthrise | `https://eol.jsc.nasa.gov/DatabaseImages/ISD/lowres/AS08/AS08-14-2383.JPG` | `img/earthrise.webp` | Download automatico bloccato da `403 Forbidden` |
| `mercurio.html` | hero / OG | `https://assets.science.nasa.gov/content/dam/science/psd/photojournal/pia/pia15/pia15160/PIA15160.jpg` | `img/mercurio-messenger.webp` | Download automatico bloccato da `403 Forbidden` |
| `mercurio.html` | immagine interna Caloris | `https://assets.science.nasa.gov/content/dam/science/psd/photojournal/pia/pia02/pia02439/PIA02439.jpg` | `img/mercurio-caloris.webp` | Download automatico bloccato da `403 Forbidden` |
| `venere.html` | hero / OG | `https://d2pn8kiwq2w21t.cloudfront.net/original_images/jpegPIA00478.jpg` | `img/venere-magellan.webp` | Download automatico bloccato da `403 Forbidden` |
| `venere.html` | immagine interna Sedna Planitia | `https://d2pn8kiwq2w21t.cloudfront.net/original_images/jpegPIA00306.jpg` | `img/venere-sedna.webp` | Download automatico bloccato da `403 Forbidden` |

## Pagine gia' autosufficienti per immagini di contenuto

Queste pagine usano immagini locali per le immagini di contenuto principali analizzate:

- `index.html`
- `luna.html`
- `marte.html`
- `giove.html`
- `saturno.html`
- `sistema-solare.html`
- `via-lattea.html`
- `nebulose.html`
- `osservare-il-cielo.html`

Nota: alcune pagine usano comunque URL assoluti GitHub Pages nei meta Open Graph/Twitter per asset locali gia' presenti. Questi URL non sono hotlink NASA/JPL/ESA e non sono stati modificati in questa PR.

## Controlli editoriali sulle immagini

Durante l'analisi sono stati controllati:

- presenza di hero image nelle pagine richieste;
- presenza di immagini interne dove gia' previste;
- testi `alt` descrittivi;
- `decoding="async"` sulle immagini analizzate;
- `loading="lazy"` sulle immagini interne non prioritarie;
- didascalie con crediti NASA/ESA/JPL dove richiesti.

## Prossimo passo consigliato

Eseguire il download degli asset ufficiali da un ambiente di rete autorizzato o dal browser, convertire i file previsti in WebP e caricarli in `img`. A quel punto sara' possibile sostituire gli URL esterni con percorsi locali `./img/*.webp` senza cambiare il testo editoriale o i crediti gia' presenti.
