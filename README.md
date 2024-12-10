# Maze Game

Welcome to the Maze Game! This text-based adventure game lets you explore a maze, solve puzzles, and find your way to the exit. Players navigate through the maze by inputting commands to move in different directions.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Gameplay](#gameplay)
- [Commands](#commands)
- [Functions Overview](#functionsoverview)
- [License](#license)


## Overview

The **Maze Game** challenges players to navigate through a maze and reach the exit ('F'). The maze is represented in a grid format, and players can move in four directions: north, south, east, and west. With multiple difficulty levels, this game offers hours of puzzle-solving fun!

Players begin at the start position ('S') and must find their way to the finish ('F'), avoiding walls and dead-ends. As you progress, the game dynamically updates, showing your position on the map.

## Features

- **Dynamic Maze Display**: The maze is represented as a grid, where walls, open paths, start, and finish points are shown using different characters and emojis.
- **Multiple Difficulty Levels**: Choose between 4 different levels of difficulty for varied maze layouts.
- **Help Screen**: Get game instructions and tips on how to move and win.
- **Player Movement**: Navigate the maze by typing commands like "go north" or "go south."
- **Goal-Oriented Gameplay**: Reach the finish ('F') to win the game.

## Gameplay

- **Start Position**: The game begins with you at the 'S' (start) position in the maze.
- **Objective**: Move through the maze to reach the 'F' (finish) position.
- **Movement**: Use the directional commands to move up, down, left, or right.
- **Invalid Moves**: You cannot move through walls ('-'), and trying to do so will prompt an error message.
- **Finish the Maze**: Once you reach the exit ('F'), you win the game!

## Commands

- **Movement**: 
  - `go north` — Move up.
  - `go south` — Move down.
  - `go east` — Move right.
  - `go west` — Move left.

- **Exit the Game**: 
  - `escape` — Exit the game at any time.
 
## Functions Overview

The following functions make up the core logic of the Maze Game:

- **clear_screen()** : Clears the terminal to update the display after each action.
- **print_location(x, y, text)** : Prints the specified text at a given location on the screen.
- **load_map(map_file)** : Loads the maze map from the provided file.
- **find_start(grid)** : Finds the starting position ('S') in the maze grid.
- **display_map(grid, player_position)** : Displays the current state of the maze with emojis for better visualization.
- **look_around(grid, player_position)** : Returns a list of directions the player can move in based on their current position.
- **move(direction, player_position, grid)** : Moves the player in the chosen direction (if valid) and returns the updated position.
- **check_finish(grid, player_position)** : Checks if the player has reached the finish ('F') position.
- **display_help(file)** : Displays the help text from the help.txt file.
- **choose_difficulty()** : Prompts the player to choose a difficulty level and returns the corresponding map file.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
