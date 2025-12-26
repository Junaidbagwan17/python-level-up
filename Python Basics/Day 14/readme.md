# Higher–Lower Game (Python) – Project Explanation

## Project Overview

This project is a Python-based Higher–Lower game where the user compares two public figures and guesses who has more followers.  
The game continues as long as the user guesses correctly and stops when a wrong guess is made, displaying the final score.

---

## Step-by-Step Development Flow (How the Project Was Built)

### 1. Understanding the Data

The game data is a list of dictionaries, where each dictionary represents a person.

Each person contains keys such as:
- name  
- follower_count  
- description  
- country  

Before writing the game logic, we first explored how to:
- Access a single person from the list  
- Access values using dictionary keys  

---

### 2. Getting Random Persons (A and B)

A function was created to randomly select two different persons from the data.

Initially, the function only returned random values.  
Later, a validation check was added to ensure that A and B are never the same person.

This step helped in understanding:
- `random.choice()`  
- Why validation logic should be handled inside a function  

---

### 3. Displaying Person Details

After selecting persons A and B, their details were displayed:
- Name  
- Description  
- Country  

At this stage, the game only displayed data and did not perform any comparison.

This step focused on:
- Dictionary access using string keys  
- Formatting output for better readability  

---

### 4. Extracting Follower Counts

A separate function was created to extract `follower_count` from a user.

The function:
- Takes one user dictionary  
- Returns an integer follower count  

**Reason for this step:**
- Keep logic reusable  
- Separate data extraction from game flow  

---

### 5. Comparing Followers

A comparison function was added to compare follower counts of A and B.

Instead of printing results, the function returns:
- `"a"` if A has more followers  
- `"b"` if B has more followers  

This design made it easy to compare the result with user input later.

---

### 6. Taking User Guess

The user was asked to guess who has more followers: A or B.

User input was normalized using `.lower()` to avoid input errors.

At this stage:
- The game worked for only one round  
- There was no repetition or score tracking  

---

### 7. Adding Score Logic

A score variable was introduced.

- Score increases only when the user guesses correctly  
- Score remains unchanged when the guess is wrong  

This step introduced the concept of game state management.

---

### 8. Introducing the Game Loop

A `while` loop was added to repeat the game.

A control variable (`should_play`) was used to decide when the game should stop.

After this step, the game:
- Continues on correct guesses  
- Stops on a wrong guess  

---

### 9. Maintaining Game Continuity (Key Logic)

Instead of selecting new A and B every round:
- B becomes the new A  
- A new random B is selected  

This behavior matches the real Higher–Lower game logic.

This step was crucial for:
- Understanding state transitions  
- Avoiding unnecessary resets  

---

### 10. Recalculating Values Inside the Loop

Since A and B change every round:
- Follower counts  
- Winner comparison  

must be recalculated inside the loop.

This fixed logical bugs where outdated values were being reused.

---

### 11. Ending the Game

When the user guesses wrong:
- The loop stops  
- Final score is displayed  

This marks a clean and proper game termination.

---

## Key Learnings from This Project

- Difference between `print` and `return`  
- Working with lists of dictionaries  
- Importance of splitting logic into small reusable functions  
- How loops control program flow  
- How to manage and update game state  
- Debugging by moving logic inside and outside loops correctly  
