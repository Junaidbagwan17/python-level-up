# ☕ Coffee Machine Project (Python)

This project simulates a real-world **Coffee Machine** using Python.
It was built step by step using **functions, loops, dictionaries, and conditionals**.

The project handles:
- drink selection
- resource management
- coin processing
- payment validation
- change return
- coffee preparation
- profit tracking

---

## 📁 Project Structure

coffee-machine/
│
- ├── main.py # Contains MENU, resources, ASCII coffee art

- ├── coffee_machine.py # Main logic of the coffee machine

---

## 🧠 Step-by-Step Development Process

### STEP 1: Project Understanding
- Identified requirements:
  - Espresso, Latte, Cappuccino
  - Limited resources (water, milk, coffee)
  - Coin-based payment
  - Change return
  - Continuous machine loop
  - `report` and `off` commands

---

### STEP 2: Data Design (`main.py`)
- Created a `MENU` dictionary:
  - Ingredients required for each drink
  - Cost of each drink
- Created a `resources` dictionary:
  - Water, milk, coffee, money

This separated **data** from **logic**, making the program clean and scalable.

---

### STEP 3: Main Loop
- Used a `while` loop to keep the machine running
- Took user input repeatedly:
What would you like? (espresso/latte/cappuccino):


- Added command handling:
- `off` → stops the machine
- `report` → prints current machine status

---

### STEP 4: Report Function
- Created `get_report()` to display:
- Water
- Milk
- Coffee
- Money
- Used formatted output for readability

---

### STEP 5: Resource Validation
- Built `check_resources()` function:
- Fetches required ingredients from `MENU`
- Loops only through required ingredients
- Compares with available `resources`
- Stops early if any ingredient is insufficient

Why?
- Espresso doesn’t require milk
- Prevents unnecessary checks
- Matches real-world behavior

---

### STEP 6: Coin Processing
- Built `take_money()` function:
- Accepts coin input (quarters, dimes, nickels, pennies)
- Converts coin count into money value
- Returns total money inserted

Coin values:
- Quarter → $0.25
- Dime → $0.10
- Nickel → $0.05
- Penny → $0.01

---

### STEP 7: Payment Validation
- Compared `money_received` with `drink_cost`
- Two cases handled:
- ❌ Not enough money → refund message
- ✅ Enough or extra money → continue process

---

### STEP 8: Change Calculation
- If money received is more than cost:
- Calculated change:
  ```
  change = money_received - drink_cost
  ```
- Rounded change to 2 decimal places
- Returned change to user

---

### STEP 9: Resource Deduction
- Created `make_coffee()` function:
- Deducts ingredients used by the selected drink
- Updates `resources` correctly
- Milk is deducted only when required

---

### STEP 10: Profit Tracking
- Added **only the drink cost** to machine money
- Extra money returned as change
- Ensures correct profit calculation

---

### STEP 11: Serve Coffee
- Printed confirmation message:
Here is your espresso ☕. Enjoy!


- Displayed coffee ASCII art for better user experience

---

### STEP 12: Continuous Operation
- After each transaction:
- Machine returns to input prompt
- Ready to serve the next customer

---

## ✅ Final Features

✔ Continuous machine loop  
✔ Resource management  
✔ Coin-based payment  
✔ Refund handling  
✔ Change return  
✔ Coffee preparation  
✔ Profit tracking  
✔ Clean modular design  

---

## 🎯 Skills Demonstrated

- Python fundamentals
- Dictionaries & loops
- Functions & modular design
- Conditional logic
- Real-world problem modeling
- Debugging & incremental development

## 🚀 Conclusion
This Coffee Machine project was built step by step to simulate a real-world ordering and payment system.
It demonstrates core Python concepts such as functions, loops, dictionaries, and conditional logic.
The program efficiently manages resources, processes payments, returns change, and tracks profit.
By building the project incrementally, the logic remains clear, modular, and easy to maintain.

☕ Happy Coding!
