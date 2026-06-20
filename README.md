# Simple Snake Game

A classic Snake game built completely in Python using the built-in `turtle` module! This project helped me move past standard tutorials to independently understand game loops, coordinate grid tracking, and object collision logic.

## Key Learnings & Problem Solving
* **Screen Optimization:** Used `sc.tracer(0)` and `sc.update()` to stop choppy rendering and handle smooth frame transitions manually.
* **Collision Math:** Calculated precise 20-pixel boundaries relative to the 600x600 grid to prevent the snake and food from rendering out-of-bounds.
* **Memory Workarounds:** Dealt with Turtle's limitation of not being able to easily delete instantiated objects by safely teleporting dead body segments off-screen (`1000, 1000`) during a game reset.

## Features
* Smooth, grid-bound snake movement.
* Real-time score tracking and persistent High Score preservation.
* Progressive difficulty (the game speeds up slightly as the snake grows!).
* Prevented self-collision bugs by blocking immediate opposite-direction input.

## How to Run

### Prerequisites
Because this project uses Python's standard library, **no external dependencies (like Pygame) are required!** You just need Python installed on your system.

### Execution
Clone the repository and run the main script directly from your terminal:
python Snake.py

##Controls
You can control the snake using either the Arrow keys or standard WASD layouts:

Up / W: Move Up

Down / S: Move Down

Left / A: Move Left

Right / D: Move Right
