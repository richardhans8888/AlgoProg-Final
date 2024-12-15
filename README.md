
# Tetris Game

## Description
This project is a Tetris game built using Python and Pygame. The game includes core Tetris mechanics, such as block movement, rotation, line clearing, and scoring. Additional features like dynamic speed adjustment and high scores make it engaging and replayable.

---

## Features
- **Core Gameplay**:
  - Classic Tetris mechanics: falling Tetromino blocks, rotation, and line clearing.
  - Game-over state detection.

- **Dynamic Speed**:
  - The game increases difficulty as players progress, with blocks falling faster as levels increase.

- **High Scores**:
  - Persistent high scores system to save and display top scores across sessions.

- **Sound Effects and Music**:
  - Rotation, clearing lines, and background music to enhance the experience.

- **Block Preview**:
  - Displays the next block to help players plan their moves.

- **Game Reset**:
  - Restart the game without exiting.

---

## File Structure

### Core Game Files
- **`main.py`**:
  - Entry point for the game.
  - Handles rendering, main game loop, and interaction with the `Game` class.

- **`game.py`**:
  - Core game logic.
  - Manages the grid, blocks, scoring, and game states.

- **`grid.py`**:
  - Handles the 10x20 Tetris grid.
  - Clears full rows and checks block placement validity.

- **`blocks.py`**:
  - Defines Tetromino shapes (I, J, L, O, S, T, Z).
  - Inherits from the base `Block` class.

- **`block.py`**:
  - Base class for blocks.
  - Manages block attributes like position, ID, and rotation.

- **`position.py`**:
  - Utility class for managing grid positions.

- **`colors.py`**:
  - Defines color schemes for blocks and the grid.

---

## How to Run
1. **Install Python**:
   - Ensure you have Python installed on your system. Download it from [python.org](https://www.python.org/).

2. **Install Dependencies**:
   - Install Pygame using pip:
     ```
     pip install pygame
     ```

3. **Run the Game**:
   - Navigate to the project directory in your terminal and run:
     ```
     python main.py
     ```

---



