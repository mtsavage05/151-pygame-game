# 151-pygame-game


Forest Duel
Forest Duel is a local two-player 2D arena game built with Python and Pygame.
Players control characters in a forest, moving, jumping, and shooting projectiles to knock out the opponent.

Features
Animated pixel characters with basic run and idle animations

Parallax forest background with multiple scrolling layers

Local two-player controls on one keyboard

Platforms that change each match using random selection

Bullet-based combat with limited shots and simple collision detection

Start screen, main PVP match, and game-over screen with winner display

Controls
Player 1 (left side)

A / D: Move left / right

W: Jump

S: Shoot toward Player 2 (max 3 bullets active)

Player 2 (right side)

Left Arrow / Right Arrow: Move left / right

Up Arrow: Jump

Down Arrow: Shoot toward Player 1 (max 3 bullets active)

Press Space on the start and game-over screens to continue.

How to Run
Install Python 3.11 or similar (3.10/3.11 recommended).

Install Pygame:
  python -m pip install pygame
  Ensure the project folder has this structure:


game-dev-project/
├─ main.py
└─ assets/
   ├─ background/
   │  ├─ parallax-forest-back-trees.png
   │  ├─ parallax-forest-lights.png
   │  └─ parallax-forest-front-trees.png
   ├─ people/
   │  ├─ _01.png
   │  └─ _02.png
   └─ music/
      └─ Amber Forest.mp3
From the project directory, run:
  python main.py
  
Code Structure
start_main(): Intro screen with animated characters and scrolling background.

movement_main(): Core PVP match loop (movement, jumping, bullets, platforms, winner logic).

game_over(): Game-over screen that shows who won (Player 1, Player 2, or Tie).

init_images(): Loads and scales all sprite sheets and background layers.

onDraw() / onDrawGO() / movment_onDraw(): Rendering functions for each game state.

onKey() / onKey2(): Handle keyboard input for both players.

movement_onTick1() / movement_onTick2(): Physics, gravity, friction, and bullet updates.

colision_detect(): Platform collision and dynamic floor adjustment.

Known Limitations / Future Ideas
No main menu or settings yet.

No sound effects beyond background music.

No single-player mode or AI opponent.

Could add health bars, rounds, power-ups, and more polished UI in future versions.
