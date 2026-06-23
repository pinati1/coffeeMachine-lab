class MenuItem:
    def __init__(self, name: str, cost: float, ingredients: dict):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients


class Menu:
    def __init__(self, menu_data: dict):
        self.items: dict[str, MenuItem] = {
            name: MenuItem(name, data["cost"], data["ingredients"])
            for name, data in menu_data.items()
        }

    def get_drink(self, name: str) -> MenuItem | None:
        return self.items.get(name)
