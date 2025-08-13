from db import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
	"money": 0,
}
machine_is_on = True
enough_ingredients = True
enough_money = True

def turn_off():
	global machine_is_on
	machine_is_on = False

def check_money(beverage, cost):
	global enough_money
	if cost >= int(MENU[beverage]["cost"]):
		change = cost - MENU[beverage]['cost']
		print(f"Here's your change: {round(change, 2)}")
		print(f"Here's your {beverage} ☕️ Enjoy!")
		resources["money"] += MENU[beverage]["cost"]
	else:
		print("Sorry, that's not enough money. Money refunded.")
		enough_money = False
		return(enough_money)

def insert_coins(drink):
	print("Please insert coins")
	quarter = int(input("How many quarters: "))
	dime = int(input("How many dimes: "))	
	nickel = int(input("How many nickels: "))
	penny = int(input("How many pennies: "))
	money_user = (quarter * 0.25) + (dime * 0.1) + (nickel * 0.05) + (penny * 0.01)
	check_money(drink, money_user)
	return(enough_money)

	
def check_ingredients(drink):
	global enough_ingredients
	if resources["water"] < MENU[drink]["ingredients"]["water"]:
		print("Sorry, there is not enough water")
		enough_ingredients = False
	if resources["milk"] < MENU[drink]["ingredients"]["milk"]:
		print("Sorry, there is not enough milk")
		enough_ingredients = False
	if resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
		print("Sorry, there is not enough coffee")
		enough_ingredients = False
	return (enough_ingredients)

def update_resources(drink):
	resources["water"] -= MENU[drink]["ingredients"]["water"]
	resources["milk"] -= MENU[drink]["ingredients"]["milk"]
	resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]

while machine_is_on:
	user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

	if user_input == "report":
		print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")

	if user_input in ["espresso", "latte", "cappuccino"]:
		check_ingredients(user_input)
		if enough_ingredients:
			insert_coins(user_input)
			if enough_money:
				update_resources(user_input)

	enough_money = True

	if user_input == "off":
		turn_off()
