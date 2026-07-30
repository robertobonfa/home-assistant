# Changelog

Tutte le modifiche rilevanti a questo tema sono documentate in questo file.

Il formato segue [Keep a Changelog](https://keepachangelog.com/it/1.1.0/)
e il progetto aderisce al [Semantic Versioning](https://semver.org/lang/it/).

## [1.1.0] - 2026-07-30

### Changed

- Gli interruttori accesi usavano `#a5c3a0`, lo stesso salvia chiaro dello
  stato attivo generico: su una palette monocromatica verde il cambio di stato
  era praticamente invisibile. `state-switch-active-color` passa a `#e9c46a`,
  lo stesso oro gia usato dalle luci.
- Stesso trattamento a `state-input_boolean-active-color` e
  `state-fan-active-color`: tutto cio che si comanda diventa caldo quando e
  acceso. Gli stati passivi (sensori, automazioni, presenza) restano sul
  salvia chiaro, cosi il caldo resta un segnale e non un colore di sfondo.

## [1.0.0] - 2026-07-26

### Added

- Tema `salvia.yaml` per Home Assistant, 185 variabili, interamente dichiarato
  sotto `modes: dark:`.
- Mappatura completa della rampa Salvia a 8 stop (`#2f3e46` → `#eef1ec`) presa
  dalla palette omonima di `wallpapers.robertobonfa.com` (`js/app.js:125`).
- Accenti semantici caldi e desaturati, scelti per convivere con una rampa
  monocromatica verde: `#c1666b` errore, `#d9ae5f` avviso, `#7fb069` successo,
  `#e9c46a` per il dominio `light` attivo.
- Colori di stato per tutti i domini supportati da Home Assistant
  (`state-{domain}-{state}-color`), inclusi i `device_class` di `binary_sensor`
  e i sotto-stati di `alarm_control_panel`, `climate`, `lock` e `update`.
- Copertura di card, sidebar, header, switch, slider, input MDC, dialog,
  tabelle, code editor, badge e colori dei grafici energia.
- Sfondo minimale: sorgente `backgrounds/salvia-bg.svg` più PNG
  2560×1440 (desktop e tablet) e 1170×2532 (smartphone).
- `backgrounds/generate-backgrounds.py` per rigenerare i PNG a qualsiasi
  risoluzione mantenendo la stessa composizione dell'SVG.
- `preview-palette.svg`: anteprima della palette per la condivisione.
- `Instructions.md` con installazione, personalizzazione, troubleshooting e
  note tecniche in italiano e inglese, già comprensive degli avvisi su HAOS,
  File editor e SFTP maturati durante l'installazione del tema Nordic.
