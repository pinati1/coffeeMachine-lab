from src.coin import Coin


class MoneyHandler:
    def __init__(self):
        self.coins: list[Coin] = [
            Coin("quarters", 0.25),
            Coin("dimes", 0.10),
            Coin("nickels", 0.05),
            Coin("pennies", 0.01),
        ]

    def process_coins(self) -> float:
        print("Please insert coins.")
        total = 0.0
        for coin in self.coins:
            while True:
                raw = input(f"How many {coin.name}? ")
                if raw.isdigit():
                    total += int(raw) * coin.value
                    break
                print("Please enter a whole number.")
        return round(total, 2)

    def check_transaction(self, total: float, cost: float) -> bool:
        if total < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
        change = round(total - cost, 2)
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
        return True
