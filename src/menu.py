class MenuItem:
    """Represents a single drink option with its cost and required ingredients."""

    def __init__(self, name: str, cost: float, ingredients: dict):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients


class Menu:
    """Builds and exposes the drink catalogue from raw menu data."""

    def __init__(self, menu_data: dict):
        self.items: dict[str, MenuItem] = {
            name: MenuItem(name, data["cost"], data["ingredients"])
            for name, data in menu_data.items()
        }

    def get_drink(self, name: str) -> MenuItem | None:
        """Return the MenuItem for the given name, or None if not found."""
        return self.items.get(name)

    def display_menu(self) -> None:
        """Print all available drinks with their prices."""
        print("\nMenu:")
        for drink in self.items.values():
            print(f"  {drink.name.capitalize()}: ${drink.cost:.2f}")
        print()
