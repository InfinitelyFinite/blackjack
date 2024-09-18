# Blackjack Game

## Overview
This is a command-line Blackjack game where the player competes against the dealer to reach a hand total as close to 21 as possible without going over. The game follows the basic rules of Blackjack, allowing the player to hit, stand, or withdraw during their turn. The dealer follows the standard Blackjack rule of standing at 17 or higher. The player's and dealer's cards are displayed in a columnar format.

## Features
- **Card Display**: Player and dealer cards are displayed in a clean, formatted columnar view. One of the dealer's cards is hidden until the dealer's turn.
- **Player Actions**: The player can choose to:
  - Hit (draw another card)
  - Stand (keep their hand as is)
  - Withdraw (end the game with their current hand)
- **Dealer Actions**: The dealer will automatically hit until their hand reaches 17 or higher.
- **Result Announcements**: The game announces the result, including whether the player or dealer busts or achieves a Blackjack.
- **Bust and Blackjack Handling**: If the player or dealer busts, the game ends immediately. If the player hits 21, the player automatically wins without further actions.

## How to Play
1. The game starts by showing the player's and dealer's hands. One of the dealer's cards will be hidden.
2. The player is prompted to hit, stand, or withdraw. After the player's turn, the dealer reveals the hidden card and plays its turn.
3. Once both turns are completed, the game announces the winner.

## Sample Game Output
<img width="342" alt="Screenshot 2024-09-17 at 19 39 57" src="https://github.com/user-attachments/assets/33b5ed4d-656d-4107-9ada-e7aed4388cc6">

# Requirements
Python 3.x
No external libraries are required.

# How to Run
  - Clone the repository:

    - git clone https://github.com/infinitelyfinite/blackjack.git

  - Navigate to the project directory:

    - cd blackjack

  - Run the game:

    - python game.py


# Future Improvements
- Adding a betting system to the game.
- Implementing a graphical user interface (GUI) using a library like Pygame.
- Enhancing the AI of the dealer for more strategic gameplay.
