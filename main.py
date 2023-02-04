from data import MENU , resources

on=True
vault=0

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"Sorry, there is not enough {item}\nPlease try to type other coffees or type 'off' to close the machine.")
            return False
    return True

def process_coins():
    print(f"{choice.title()} costs ${MENU[choice]['cost']}\nPlease insert coins.")
    total=int(input("How many quarters?"))*0.25
    total+=int(input("How many dimes?"))*0.10
    total+=int(input("How many nickles?"))*0.05
    total+=int(input("How many pennies?"))*0.01
    return total

def transaction(money_received,drink_cost):
    if money_received>=drink_cost:
        change=round(money_received-drink_cost,2)
        if change>0:
            print(f"Here is ${change} change.")
        global vault
        vault+=drink_cost
        return True
    else:
        print(f"Sorry that's not enough money.You You should put ${drink_cost-money_received} more coins. ")

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here your {drink_name}.")


while on is True:
    choice=input("What would you like (espresso,latte,cappuccino)")
    if choice=="off":
        on=False
    elif choice == "report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: ${vault}")
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment=process_coins()
            if transaction(payment,drink['cost']):
                make_coffee(choice,drink["ingredients"])
