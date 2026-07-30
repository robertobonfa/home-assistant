# Changelog

Tutte le modifiche rilevanti a questo tema sono documentate in questo file.

Il formato segue [Keep a Changelog](https://keepachangelog.com/it/1.1.0/)
e il progetto aderisce al [Semantic Versioning](https://semver.org/lang/it/).

## [1.0.0] - 2026-07-26

### Added

- Tema `sunset.yaml` per Home Assistant, 185 variabili, interamente dichiarato
  sotto `modes: dark:`.
- Mappatura completa della rampa Sunset a 8 stop (`#1d1135` → `#ffe8b0`) presa
  dalla palette omonima di `wallpapers.robertobonfa.com` (`js/app.js:123`).
- Accenti semantici: `#e01e37` errore, `#ffb703` avviso, `#3fb98a` successo,
  `#ffd166` per il dominio `light` attivo.
- Colori di stato per tutti i domini supportati da Home Assistant
  (`state-{domain}-{state}-color`), inclusi i `device_class` di
  `binary_sensor` e i sotto-stati di `alarm_control_panel`, `climate`, `lock`
  e `update`.
- Copertura di card, sidebar, header, switch, slider, input MDC, dialog,
  tabelle, code editor, badge e colori dei grafici energia.
- Sfondo minimale: sorgente `backgrounds/sunset-bg.svg` più PNG 2560×1440
  (desktop e tablet) e 1170×2532 (smartphone).
- `backgrounds/generate-backgrounds.py` per rigenerare i PNG a qualsiasi
  risoluzione mantenendo la stessa composizione dell'SVG.
- `preview-palette.svg`: anteprima della palette per la condivisione.
- `Instructions.md` con installazione, personalizzazione, troubleshooting e
  note tecniche in italiano e inglese.
