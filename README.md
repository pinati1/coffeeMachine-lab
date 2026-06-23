# Coffee Machine Lab

Ori Cohen, ID 211481791

A command-line coffee machine. It takes an order, checks if there are enough
ingredients, takes coins, and makes the drink (or refunds you if you didn't
pay enough).

## How to run

```
python main.py
```

Needs Python 3.10+ (uses the `X | None` type hint syntax). No external
packages required.

## Project layout

- `main.py` - entry point, runs the machine
- `src/coffee_machine.py` - main loop, resource checks, makes the coffee
- `src/money_handler.py` - coin input and payment validation
- `src/menu.py` - drink definitions (cost + ingredients)
- `src/coin.py` - a single coin class
- `assets/coffee_machine_cons.py` - menu data and starting resource amounts

## Commands

- Type a drink name (`espresso`, `latte`, `cappuccino`) to order it
- `report` - shows current water, milk, coffee and money
- `off` - shuts the machine down

## Test scenarios

**1. Paying more than needed**

Ordered an `espresso` cost  ($1.50)   put in the machine (1.75) . The machine

gave back $0.25 in change and printed "Here is your espresso. Enjoy!".

**2. Report after an order**
Typed `report` right after the espresso above. Shows the resources used
going down (water 250ml, coffee 82g, milk unchanged at 200ml) and the
till at $1.5, matching the price of the espresso that was made.

**3. Not paying enough**
Ordered a `latte` ($2.50) but only inserted 1 quarter ($0.25). The machine
printed "Sorry that's not enough money. Money refunded." and didn't touch
the resources.

A full terminal output of these three runs is in `demo.txt`.
