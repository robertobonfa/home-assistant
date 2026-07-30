# Changelog

Tutte le modifiche rilevanti a questo tema sono documentate in questo file.

Il formato segue [Keep a Changelog](https://keepachangelog.com/it/1.1.0/)
e il progetto aderisce al [Semantic Versioning](https://semver.org/lang/it/).

## [1.0.4] - 2026-07-28

### Fixed

- Il crinale dello sfondo usava `#3b4252`, **lo stesso valore di
  `ha-card-background`**: nella fascia bassa della dashboard le card si
  confondevano con lo sfondo. Difetto identico a quello gia corretto su Salvia,
  ma mai riportato su Nordic. Crinali ricalcolati con la formula ora comune a
  tutta la raccolta — `mix(P1, P0, 0.35 / 0.55 / 0.20)` — passando a `#363d4c`,
  `#343a48` e `#383f4e`.
- PNG dello sfondo rigenerati di conseguenza. **Vanno ricopiati sull'istanza**:
  il file gia installato contiene ancora la versione difettosa.

## [1.0.3] - 2026-07-26

### Added

- `Instructions.md`: avviso al passo 0 sul fatto che una connessione SFTP
  all'add-on SSH atterra in `/root/`, home di un container separato che Home
  Assistant non legge e che viene azzerato a ogni aggiornamento dell'add-on.
  Chiarito che `config/`, `homeassistant/`, `addons/`, `media/`, `share/` e
  `ssl/` visibili lì sono collegamenti simbolici, e che bisogna entrare in
  `homeassistant/` prima di creare `themes` e `www`.

### Fixed

- `Instructions.md`: il troubleshooting del selettore temi non copriva il caso
  "Nessun tema disponibile" con selettore grigio, ed elencava le verifiche in
  un ordine che metteva per ultima la causa più frequente. Ora la prima verifica
  è la posizione della cartella `themes/` rispetto alla cartella di
  configurazione.

## [1.0.2] - 2026-07-26

### Added

- `Instructions.md`: riga SFTP nella tabella dei percorsi, come modo di accesso
  alla cartella di configurazione accanto a File editor, Samba e SSH.
- `Instructions.md`: avviso esplicito che la sottocartella `www/nordic/` non è
  facoltativa, perché il tema punta a `/local/nordic/…`; indicata l'alternativa
  di togliere `nordic/` dalla riga `lovelace-background`.

### Changed

- `Instructions.md`: nei blocchi dei percorsi il percorso HAOS è ora elencato
  per primo, con etichetta `HAOS ▸`, invece di comparire dopo una freccia in
  coda al percorso generico. L'ordine precedente rendeva difficile individuare
  il percorso corretto su HAOS, che è il caso d'uso più comune.

## [1.0.1] - 2026-07-26

### Added

- `Instructions.md`: sezione "Dove si trova la cartella di configurazione", con
  tabella di corrispondenza fra `/config/` della documentazione ufficiale e il
  percorso effettivamente visibile in File editor (`homeassistant/`), Studio
  Code Server, SSH, Samba share e installazioni Container/Core.
- `Instructions.md`: avviso che l'add-on File editor non gestisce file binari e
  corrompe i PNG dello sfondo; indicati Samba share e Studio Code Server come
  alternative.
- `Instructions.md`: passo 1-bis con variante `lovelace-background` a solo
  gradiente CSS, per installare il tema senza copiare alcuna immagine.
- `Instructions.md`: procedura per creare la cartella `themes` da File editor,
  che non ha un comando "nuova cartella" (si crea indicando il percorso
  completo come nome del nuovo file).
- `Instructions.md`: nota sulla chiave `frontend:` duplicata in
  `configuration.yaml`, sul comando "Ricarica temi" e su cosa controllare se il
  tema non compare nel selettore.

### Changed

- `Instructions.md`: i percorsi assoluti `/config/…` sono stati resi relativi e
  affiancati dall'equivalente HAOS, per non far cercare all'utente una cartella
  `config` che su HAOS non esiste.
- `Instructions.md`: ampliato il troubleshooting dello sfondo con i casi 404,
  cartella `www` appena creata e PNG corrotti da File editor.

## [1.0.0] - 2026-07-26

### Added

- Tema `nordic.yaml` per Home Assistant, 185 variabili, interamente dichiarato
  sotto `modes: dark:`.
- Mappatura completa della rampa Nordic a 8 stop (`#2e3440` → `#eceff4`) presa
  dalla palette omonima di `wallpapers.robertobonfa.com` (`js/app.js:129`).
- Accenti semantici dalla palette Nord Aurora: `#bf616a` errore, `#ebcb8b`
  avviso, `#a3be8c` successo, `#b48ead` per il dominio `light` attivo.
- Colori di stato per tutti i domini supportati da Home Assistant
  (`state-{domain}-{state}-color`), inclusi i `device_class` di `binary_sensor`
  e i sotto-stati di `alarm_control_panel`, `climate`, `lock` e `update`.
- Copertura di card, sidebar, header, switch, slider, input MDC, dialog,
  tabelle, code editor, badge e colori dei grafici energia.
- Sfondo minimale: sorgente `backgrounds/nordic-bg.svg` più PNG
  2560×1440 (desktop e tablet) e 1170×2532 (smartphone).
- `backgrounds/generate-backgrounds.py` per rigenerare i PNG a qualsiasi
  risoluzione mantenendo la stessa composizione dell'SVG.
- `preview-palette.svg`: anteprima della palette per la condivisione.
- `Instructions.md` con installazione, personalizzazione, troubleshooting e
  note tecniche in italiano e inglese.
