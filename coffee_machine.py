MENU = {
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost": 1.5, 
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.5,
    },
    "cappucino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

order = input("What would you like to have ? (espresso/latte/cappucino): ")

def check_resources():
    if resources["water"]<0 or resources["coffee"]<0 or resources["milk"]<0:
        print("Sorry! Not enough resources")
    
def insert_coin():
    print("Please insert coins.")
    fiverupee = int(input("How many five rupee coins?: "))
    tenrupee = int(input("How many ten rupee coins?: "))
    twentyrupee = int(input("How many twenty rupee coins?: "))
    inserted_coins = fiverupee + tenrupee + twentyrupee
    if inserted_coins > MENU["cappucino"]["cost"] or MENU["latte"]["cost"] or MENU["espresso"]["cost"]:
        change = inserted_coins - MENU["cappucino"]["cost"]
    


def order_coffee():
    if order == "espresso":
        insert_coin()