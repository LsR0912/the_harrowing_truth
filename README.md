# The Harrowing Truth

**The Harrowing Truth** is a dark and bloody text adventure game written in Python. Explore mysterious rooms, interact with NPCs, collect items, and uncover secrets as you navigate a chilling narrative.

## Features

- Multiple rooms with unique descriptions and items
- Inventory and item management
- NPC interactions and dialogue
- Experience and leveling system
- Save and load player progress

## Requirements

- Python 3.10+
- [rich](https://pypi.org/project/rich/) (for colored console output)

Install dependencies with:

```sh
pip install -r requierements.txt
```

## Getting Started

1. Clone the repository or download the source code.
2. Ensure you have Python and the required packages installed.
3. Run the game from the `src` directory:

```sh
python main.py
```

## Project Structure

```
requierements.txt
data/
    players.json
src/
    game.py
    item.py
    main.py
    npc.py
    player.py
    room.py
    utils/
        commands.py
        print_helper.py
```

- `src/main.py`: Entry point for the game.
- `src/game.py`: Main game logic and loop.
- `src/player.py`: Player class and save/load functionality.
- `src/room.py`: Room definitions and logic.
- `src/item.py`: Item definitions.
- `src/npc.py`: NPC definitions and interactions.
- `src/utils/`: Helper functions for commands and printing.

## Saving and Loading

Player progress is automatically saved to `data/players.json`. When you start the game, you can continue from your last save or create a new character.

## Commands

Type commands to interact with the game. Some available commands:

- `go [direction]` — Move to another room (e.g., `go north`)
- `look` — Look around the current room
- `take [item]` — Pick up an item
- `examine [item]` — Examine an item in your inventory
- `inventory` — Show your inventory
- `stats` — Show your player stats
- `talk` — Talk to an NPC in the room
- `help` — Show available commands
- `quit` — Exit the game

## License
MIT

This project is for educational purposes.

---

Enjoy your adventure in **The Harrowing Truth**!
