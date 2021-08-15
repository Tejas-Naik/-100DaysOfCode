MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_sufficient(order_ingredients):
    """Returns true when order can be made and false when there's isn't sufficient resource"""
    for item in order_ingredients:
        if resources[item] <= order_ingredients[item]:
            print(f"sorry, there's not enough {item}")
            return False
    return True


def process_coins():
    """Returns total calculation of coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters you have?")) * 0.25
    total += int(input("How many dimes you have?")) * 0.1
    total += int(input("How many nickles you have?")) * 0.05
    total += int(input("How many pennies you have?")) * 0.01
    return total


def is_transaction_successful(coffee_price, money_recieved):
    """Return true when payment is accepted and false when not enough money entered"""
    if money_recieved > coffee_price:
        change = round(money_recieved - coffee_price, 2)
        print(f"Here's ${change} your change.")
        global profit
        profit += coffee_price
        return True

    else:
        print("There's not enough money, Money Refunded!")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required igredients from the available resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your ☕ {drink_name}, Have a Good Day!")


is_on = True
while is_on:
    choice = input("Please select youe coffee (espresso/lette/cappuccino):")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gm")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        print(drink)
        if is_sufficient(drink['ingredients']):
            money_entered = process_coins()
            if is_transaction_successful(drink['cost'], money_entered):
                make_coffee(choice, drink['ingredients'])