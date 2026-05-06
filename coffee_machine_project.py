# -*- coding: utf-8 -*-
# ============================================================
#         ***  COFFEE MACHINE PROJECT  ***
#         Built using Object-Oriented Programming (OOP)
#         Language: Python 3
# ============================================================
#
# HOW CLASSES INTERACT:
# +-----------+   asks for drink   +-----------+
# |   Menu    | -----------------> | MenuItem  |
# +-----------+                    +-----------+
#       |                                |
#       |  selected drink               | ingredients/cost
#       v                                v
# +-----------+  checks resources  +--------------+
# |CoffeeMaker| <------------------| MoneyMachine |
# +-----------+                    +--------------+
#       |                                |
#       | makes coffee                  | processes payment
#       v                                v
#     USER  <---------- serves -------- USER
#
# ============================================================


# ─────────────────────────────────────────────────────────────
# CLASS 1: MenuItem
# Represents a single drink item on the menu.
# Think of it as a "recipe card" for each coffee.
# ─────────────────────────────────────────────────────────────
class MenuItem:
    """
    Stores information about one coffee drink.
    Each drink has a name, ingredients needed, and price.
    """

    def __init__(self, name, water, milk, coffee, cost):
        """
        Constructor -- runs automatically when we create a MenuItem object.

        Parameters:
            name   (str)   : Name of the drink (e.g., "espresso")
            water  (int)   : Water needed in ml
            milk   (int)   : Milk needed in ml
            coffee (int)   : Coffee beans needed in grams
            cost   (float) : Price of the drink in rupees
        """
        self.name = name                      # Drink name
        self.ingredients = {                  # Dictionary of ingredients
            "water":  water,
            "milk":   milk,
            "coffee": coffee
        }
        self.cost = cost                      # Price in rupees

    def __str__(self):
        """Returns a readable string when we print a MenuItem object."""
        return (f"{self.name.capitalize()} | "
                f"Water: {self.ingredients['water']}ml | "
                f"Milk: {self.ingredients['milk']}ml | "
                f"Coffee: {self.ingredients['coffee']}g | "
                f"Cost: Rs.{self.cost:.2f}")


# ─────────────────────────────────────────────────────────────
# CLASS 2: Menu
# Stores all available drinks and helps find a drink by name.
# Think of it as the "menu board" at a coffee shop.
# ─────────────────────────────────────────────────────────────
class Menu:
    """
    Manages the list of all available coffee drinks.
    Provides methods to display the menu and find a drink.
    """

    def __init__(self):
        """
        Constructor -- creates MenuItem objects for each drink
        and stores them in a list.
        """
        # Creating drink objects using the MenuItem class
        self.menu = [
            MenuItem(name="espresso",   water=50,  milk=0,   coffee=18, cost=30),
            MenuItem(name="latte",      water=200, milk=150, coffee=24, cost=50),
            MenuItem(name="cappuccino", water=250, milk=100, coffee=24, cost=60),
        ]

    def get_items(self):
        """
        Returns a string of all drink names, separated by slashes.
        Example: "espresso/latte/cappuccino"
        """
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options.rstrip("/")   # Remove trailing slash

    def find_drink(self, order_name):
        """
        Searches the menu for the drink the user ordered.

        Parameters:
            order_name (str): The name of the drink the user typed.

        Returns:
            MenuItem object if found, else None.
        """
        for item in self.menu:
            if item.name == order_name.lower().strip():
                return item
        print(f"\n  [!] '{order_name}' is not on the menu. Please try again.\n")
        return None

    def show_menu(self):
        """Prints a nicely formatted menu to the screen."""
        print("\n" + "=" * 55)
        print("         ***  WELCOME TO COFFEE MACHINE  ***")
        print("=" * 55)
        print(f"  {'Drink':<15} {'Water':>8} {'Milk':>8} {'Coffee':>8} {'Price':>8}")
        print("-" * 55)
        for item in self.menu:
            print(f"  {item.name.capitalize():<15} "
                  f"{item.ingredients['water']:>5}ml "
                  f"{item.ingredients['milk']:>6}ml "
                  f"{item.ingredients['coffee']:>5}g "
                  f"  Rs.{item.cost:.2f}")
        print("=" * 55)


# ─────────────────────────────────────────────────────────────
# CLASS 3: CoffeeMaker
# Manages the machine's resources (water, milk, coffee).
# Think of it as the "engine" of the coffee machine.
# ─────────────────────────────────────────────────────────────
class CoffeeMaker:
    """
    Handles the internal resources of the coffee machine.
    Checks if there are enough ingredients and makes the coffee.
    """

    def __init__(self):
        """
        Constructor -- sets the starting amount of resources
        available in the machine.
        """
        self.resources = {
            "water":  300,    # 300 ml of water
            "milk":   200,    # 200 ml of milk
            "coffee": 100,    # 100 grams of coffee beans
        }

    def report(self):
        """Prints the current resource levels in the machine."""
        print("\n" + "-" * 40)
        print("  [REPORT]  MACHINE RESOURCES")
        print("-" * 40)
        print(f"  Water  : {self.resources['water']} ml")
        print(f"  Milk   : {self.resources['milk']} ml")
        print(f"  Coffee : {self.resources['coffee']} g")

    def is_resource_sufficient(self, drink):
        """
        Checks if the machine has enough ingredients for the chosen drink.

        Parameters:
            drink (MenuItem): The drink the user wants to make.

        Returns:
            True  -- if all resources are available.
            False -- if any resource is insufficient.
        """
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"\n  [!] Sorry! Not enough {item} to make {drink.name}.")
                print("      Please refill the machine or choose another drink.")
                input("\n  Press Enter to continue...")
                return False
        return True

    def make_coffee(self, drink):
        """
        Deducts the required ingredients from the machine's resources
        and serves the coffee.

        Parameters:
            drink (MenuItem): The drink to be prepared.
        """
        self.resources["water"]  -= drink.ingredients["water"]
        self.resources["milk"]   -= drink.ingredients["milk"]
        self.resources["coffee"] -= drink.ingredients["coffee"]
        print(f"\n  [**] Here is your {drink.name.capitalize()}! Enjoy! :)\n")


# ─────────────────────────────────────────────────────────────
# CLASS 4: MoneyMachine
# Handles all payment-related tasks.
# Think of it as the "cash register" of the coffee machine.
# ─────────────────────────────────────────────────────────────
class MoneyMachine:
    """
    Processes coin insertion, verifies payment,
    calculates change, and tracks total profit.
    """

    # Coin values accepted by the machine (in rupees)
    COIN_VALUES = {
        "5 rupee":  5,
        "10 rupee": 10,
        "20 rupee": 20,
    }

    def __init__(self):
        """
        Constructor -- sets the initial profit to zero.
        """
        self.profit = 0    # Total money earned by the machine

    def report(self):
        """Prints the total money (profit) collected so far."""
        print(f"  Money  : Rs.{self.profit:.2f}  (Total Collected)")
        print("-" * 40)   # Close the report box properly

    def process_coins(self):
        """
        Asks the user how many of each coin they are inserting.
        Calculates the total amount inserted.

        Returns:
            float: Total amount of money inserted by the user.
        """
        print("\n  [COINS]  INSERT YOUR COINS")
        print("  " + "-" * 30)
        total = 0
        for coin, value in self.COIN_VALUES.items():
            while True:
                try:
                    count = int(input(f"  How many {coin} coins? : "))
                    if count < 0:
                        print("  [!] Please enter 0 or a positive number.")
                    else:
                        total += count * value
                        break
                except ValueError:
                    print("  [!] Invalid input! Please enter a whole number.")
        return total

    def is_transaction_successful(self, money_received, drink_cost):
        """
        Checks if the user paid enough for the drink.
        Gives back change if they overpaid.

        Parameters:
            money_received (float): Total coins inserted.
            drink_cost     (float): Price of the selected drink.

        Returns:
            True  -- if payment is sufficient.
            False -- if payment is insufficient.
        """
        if money_received >= drink_cost:
            change = round(money_received - drink_cost, 2)
            if change > 0:
                print(f"\n  [OK] Payment accepted! Your change is Rs.{change:.2f}")
            else:
                print(f"\n  [OK] Payment accepted! Exact amount received.")
            self.profit += drink_cost   # Add drink cost to machine profit
            return True
        else:
            shortage = round(drink_cost - money_received, 2)
            print(f"\n  [!] Not enough money! You need Rs.{shortage:.2f} more.")
            print("      Refunding your money. Please try again.")
            input("\n  Press Enter to continue...")  # Pause so user can read the message
            return False


# ─────────────────────────────────────────────────────────────
# MAIN PROGRAM
# This is where all classes come together and the machine runs.
# ─────────────────────────────────────────────────────────────
def main():
    """
    Main function that runs the coffee machine loop.

    Program Flow:
    1.  Show the menu
    2.  Get user's drink choice
    3.  Handle special commands (report / off)
    4.  Check if ingredients are available
    5.  Process coins / payment
    6.  Verify payment
    7.  Make and serve coffee
    8.  Repeat until user types 'off'
    """

    # ── Create objects from our classes ──────────────────────
    menu          = Menu()           # The drinks menu
    coffee_maker  = CoffeeMaker()    # The machine that makes coffee
    money_machine = MoneyMachine()   # The payment system
    # ─────────────────────────────────────────────────────────

    is_on = True   # Controls the machine on/off state

    while is_on:

        # STEP 1: Show menu and get user's choice
        menu.show_menu()
        options = menu.get_items()
        choice = input(f"\n  What would you like? ({options}) : ").lower().strip()

        # STEP 2: Handle special commands
        if choice == "off":
            # Turn off the machine
            print("\n  [OFF] Turning off the coffee machine. Goodbye!\n")
            is_on = False

        elif choice == "report":
            # Show resource and money report (both inside the same box)
            coffee_maker.report()
            money_machine.report()
            # Note: money_machine.report() closes the box with the bottom dashes

        else:
            # STEP 3: Find the drink on the menu
            drink = menu.find_drink(choice)

            if drink is not None:
                # STEP 4: Check if machine has enough ingredients
                if coffee_maker.is_resource_sufficient(drink):
                    # STEP 5: Process coins from the user
                    payment = money_machine.process_coins()

                    # STEP 6: Verify if payment is enough
                    if money_machine.is_transaction_successful(payment, drink.cost):
                        # STEP 7: Make and serve the coffee
                        coffee_maker.make_coffee(drink)


# ─────────────────────────────────────────────────────────────
# Entry Point -- Python runs this block first
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()


# ============================================================
# SAMPLE OUTPUT:
# ============================================================
#
#  =======================================================
#           ***  WELCOME TO COFFEE MACHINE  ***
#  =======================================================
#    Drink            Water     Milk   Coffee    Price
#  -------------------------------------------------------
#    Espresso          50ml      0ml    18g    Rs.30.00
#    Latte            200ml    150ml   24g    Rs.50.00
#    Cappuccino       250ml    100ml   24g    Rs.60.00
#  =======================================================
#
#  What would you like? (espresso/latte/cappuccino) : latte
#
#  [COINS]  INSERT YOUR COINS
#  ------------------------------
#  How many 5 rupee coins?  : 0
#  How many 10 rupee coins? : 5
#  How many 20 rupee coins? : 0
#
#  [OK] Payment accepted! Exact amount received.
#
#  [**] Here is your Latte! Enjoy! :)
#
#  What would you like? (espresso/latte/cappuccino) : report
#
#  ----------------------------------------
#   [REPORT]  MACHINE RESOURCES
#  ----------------------------------------
#   Water  : 100 ml
#   Milk   : 50 ml
#   Coffee : 76 g
#  ----------------------------------------
#   Money  : Rs.50.00  (Total Collected)
#
#  What would you like? (espresso/latte/cappuccino) : off
#  [OFF] Turning off the coffee machine. Goodbye!
#
# ============================================================
