# Coffee Machine Pro ☕

A professional Python **Coffee Machine Simulator** built using **Object-Oriented Programming (OOP)**. This project simulates a real-world coffee machine — managing resources, processing payments, logging orders, and persisting data across sessions.

---

## Version 2.0 — What's New

- 3 new drinks: Mocha, Black Coffee, Cold Coffee (6 drinks total)
- Admin **refill** command to restock ingredients
- **Order logging** — every order saved to `orders.txt`
- **Billing receipt** printed after every successful order
- **Persistent profit** — total earnings saved in `profit.txt`
- Improved input validation and error messages
- Cleaner console UI with formatted tables

---

## Features

| Feature | Description |
|---|---|
| 6 Drink Options | Espresso, Latte, Cappuccino, Mocha, Black Coffee, Cold Coffee |
| Resource Management | Tracks water, milk, and coffee levels |
| Payment Processing | Accepts 5, 10, 20 rupee coins |
| Change Calculation | Auto-refunds extra money |
| Billing Receipt | Prints itemized receipt after every order |
| Order Logging | Saves all orders with timestamp to `orders.txt` |
| Persistent Profit | Saves total earnings in `profit.txt` — reloads on restart |
| Refill Command | Admin can top up water, milk, and coffee stock |
| Input Validation | Handles invalid names, negative coins, empty input |

---

## Technologies Used

- **Language:** Python 3
- **Concepts:** OOP, Classes, Constructors, Methods, File I/O
- **Libraries:** `os` (built-in), `datetime` (built-in)
- **No external dependencies**

---

## Project Structure

```
Coffee Machine Project/
│
├── coffee_machine_project.py   # Main file — all classes and logic
├── orders.txt                  # Auto-created — logs every order
├── profit.txt                  # Auto-created — saves total earnings
├── README.md                   # Project documentation
└── .gitignore                  # Git ignore rules
```

---

## OOP Class Structure

```
MenuItem      -- Recipe card for each drink (name, ingredients, cost)
     |
Menu          -- Menu board (stores all drinks, finds drink by name)
     |
CoffeeMaker   -- Machine engine (check resources, refill, make coffee)
     |
MoneyMachine  -- Cash register (coins, payment, change, profit.txt)
     |
OrderLogger   -- Receipt printer + order logger (orders.txt)
```

---

## How to Run

```bash
python coffee_machine_project.py
```

No installation required. Python 3.x only.

---

## Commands

| You Type | Action |
|---|---|
| `espresso` | Order Espresso — Rs.30 |
| `latte` | Order Latte — Rs.50 |
| `cappuccino` | Order Cappuccino — Rs.60 |
| `mocha` | Order Mocha — Rs.70 |
| `black coffee` | Order Black Coffee — Rs.25 |
| `cold coffee` | Order Cold Coffee — Rs.65 |
| `report` | View current resources and total profit |
| `refill` | Refill machine stock (admin) |
| `off` | Shut down the machine |

---

## Drink Menu

| # | Drink | Water | Milk | Coffee | Price |
|---|---|---|---|---|---|
| 1 | Espresso | 50 ml | 0 ml | 18 g | Rs. 30 |
| 2 | Latte | 200 ml | 150 ml | 24 g | Rs. 50 |
| 3 | Cappuccino | 250 ml | 100 ml | 24 g | Rs. 60 |
| 4 | Mocha | 200 ml | 50 ml | 30 g | Rs. 70 |
| 5 | Black Coffee | 200 ml | 0 ml | 18 g | Rs. 25 |
| 6 | Cold Coffee | 100 ml | 200 ml | 24 g | Rs. 65 |

---

## Coins Accepted

- 5 Rupee
- 10 Rupee
- 20 Rupee

---

## Sample Output

```
=================================================================
             ***  COFFEE MACHINE PRO  ***
=================================================================
  #   Drink           Water    Milk   Coffee    Price
-----------------------------------------------------------------
  1   Espresso          50ml     0ml    18g   Rs.30.00
  2   Latte            200ml   150ml    24g   Rs.50.00
  3   Cappuccino       250ml   100ml    24g   Rs.60.00
  4   Mocha            200ml    50ml    30g   Rs.70.00
  5   Black Coffee     200ml     0ml    18g   Rs.25.00
  6   Cold Coffee      100ml   200ml    24g   Rs.65.00
=================================================================
  Commands: report | refill | off
=================================================================

  Your choice : latte

  [COINS]  Paying for Latte
  -----------------------------------
  How many 5 rupee coins?  : 0
  How many 10 rupee coins? : 5
  How many 20 rupee coins? : 0

==================================================
            BILLING RECEIPT
==================================================
  Date / Time  : 06-05-2026  03:30 PM
  Drink        : Latte
  Cost         : Rs.50.00
  Amount Paid  : Rs.50.00
  Change       : No change (Exact payment)
--------------------------------------------------
  Status       : Payment Successful
==================================================
       Thank you! Enjoy your coffee!
==================================================
```

---

## Sample orders.txt

```
[2026-05-06 15:30:00]  |  Latte           |  Cost: Rs.50.00  |  Paid: Rs.50.00  |  Change: Rs.0.00
[2026-05-06 15:35:22]  |  Espresso        |  Cost: Rs.30.00  |  Paid: Rs.40.00  |  Change: Rs.10.00
[2026-05-06 15:42:10]  |  Mocha           |  Cost: Rs.70.00  |  Paid: Rs.80.00  |  Change: Rs.10.00
```

---

## What I Learned

- Designing multiple classes that interact with each other
- Using `__init__` constructors to initialize objects
- File I/O — reading and writing `.txt` files
- Input validation with `try/except`
- Modular, clean code structure using OOP principles

---

## Author

**Lokesh**
GitHub: [github.com/Loki6300](https://github.com/Loki6300)

---

> Built as a Python OOP learning project — beginner friendly, resume ready.
