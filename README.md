# Pokémon Top Trumps - Best of Three

## 📌 Overview

Pokémon Top Trumps is a command-line game where players battle using randomly assigned Pokémon and their moves. The game is a "best of three" format—whoever wins three rounds first is the champion!

## 🎮 How to Play

1. You are assigned a random Pokémon with three randomly selected moves.
2. Choose one move to use in battle.
3. Your opponent (CPU) also picks a random Pokémon and move.
4. The move with the **higher power** wins the round.
5. First to **three wins** is the overall winner!
6. After each game, you can choose to play again.

## 🛠 Installation

### Prerequisites

- Python 3
- Internet connection (the game fetches Pokémon data from the PokeAPI: https://pokeapi.co/)

### Steps

1. Clone this repository:
   git clone https://github.com/cupcakeio/cuddly-train.git
2. cd cuddly-train
3. pip install requests
4. pokemon.py

## 🏆 Game Rules

Each Pokémon has a list of moves with different power levels.
If your selected move has a higher power than the opponent’s, you win the round.
If the opponent’s move is stronger, they win.
If the moves have the same power, it’s a draw and no one wins.
The first player to win three rounds wins the game.
