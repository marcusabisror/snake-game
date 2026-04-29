# Snake Game (Browser)

A single-file, browser-based Snake game built with **HTML5 Canvas + vanilla JavaScript**.

It includes desktop + mobile controls, configurable board/speed options, sound controls, local high scores, and recovery mechanics (Continue/Redo) with optional key usage.

## Current Features

- **Game setup panel**
  - Start game button
  - Board sizes: `16×16`, `14×14`, `10×10`, `8×8`, `4×4 (Practice)`
  - Speed modes: `Regular`, `Fast`
  - How To Play modal
  - Sound settings modal
- **Gameplay + UI**
  - Canvas-rendered snake + food
  - Progress tube toward full-board win condition
  - Score + best score display
  - Dynamic speed scaling as score increases
  - Pause/resume with countdown overlay
  - Game-over and win overlays (with celebration effect on win)
- **Controls**
  - Desktop: Arrow keys + `Space` to pause/resume
  - Mobile: swipe on the board to turn, on-screen D-pad as fallback, Pause button
  - Center of the D-pad doubles as a pause/resume button on mobile
  - Haptic feedback on eat / game over / win (where supported)
- **Recovery systems**
  - **Continue** from latest checkpoint (state before last food)
  - **Redo** one checkpoint at a time (from Pause or Game Over)
  - **Keys** as a shared resource for Continue/Redo usage
  - Placeholder “Watch Ad” and “Buy Keys” flows in UI
- **Audio system**
  - Master sound toggle
  - Sound effects toggle
  - Background music toggle
  - Pre-generated WAV assets in `sounds/`
- **Persistence**
  - High score is stored in `localStorage` and tracked per board size
- **Mobile / PWA**
  - Web manifest + iOS web-app meta tags so the game can be installed to the home screen and run fullscreen
  - Pre-game options panel hides during active runs to give the board more vertical space
  - Board scales to viewport height using `dvh`-based sizing
  - **Sideways mode** toggle: places the board on the left and the D-pad on the right (best when the phone is held in landscape); the choice is persisted in `localStorage`
  - D-pad is centered horizontally in portrait

## Project Structure

- `index.html` – app UI, styles, and all game logic
- `manifest.webmanifest` – PWA manifest enabling home-screen install
- `sounds/` – audio assets used by the game
- `generate_sounds.py` – regenerates core sound assets
- `beep.py`, `bg_music.py`, `game_over.py` – helper scripts for sound generation

## Run Locally

Run a local web server from the project root:

```bash
python3 -m http.server 8000
```

Open:

```text
http://localhost:8000
```

> You can also use VS Code Live Server.

## Optional: Regenerate Sounds

```bash
python3 generate_sounds.py
```

This rewrites sound files inside `sounds/`.

## Notes

- No backend required; everything runs client-side.
- “Watch Ad” / “Buy Keys” actions are placeholder UX flows (not wired to ad/payment providers).

## README Maintenance

When future tasks change behavior, controls, setup, or project structure, update this README in the same change set.
