# Snake Game (Browser)

A polished browser-based Snake game built with **HTML5 Canvas + vanilla JavaScript**, with retro sound effects, pause/resume, and extra recovery mechanics (Continue and Redo).

## Features

- Adjustable game speed (`Slow`, `Regular`).
- Adjustable board sizes (`16x16`, `14x14`, `10x10`, `8x8`, `4x4 Practice`).
- Keyboard controls (Arrow keys) with **Space** to pause/resume.
- In-game overlays for pause, game over, and resume countdown.
- Sound system with toggles:
  - Master Sound
  - Sound Effects
  - Background Music
- Extra gameplay systems:
  - **Continue**: return to state before the last food was eaten.
  - **Redo**: repeatedly step back eat-by-eat.
  - **Keys**: shared resource for Continue/Redo uses.

## Project Structure

- `index.html` – main game UI, styles, and game logic.
- `sounds/` – generated audio assets used by the game.
- `generate_sounds.py` – generates key game sound files into `sounds/`.
- `beep.py`, `bg_music.py`, `game_over.py` – helper scripts for custom sound generation.

## Run Locally

Because browsers restrict local file audio in some cases, run a tiny local web server instead of opening `index.html` directly.

### Option 1: Python

```bash
python3 -m http.server 8000
```

Then open:

```text
http://localhost:8000
```

### Option 2: VS Code Live Server

Open the repo folder in VS Code and run **Live Server** on `index.html`.

## Controls

- **Arrow Keys**: move snake
- **Space** or **Pause button**: pause/resume
- **Start Game**: start a new game with selected settings
- **Restart**: restart after game over

## Sound Asset Generation (Optional)

If you want to regenerate sounds:

```bash
python3 generate_sounds.py
```

This writes game sound files into the `sounds/` folder.

## Notes

- This game is fully client-side (no backend required).
- Ad buttons in the UI are currently gameplay placeholders and can be wired to real ad flows later.

## License

No license file is currently included. Add one (for example, MIT) if you plan to publish or share broadly.
