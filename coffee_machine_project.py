# -*- coding: utf-8 -*-
# ================================================================
#          ***  COFFEE MACHINE PRO  ***
#          Python OOP Project  |  Version 2.0
#          Language: Python 3
# ================================================================
#
# NEW IN VERSION 2.0:
#   - 3 new drinks: Mocha, Black Coffee, Cold Coffee
#   - Refill command for admin
#   - Order logging to orders.txt
#   - Billing receipt after every order
#   - Persistent profit saved in profit.txt
#   - Better input validation
#   - Cleaner console UI
#
# HOW CLASSES INTERACT:
#
#   MenuItem  <-- holds recipe (ingredients + price)
#       |
#   Menu      <-- stores all MenuItems, shows menu, finds drink
#       |
#   CoffeeMaker <-- checks resources, refills, makes coffee
#       |
#   MoneyMachine <-- takes coins, verifies payment, gives change
#       |            saves/loads profit from profit.txt
#   OrderLogger  <-- logs orders to orders.txt, prints receipt
#       |
#   main()    <-- connects everything, runs the machine loop
#
# ================================================================

import os
from datetime import datetime


# ────────────────────────────────────────────────────────────────
# CLASS 1: MenuItem
# A single drink "recipe card" — stores name, ingredients, price.
# ────────────────────────────────────────────────────────────────
class MenuItem:
    """
    Represents one drink item on the menu.
    Each drink has a name, ingredients needed, and a price.
    """

    def __init__(self, name, water, milk, coffee, cost):
        """
        Constructor — called automatically when a MenuItem is created.

        Parameters:
            name   (str)   : Drink name (e.g., "latte")
            water  (int)   : Water needed in ml
            milk   (int)   : Milk needed in ml
            coffee (int)   : Coffee beans needed in grams
            cost   (float) : Price in rupees
        """
        self.name = name
        self.ingredients = {
            "water":  water,
            "milk":   milk,
            "coffee": coffee,
        }
        self.cost = cost

    def __str__(self):
        """Readable string representation of a drink."""
        return (f"{self.name.capitalize():<14} | "
                f"Water: {self.ingredients['water']:>4}ml | "
                f"Milk: {self.ingredients['milk']:>4}ml | "
                f"Coffee: {self.ingredients['coffee']:>3}g | "
                f"Rs.{self.cost:.2f}")


# ────────────────────────────────────────────────────────────────
# CLASS 2: Menu
# The full menu board — lists all drinks, finds a drink by name.
# ────────────────────────────────────────────────────────────────
class Menu:
    """
    Manages all available coffee drinks.
    Provides methods to display the menu and find a drink by name.

    VERSION 2.0: Added Mocha, Black Coffee, Cold Coffee.
    """

    def __init__(self):
        """
        Constructor — creates all MenuItem objects and stores them.
        """
        self.menu = [
            # Original 3 drinks
            MenuItem(name="espresso",    water=50,  milk=0,   coffee=18, cost=30),
            MenuItem(name="latte",       water=200, milk=150, coffee=24, cost=50),
            MenuItem(name="cappuccino",  water=250, milk=100, coffee=24, cost=60),
            # New 3 drinks added in Version 2.0
            MenuItem(name="mocha",       water=200, milk=50,  coffee=30, cost=70),
            MenuItem(name="black coffee",water=200, milk=0,   coffee=18, cost=25),
            MenuItem(name="cold coffee", water=100, milk=200, coffee=24, cost=65),
        ]

    def get_items(self):
        """
        Returns all drink names as a slash-separated string.
        Example: "espresso/latte/cappuccino/mocha/black coffee/cold coffee"
        """
        return "/".join(item.name for item in self.menu)

    def find_drink(self, order_name):
        """
        Finds a drink on the menu by name (case-insensitive).

        Parameters:
            order_name (str): The name the user typed.

        Returns:
            MenuItem if found, else None.
        """
        cleaned = order_name.lower().strip()
        for item in self.menu:
            if item.name == cleaned:
                return item
        return None

    def show_menu(self):
        """Prints the full menu in a formatted table."""
        print("\n" + "=" * 65)
        print("             ***  COFFEE MACHINE PRO  ***")
        print("=" * 65)
        print(f"  {'#':<3} {'Drink':<15} {'Water':>7} {'Milk':>7} {'Coffee':>8} {'Price':>8}")
        print("-" * 65)
        for i, item in enumerate(self.menu, start=1):
            print(f"  {i:<3} {item.name.capitalize():<15} "
                  f"{item.ingredients['water']:>5}ml "
                  f"{item.ingredients['milk']:>5}ml "
                  f"{item.ingredients['coffee']:>5}g "
                  f"   Rs.{item.cost:.2f}")
        print("=" * 65)
        print("  Commands: report | refill | off")
        print("=" * 65)


# ────────────────────────────────────────────────────────────────
# CLASS 3: CoffeeMaker
# The machine engine — manages resources, refills, makes coffee.
# ────────────────────────────────────────────────────────────────
class CoffeeMaker:
    """
    Handles the coffee machine's internal resources.
    Checks ingredients, refills stock, and prepares drinks.

    VERSION 2.0: Added refill() method.
    """

    # Maximum capacity of the machine
    MAX_WATER  = 1000   # ml
    MAX_MILK   = 800    # ml
    MAX_COFFEE = 500    # g

    def __init__(self):
        """
        Constructor — sets starting resource levels.
        """
        self.resources = {
            "water":  300,
            "milk":   200,
            "coffee": 100,
        }

    def report(self):
        """Prints current resource levels with capacity percentages."""
        water_pct  = int((self.resources["water"]  / self.MAX_WATER)  * 100)
        milk_pct   = int((self.resources["milk"]   / self.MAX_MILK)   * 100)
        coffee_pct = int((self.resources["coffee"] / self.MAX_COFFEE) * 100)

        print("\n" + "-" * 50)
        print("  [MACHINE RESOURCES]")
        print("-" * 50)
        print(f"  Water  : {self.resources['water']:>5} ml   ({water_pct}% full)")
        print(f"  Milk   : {self.resources['milk']:>5} ml   ({milk_pct}% full)")
        print(f"  Coffee : {self.resources['coffee']:>5} g    ({coffee_pct}% full)")

    def is_resource_sufficient(self, drink):
        """
        Checks if the machine has enough ingredients for the drink.

        Parameters:
            drink (MenuItem): The drink to check.

        Returns:
            True if all ingredients are available, False otherwise.
        """
        for ingredient, amount_needed in drink.ingredients.items():
            if amount_needed > self.resources[ingredient]:
                print(f"\n  [!] Sorry! Not enough {ingredient} "
                      f"to make {drink.name.capitalize()}.")
                print(f"      Need {amount_needed} {self._unit(ingredient)}, "
                      f"have {self.resources[ingredient]} {self._unit(ingredient)}.")
                print("      Please refill the machine or choose another drink.")
                input("\n  Press Enter to continue...")
                return False
        return True

    def refill(self):
        """
        Allows admin to refill water, milk, and coffee stock.
        Validates input and caps at maximum capacity.

        VERSION 2.0: New method.
        """
        print("\n" + "-" * 50)
        print("  [REFILL]  Admin Refill Mode")
        print("-" * 50)
        print(f"  Current  -> Water: {self.resources['water']}ml | "
              f"Milk: {self.resources['milk']}ml | "
              f"Coffee: {self.resources['coffee']}g")
        print(f"  Maximum  -> Water: {self.MAX_WATER}ml | "
              f"Milk: {self.MAX_MILK}ml | "
              f"Coffee: {self.MAX_COFFEE}g")
        print("-" * 50)

        for ingredient, unit, maximum in [
            ("water",  "ml", self.MAX_WATER),
            ("milk",   "ml", self.MAX_MILK),
            ("coffee", "g",  self.MAX_COFFEE),
        ]:
            while True:
                try:
                    add = int(input(f"  Add {ingredient} ({unit}): "))
                    if add < 0:
                        print("  [!] Please enter a positive number.")
                    else:
                        new_val = self.resources[ingredient] + add
                        if new_val > maximum:
                            new_val = maximum
                            print(f"  [!] Capped at maximum ({maximum}{unit}).")
                        self.resources[ingredient] = new_val
                        break
                except ValueError:
                    print("  [!] Invalid input. Enter a whole number.")

        print("\n  [OK] Machine refilled successfully!")
        print(f"  New Stock -> Water: {self.resources['water']}ml | "
              f"Milk: {self.resources['milk']}ml | "
              f"Coffee: {self.resources['coffee']}g")
        print("-" * 50)
        input("\n  Press Enter to continue...")

    def make_coffee(self, drink):
        """
        Deducts ingredients and prepares the drink.

        Parameters:
            drink (MenuItem): The drink to prepare.
        """
        self.resources["water"]  -= drink.ingredients["water"]
        self.resources["milk"]   -= drink.ingredients["milk"]
        self.resources["coffee"] -= drink.ingredients["coffee"]

    def _unit(self, ingredient):
        """Returns the measurement unit for a given ingredient."""
        return "g" if ingredient == "coffee" else "ml"


# ────────────────────────────────────────────────────────────────
# CLASS 4: MoneyMachine
# The cash register — handles coins, payment, change, and profit.
# VERSION 2.0: Profit is now saved/loaded from profit.txt
# ────────────────────────────────────────────────────────────────
class MoneyMachine:
    """
    Manages coin input, payment verification, change calculation,
    and persistent profit tracking via profit.txt.
    """

    PROFIT_FILE = "profit.txt"

    # Coin denominations accepted (in rupees)
    COIN_VALUES = {
        "5 rupee":  5,
        "10 rupee": 10,
        "20 rupee": 20,
    }

    def __init__(self):
        """
        Constructor — loads profit from profit.txt if it exists.
        Otherwise starts fresh at Rs.0.
        """
        self.profit = self._load_profit()

    def _load_profit(self):
        """
        Reads saved profit from profit.txt.
        Returns 0.0 if file doesn't exist or is corrupted.
        """
        if os.path.exists(self.PROFIT_FILE):
            try:
                with open(self.PROFIT_FILE, "r") as f:
                    value = float(f.read().strip())
                    print(f"\n  [INFO] Loaded saved profit: Rs.{value:.2f}")
                    return value
            except Exception:
                return 0.0
        return 0.0

    def _save_profit(self):
        """
        Saves current profit to profit.txt so it persists
        between program runs.
        """
        try:
            with open(self.PROFIT_FILE, "w") as f:
                f.write(f"{self.profit:.2f}")
        except Exception as e:
            print(f"  [!] Warning: Could not save profit. ({e})")

    def report(self):
        """Prints total profit collected (loaded + this session)."""
        print(f"  Money  : Rs.{self.profit:.2f}  (Total Collected)")
        print("-" * 50)

    def process_coins(self, drink_name):
        """
        Asks the user to insert coins and calculates total amount.

        Parameters:
            drink_name (str): Name of the drink (shown in prompt).

        Returns:
            float: Total money inserted.
        """
        print(f"\n  [COINS]  Paying for {drink_name.capitalize()}")
        print("  " + "-" * 35)
        total = 0
        for coin, value in self.COIN_VALUES.items():
            while True:
                try:
                    count = int(input(f"  How many {coin} coins? : "))
                    if count < 0:
                        print("  [!] Cannot be negative. Enter 0 or more.")
                    else:
                        total += count * value
                        break
                except ValueError:
                    print("  [!] Invalid input. Please enter a whole number.")
        return total

    def is_transaction_successful(self, money_received, drink_cost):
        """
        Verifies if payment is sufficient, calculates change.

        Parameters:
            money_received (float): Amount inserted by user.
            drink_cost     (float): Price of the drink.

        Returns:
            (bool, float): (success, change_given)
        """
        if money_received >= drink_cost:
            change = round(money_received - drink_cost, 2)
            self.profit += drink_cost
            self._save_profit()    # Save immediately after each sale
            return True, change
        else:
            shortage = round(drink_cost - money_received, 2)
            print(f"\n  [!] Insufficient payment!")
            print(f"      Required : Rs.{drink_cost:.2f}")
            print(f"      Received : Rs.{money_received:.2f}")
            print(f"      Short by : Rs.{shortage:.2f}")
            print("      Refunding your coins. Please try again.")
            input("\n  Press Enter to continue...")
            return False, 0


# ────────────────────────────────────────────────────────────────
# CLASS 5: OrderLogger  (NEW in Version 2.0)
# Logs every order to orders.txt and prints a billing receipt.
# ────────────────────────────────────────────────────────────────
class OrderLogger:
    """
    Handles order tracking and receipt printing.

    - Logs every completed order to orders.txt with timestamp.
    - Prints a detailed billing receipt on screen after each order.

    VERSION 2.0: New class.
    """

    LOG_FILE = "orders.txt"

    def log_order(self, drink, paid, change):
        """
        Appends one order record to orders.txt.

        Parameters:
            drink  (MenuItem): The drink that was ordered.
            paid   (float)   : Total coins inserted.
            change (float)   : Change returned.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = (
            f"[{timestamp}]  |  "
            f"{drink.name.capitalize():<14}  |  "
            f"Cost: Rs.{drink.cost:<7.2f}  |  "
            f"Paid: Rs.{paid:<7.2f}  |  "
            f"Change: Rs.{change:.2f}\n"
        )
        try:
            with open(self.LOG_FILE, "a") as f:
                f.write(log_line)
        except Exception as e:
            print(f"  [!] Warning: Could not log order. ({e})")

    def print_receipt(self, drink, paid, change):
        """
        Prints a formatted billing receipt on screen.

        Parameters:
            drink  (MenuItem): The drink ordered.
            paid   (float)   : Amount paid.
            change (float)   : Change returned.
        """
        timestamp = datetime.now().strftime("%d-%m-%Y  %I:%M %p")
        print("\n" + "=" * 50)
        print("            BILLING RECEIPT")
        print("=" * 50)
        print(f"  Date / Time  : {timestamp}")
        print(f"  Drink        : {drink.name.capitalize()}")
        print(f"  Cost         : Rs.{drink.cost:.2f}")
        print(f"  Amount Paid  : Rs.{paid:.2f}")
        if change > 0:
            print(f"  Change       : Rs.{change:.2f}")
        else:
            print(f"  Change       : No change (Exact payment)")
        print("-" * 50)
        print("  Status       : Payment Successful")
        print("=" * 50)
        print("       Thank you! Enjoy your coffee!")
        print("=" * 50)


# ────────────────────────────────────────────────────────────────
# MAIN PROGRAM
# Connects all classes and runs the coffee machine loop.
# ────────────────────────────────────────────────────────────────
def main():
    """
    Main function — runs the coffee machine.

    Program Flow (Version 2.0):
    1.  Load saved profit from profit.txt
    2.  Show the full drink menu (6 drinks)
    3.  Get user input
    4.  Handle: report | refill | off | drink name
    5.  Check resources
    6.  Process coins
    7.  Verify payment
    8.  Make coffee
    9.  Print billing receipt
    10. Log order to orders.txt
    11. Repeat until 'off'
    """

    # ── Create all objects ───────────────────────────────────
    menu          = Menu()          # The menu board
    coffee_maker  = CoffeeMaker()   # The machine engine
    money_machine = MoneyMachine()  # The cash register
    order_logger  = OrderLogger()   # The order tracker
    # ─────────────────────────────────────────────────────────

    is_on = True

    while is_on:

        # STEP 1: Display the menu
        menu.show_menu()
        options = menu.get_items()

        # STEP 2: Get user's choice with validation
        raw = input(f"\n  Your choice : ").strip()

        # STEP 3: Handle empty input
        if not raw:
            print("\n  [!] No input received. Please type a drink name or command.")
            input("  Press Enter to continue...")
            continue

        choice = raw.lower()

        # STEP 4: Handle special commands
        if choice == "off":
            print("\n" + "=" * 50)
            print("  [OFF] Coffee Machine shutting down.")
            print(f"  Total Earnings Today: Rs.{money_machine.profit:.2f}")
            print("  Goodbye! Have a great day!")
            print("=" * 50 + "\n")
            is_on = False

        elif choice == "report":
            coffee_maker.report()
            money_machine.report()

        elif choice == "refill":
            coffee_maker.refill()

        else:
            # STEP 5: Find the drink
            drink = menu.find_drink(choice)

            if drink is None:
                print(f"\n  [!] '{raw}' is not on the menu.")
                print(f"  Available: {options}")
                input("  Press Enter to continue...")
                continue

            # STEP 6: Check if machine has enough ingredients
            if not coffee_maker.is_resource_sufficient(drink):
                continue

            # STEP 7: Process coins
            paid = money_machine.process_coins(drink.name)

            # STEP 8: Verify payment
            success, change = money_machine.is_transaction_successful(paid, drink.cost)

            if success:
                # STEP 9: Make the coffee
                coffee_maker.make_coffee(drink)

                # STEP 10: Print receipt
                order_logger.print_receipt(drink, paid, change)

                # STEP 11: Log the order
                order_logger.log_order(drink, paid, change)

                input("\n  Press Enter to continue...")


# ────────────────────────────────────────────────────────────────
# Entry Point
# ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()


# ================================================================
# FILE GUIDE (New in Version 2.0):
# ================================================================
#
#  coffee_machine_project.py  -- Main program (all classes here)
#  profit.txt                 -- Auto-created: saves total profit
#  orders.txt                 -- Auto-created: logs every order
#
# ================================================================
# SAMPLE orders.txt content:
# ================================================================
#
#  [2026-05-06 15:30:00]  |  Latte           |  Cost: Rs.50.00   |  Paid: Rs.60.00   |  Change: Rs.10.00
#  [2026-05-06 15:35:22]  |  Espresso        |  Cost: Rs.30.00   |  Paid: Rs.30.00   |  Change: Rs.0.00
#  [2026-05-06 15:40:10]  |  Mocha           |  Cost: Rs.70.00   |  Paid: Rs.80.00   |  Change: Rs.10.00
#
# ================================================================
# SAMPLE profit.txt content:
# ================================================================
#
#  150.00
#
# ================================================================
