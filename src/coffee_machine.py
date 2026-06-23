from src.menu import Menu, MenuItem
from src.money_handler import MoneyHandler


class CoffeeMachine:
    def __init__(self, resources: dict, menu: Menu, handler: MoneyHandler):
        self.resources = dict(resources)
        self.money = 0.0
        self.menu = menu
        self.handler = handler

    def report(self) -> None:
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.money}")

    def check_resources(self, drink: MenuItem) -> bool:
        for ingredient, amount in drink.ingredients.items():
            if self.resources.get(ingredient, 0) < amount:
                print(f"Sorry there is not enough {ingredient}.")
                return False
        return True

    def make_coffee(self, drink: MenuItem) -> None:
        for ingredient, amount in drink.ingredients.items():
            self.resources[ingredient] -= amount
        # profit is the drink price, not the amount inserted — change is excluded
        self.money += drink.cost
        print(f"Here is your {drink.name}. Enjoy!")

    def run(self) -> None:
        prompt = "What would you like? (espresso/latte/cappuccino): "
        while True:
            choice = input(prompt).strip().lower()

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
