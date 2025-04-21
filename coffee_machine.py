MENU = {
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost": 75, 
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost": 125,
    },
    "cappucino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost": 185,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


profit = 0

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry! Not enough {item}.")
            return False
    return True

def insert_coin():
    '''returns the total from the coins inserted'''
    print("Please insert coins.")
    fiverupee = int(input("How many five rupee coins?: "))*5
    tenrupee = int(input("How many ten rupee coins?: "))*10
    twentyrupee = int(input("How many twenty rupee coins?: "))*20
    total = fiverupee + tenrupee + twentyrupee
    return total

def is_transaction_successful(money_received, drink_cost):
    '''checks if the payment transaction is successfull'''
    if money_received >= drink_cost:
        global profit
        change = round(money_received - drink_cost, 2)
        print(f"Here is ₹{change} in change")
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕ ")
    


is_on = True

while is_on: 
    order = input("What would you like to have ? (espresso/latte/cappucino): ")
    if order == "off":
        is_on = False
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ₹{profit}")
    else:
        drink = MENU[order]
        if check_resources(drink["ingredients"]):
            payment = insert_coin()
            is_transaction_successful(payment, drink["cost"])
            make_coffee(order, drink["ingredients"])





    




