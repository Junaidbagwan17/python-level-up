
# Blackjack Game (Python)

This is a console-based Blackjack game built using Python.  
The project focuses on game logic, clean function design, and control flow.

## Features
- Random card dealing
- Blackjack detection (Ace + 10-value card)
- Ace value adjustment (11 → 1 when score exceeds 21)
- User vs Computer gameplay
- Dealer follows standard Blackjack rules (draw until score ≥ 17)
- Replay option

## Game Logic Overview
- Cards are dealt randomly using a helper function.
- Scores are calculated using a dedicated function.
- Blackjack is detected only in the initial hand (2 cards).
- The user decides whether to draw more cards.
- The computer draws cards automatically based on rules.
- Final scores are compared to decide the winner.

## Concepts Used
- Functions
- Lists
- Loops (`while`)
- Conditional statements
- Game flow control
- Modular code design

-------------------
Blackjack Game Logic – Step-by-Step Explanation

First, we created a deal_card() function whose responsibility is to return one random card value from a predefined list of possible Blackjack cards. This helped us centralize the card-dealing logic so that both the user and the computer can receive cards in the same way. Next, we created a caluculated_score() function to calculate the total score of a hand. Inside this function, we handled two important Blackjack rules: if a hand has exactly two cards and their sum is 21, we return 0 to represent a Blackjack; and if the hand contains an Ace (11) and the score exceeds 21, we convert the Ace from 11 to 1 to prevent busting. After that, we created a compare() function that takes the user’s score and the computer’s score and decides the game result by checking conditions in the correct priority order, such as draw, Blackjack cases, bust cases, and finally higher score wins.

Then we built the main play_game() function, where the actual game flow happens. Inside this function, we initialized empty lists for the user’s cards and the computer’s cards, along with a boolean variable to control the game loop. We dealt two initial cards to both the user and the computer using the deal_card() function. After dealing, we entered a loop that runs until the game is over. In this loop, we continuously calculated the scores for both players, displayed the user’s full hand and score, and showed only the computer’s first card. We then checked for immediate game-ending conditions such as Blackjack or the user going over 21. If the game was not over, we asked the user whether they wanted another card; if yes, we dealt a new card to the user, otherwise we ended the user’s turn.

Once the user’s turn finished, we let the computer play automatically by drawing cards while its score was below 17 and it did not have a Blackjack, following standard Blackjack dealer rules. Finally, we printed both the user’s and computer’s final hands and scores, and passed those scores to the compare() function to determine and display the final result. Outside the game function, we wrapped the entire game in a loop that asks the user whether they want to play again, allowing the Blackjack game to restart cleanly without repeating code.


🔑 One-line recall sentence 
The Blackjack game is built by separating card dealing, score calculation, game flow, and result comparison into clear functions
