# Object-Oriented Programming (OOP) – Complete Notes (Day 16)

Author: Junaid  
Level: Beginner → Intermediate Transition  
Goal: Strong OOP foundation for real projects & interviews

---

## 1. Why OOP Exists (Restaurant Analogy 🍽️)

I understood OOP by imagining a **real-world restaurant**.

A restaurant has different staff:
- Waiter
- Chef
- Cleaner
- Cashier

In real life:
- One person cannot efficiently do all jobs
- Even if one person tries, they can only handle a few customers
- As customers increase, work becomes **complex and messy**

So we **split the work**:
- Each staff member has a **specific responsibility**
- Everyone is trained to do **one job well**

### Same problem in coding ❌
When all logic is written in one place:
- Code becomes very long
- Hard to read and debug
- Difficult to add new features
- Difficult to reuse code

### OOP Solution ✅
OOP solves this by:
- Splitting code into **objects**
- Each object has **one responsibility**
- Objects collaborate like a team

> **OOP is about managing complexity by dividing responsibilities.**

---

## 2. Core Idea of OOP (One Line)

> **Object-Oriented Programming means designing programs using real-world objects.**

Each object has:
- **Attributes** → what it *has*
- **Methods** → what it *does*

---

## 3. Class and Object (Foundation 🔑)

### Class
- Blueprint / design
- Defines attributes and methods
- Does NOT store real data

### Object

Example:
Real instance created from a class
Stores actual data
Uses methods
Example:
```my_car = Car()```
Class = blueprint
Object = real thing created from the blueprint

### 4. Example: Waiter as a Class 👨‍🍳
Real-life thinking
A waiter:
- Has responsibilities
- Performs actions
  
#### OOP Mapping
Class: *Waiter*

#### Attributes (has):

``` is_holding_plate = True
tables_responsible = [2, 5, 9]
```
### Methods (does):
take_order(table, order)

take_payment(amount)

```
def take_order(self, table, order):
      # go and tgake order from table
def take_payment(self, amount):
     # send bill to the counter
```

#### Objects (real waiters):
1. jerry = Waiter()
2. michel = Waiter()
3. ben = Waiter()

*One class → many objects*


## 5. Attributes vs Methods (Very Important)

### Attributes
- Store data
- Do not use brackets () uses .
*car.speed*

### Methods
- perform actions
- Always use brackets ()
*car.drive()*

### 6. Understanding self

self represents the current object itself.

If:
````car1 = Car()```

Inside the class:
self refers to car1

### Why we use self:
To store data inside the object
To access object-specific attributes


## 7. OOP Flow Using Coffee Machine ☕ (Mental Model)

### Objects involved
- **Menu** → knows available drinks
- **CoffeeMaker** → manages resources and makes coffee
- **MoneyMachine** → handles money
- **main.py** → controls the flow

### Logical Flow
- Ask user for input
- If `off` → stop machine
- If `report` → show status
- Ask menu if drink exists
- Check resources
- Take payment
- Serve coffee

Main file coordinates — objects do the work.

---

## 8. Package vs Module (Common Confusion ❗)

### Module
- A single `.py` file
- Contains functions, classes, and variables

**Examples:**
- `menu.py`
- `coffee_maker.py`
- `money_machine.py`

### Package
- A folder containing multiple modules
- Used for large libraries

---

## 9. Example: `prettytable` 📦

- `prettytable` → package
- `PrettyTable` → class

```
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Name", ["A", "B"])
```
### Mapping
- Package → `prettytable`
- Class → `PrettyTable`
- Method → `add_column()`
- Attribute → `.align`
---
## 10. Example: `turtle` 🐢

```
from turtle import Turtle
t = Turtle()
t.forward(100)
```
### Mapping
- `turtle` → package/module
- `Turtle` → class
- `t` → object
- `forward()` → method

----

**Object-Oriented Programming helps manage complex programs by organizing code into objects that represent real-world entities, each responsible for its own data and behavior.**
