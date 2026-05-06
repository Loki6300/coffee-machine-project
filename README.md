# Coffee Machine Project ☕

A Python-based **Coffee Machine Simulator** built using **Object-Oriented Programming (OOP)** concepts. This beginner-friendly project demonstrates how classes, objects, constructors, and methods work together to simulate a real coffee machine.

---

## Features

- Order **Espresso**, **Latte**, or **Cappuccino**
- **Resource management** — tracks water, milk, and coffee beans
- **Payment processing** — accepts 5, 10, and 20 rupee coins
- **Change calculation** — refunds extra money automatically
- **Report command** — view current stock and total money collected
- **Input validation** — handles invalid inputs gracefully

---

## OOP Concepts Used

| Class | Responsibility |
|---|---|
| `MenuItem` | Stores drink name, ingredients, and price |
| `Menu` | Manages all drinks, displays menu, finds drink by name |
| `CoffeeMaker` | Manages machine resources and makes coffee |
| `MoneyMachine` | Handles coin input, payment verification, and change |

---

## How to Run

```bash
python coffee_machine_project.py
```

---

## Usage

```
What would you like? (espresso/latte/cappuccino) : latte
```

| Command | Action |
|---|---|
| `espresso` | Order an Espresso — Rs. 30 |
| `latte` | Order a Latte — Rs. 50 |
| `cappuccino` | Order a Cappuccino — Rs. 60 |
| `report` | View current resources and money |
| `off` | Shut down the machine |

---

## Drink Menu

| Drink | Water | Milk | Coffee | Price |
|---|---|---|---|---|
| Espresso | 50 ml | 0 ml | 18 g | Rs. 30 |
| Latte | 200 ml | 150 ml | 24 g | Rs. 50 |
| Cappuccino | 250 ml | 100 ml | 24 g | Rs. 60 |

---

## Coins Accepted

- 5 Rupee
- 10 Rupee
- 20 Rupee

---

## Sample Output

```
=======================================================
         ***  WELCOME TO COFFEE MACHINE  ***
=======================================================
  Drink            Water     Milk   Coffee    Price
-------------------------------------------------------
  Espresso          50ml      0ml    18g   Rs.30.00
  Latte            200ml    150ml   24g    Rs.50.00
  Cappuccino       250ml    100ml   24g    Rs.60.00
=======================================================

  What would you like? (espresso/latte/cappuccino) : latte

  [COINS]  INSERT YOUR COINS
  ------------------------------
  How many 5 rupee coins?  : 0
  How many 10 rupee coins? : 5
  How many 20 rupee coins? : 0

  [OK] Payment accepted! Exact amount received.

  [**] Here is your Latte! Enjoy! :)
```

---

## Requirements

- Python 3.x
- No external libraries needed

---

## Project Structure

```
Coffee Machine Project/
│
└── coffee_machine_project.py   # Main file with all classes and logic
```

---

## Author

**Lokesh**

---

> Built as a beginner Python OOP learning project.
