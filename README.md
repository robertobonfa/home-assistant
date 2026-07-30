# Home Assistant Themes

Undici temi per **Home Assistant**, gratuiti e completi: palette, sfondo, istruzioni.
Eleven free themes for **Home Assistant**, complete with palette, wallpaper and instructions.

🇮🇹 [Pagina del progetto](https://robertobonfa.com/temi-home-assistant/) · 🇬🇧 [Project page](https://robertobonfa.com/home-assistant-themes/)

---

## 🎨 I temi / The themes

| Tema · Theme | Anima · Character | Primario · Primary |
|---|---|---|
| [Nordic](Nordic/) | freddo, artico · cold, arctic | `#81a1c1` |
| [Ghiaccio](Ghiaccio/) | blu profondo · deep marine blue | `#468faf` |
| [Notte](Notte/) | blu quasi nero · near-black navy | `#5a6ac9` |
| [Lavanda](Lavanda/) | viola tenue · soft purple | `#9f86c0` |
| [Uva](Uva/) | viola saturo · bold purple | `#a855d8` |
| [Salvia](Salvia/) | verde caldo · warm sage green | `#84a98c` |
| [Sunset](Sunset/) | crepuscolo · twilight, amber | `#ee6c6b` |
| [Neon](Neon/) | fluo, saturo · fluorescent, saturated | `#e01e84` |
| [Bosco](Bosco/) | verde bosco · deep forest green | `#52b788` |
| [Oceano](Oceano/) | blu-verde abissale · abyssal teal | `#52b69a` |
| [Terracotta](Terracotta/) | cotto, sabbia · fired clay, sand | `#e07a5f` |

Ogni tema usa **solo variabili supportate** dal frontend di Home Assistant: niente `card-mod`, niente CSS iniettato, niente JavaScript aggiuntivo. Nessuna variante chiara o scura, per scelta.

Every theme uses **supported theme variables only**: no `card-mod`, no injected CSS, no extra JavaScript. No light or dark variant, by choice.

---

## 📦 Contenuto di ogni cartella / Inside each folder

```
<Tema>/
├── <tema>.yaml              # il tema / the theme
├── Instructions.md          # istruzioni IT + EN / instructions IT + EN
├── preview-palette.svg      # anteprima palette / palette preview
├── changelog.md
└── backgrounds/             # sfondo 2560x1440 e 1170x2532 + sorgente SVG
```

---

## 🚀 Installazione rapida / Quick install

1. Copia `<tema>.yaml` in `themes/` dentro la cartella di configurazione (quella con `configuration.yaml`).
   
   Copy `<theme>.yaml` into `themes/` inside your configuration folder (the one with `configuration.yaml`).
2. Copia i due PNG in `www/<tema>/` e aggiungi a `configuration.yaml`:
   
   Copy the two PNGs into `www/<theme>/` and add to `configuration.yaml`:
   
   ```yaml
   frontend:
     themes: !include_dir_merge_named themes
   ```
3. Riavvia (o *Strumenti per sviluppatori → YAML → Ricarica temi*), poi profilo utente → **Tema**.
   
   Restart (or *Developer tools → YAML → Reload themes*), then user profile → **Theme**.

La procedura completa, con tutte le varianti (File editor, Studio Code Server, SSH, Samba), è nel file `Instructions.md` di ogni tema.

The full procedure, covering every access method, is in each theme's `Instructions.md`.

---

## 📄 Licenza / License

[MIT](LICENSE) — usali, modificali, ridistribuiscili. Se ne nasce qualcosa di bello, fammelo sapere.

[MIT](LICENSE) — use them, change them, redistribute them. If something nice comes out of it, let me know.
