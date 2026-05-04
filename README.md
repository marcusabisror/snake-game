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
  - Mobile: swipe anywhere to turn, tap anywhere to pause; on-screen D-pad as fallback
  - Center of the D-pad doubles as a pause/resume button on mobile
  - Haptic feedback on eat / game over / win (where supported)
- **Recovery systems**
  - **Continue** from latest checkpoint (state before last food)
  - **Redo** one checkpoint at a time (from Pause or Game Over)
  - **End Game** button in the pause and continue modals to abandon the run
  - **Keys** as a shared resource for Continue/Redo usage
  - Placeholder “Watch Ad” and “Buy Keys” flows in UI
- **Audio system** (fully synthesized via the Web Audio API — no audio assets shipped)
  - Master sound toggle
  - Sound effects toggle (eat blip, descending game-over sting, win fanfare)
  - Background music toggle (chiptune lead + bass loop in A minor)
  - BGM ducks during the game-over sting and resumes after
- **Persistence**
  - High score is stored in `localStorage` and tracked per board size
  - Sideways-mode preference is stored in `localStorage`
- **Mobile / PWA**
  - Web manifest + iOS web-app meta tags so the game can be installed to the home screen and run fullscreen
  - Pre-game options panel hides during active runs to give the board more vertical space
  - Board scales to viewport height using `dvh`-based sizing
  - **Sideways mode** toggle: lays out the board on the left and the D-pad on the right; prompts you to rotate to landscape and shows a "Show/Hide Controls" toggle so the board can fill the screen
  - D-pad is centered horizontally in portrait

## Project Structure

- `index.html` – app UI, styles, and all game logic (including synthesized audio)
- `manifest.webmanifest` – PWA manifest enabling home-screen install

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

## Notes

- No backend required; everything runs client-side.
- All sound effects and background music are generated at runtime with `AudioContext`; there are no audio files to ship or regenerate.
- “Watch Ad” / “Buy Keys” actions are placeholder UX flows (not wired to ad/payment providers).

## README Maintenance

When future tasks change behavior, controls, setup, or project structure, update this README in the same change set.
