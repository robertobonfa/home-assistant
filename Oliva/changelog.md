# Changelog

Tutte le modifiche rilevanti a questo tema sono documentate in questo file.

Il formato segue [Keep a Changelog](https://keepachangelog.com/it/1.1.0/)
e il progetto aderisce al [Semantic Versioning](https://semver.org/lang/it/).

## [1.1.0] - 2026-07-30

### Changed

- Gli interruttori accesi usavano `#a4ad80`, lo stesso colore dello stato
  attivo generico: il cambio di stato era poco leggibile, perche quel colore
  appartiene alla rampa e si confonde con il resto dell'interfaccia.
  `state-switch-active-color` passa a `#f2d65e`.
- Stesso trattamento a `state-input_boolean-active-color` e
  `state-fan-active-color`: tutto cio che si comanda diventa caldo quando e
  acceso. Gli stati passivi (sensori, automazioni, presenza) restano sul
  colore della rampa, cosi il segnale resta tale e non diventa sfondo.

## [1.0.0] - 2026-07-26

### Added

- Tema `oliva.yaml` per Home Assistant, 185 variabili, interamente dichiarato
  sotto `modes: dark:`.
- Mappatura completa della rampa Oliva a 8 stop (`#20240f` → `#f1f2e1`) presa
  dalla palette omonima di `wallpapers.robertobonfa.com` (`js/app.js:150`).
- Accenti semantici: `#cf5b4e` errore, `#e8a33d` avviso, `#7ec46a` successo,
  `#f2d65e` per il dominio `light` attivo.
- Colori di stato per tutti i domini supportati da Home Assistant
  (`state-{domain}-{state}-color`), inclusi i `device_class` di
  `binary_sensor` e i sotto-stati di `alarm_control_panel`, `climate`, `lock`
  e `update`.
- Copertura di card, sidebar, header, switch, slider, input MDC, dialog,
  tabelle, code editor, badge e colori dei grafici energia.
- Sfondo minimale: sorgente `backgrounds/oliva-bg.svg` più PNG 2560×1440
  (desktop e tablet) e 1170×2532 (smartphone).
- `backgrounds/generate-backgrounds.py` per rigenerare i PNG a qualsiasi
  risoluzione mantenendo la stessa composizione dell'SVG.
- `preview-palette.svg`: anteprima della palette per la condivisione.
- `Instructions.md` con installazione, personalizzazione, troubleshooting e
  note tecniche in italiano e inglese.
