from src.menu import Menu, MenuItem
from src.money_handler import MoneyHandler


class CoffeeMachine:
    """Manages machine resources, profit, and the main serving loop."""

    def __init__(self, resources: dict, menu: Menu, handler: MoneyHandler):
        self.resources = dict(resources)
        self.money = 0.0
        self.menu = menu
        self.handler = handler

    def report(self) -> None:
        """Print the current resource levels and total profit."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.money}")

    def check_resources(self, drink: MenuItem) -> bool:
        """Return True if the machine has enough ingredients for the drink."""
        for ingredient, amount in drink.ingredients.items():
            if self.resources.get(ingredient, 0) < amount:
                print(f"Sorry there is not enough {ingredient}.")
                return False
        return True

    def make_coffee(self, drink: MenuItem) -> None:
        """Deduct ingredients, record profit, and serve the drink."""
        for ingredient, amount in drink.ingredients.items():
            self.resources[ingredient] -= amount
        self.money += drink.cost
        print(f"Here is your {drink.name}. Enjoy!")

    def run(self) -> None:
        """Main serving loop — runs until the user types 'off'."""
        self.menu.display_menu()
        while True:
            choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()

            if choice == "off":
                break
            elif choice == "report":
                self.report()
            elif choice in self.menu.items:
                drink = self.menu.get_drink(choice)
                if self.check_resources(drink):
                    total = self.handler.process_coins()
                    if self.handler.check_transaction(total, drink.cost):
                        self.make_coffee(drink)
            else:
                print(f"'{choice}' is not a valid option.")
