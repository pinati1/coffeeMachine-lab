from assets.coffee_machine_cons import MENU, resources
from src.menu import Menu
from src.money_handler import MoneyHandler
from src.coffee_machine import CoffeeMachine

CoffeeMachine(resources, Menu(MENU), MoneyHandler()).run()
