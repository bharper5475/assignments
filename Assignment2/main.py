import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    while True:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

        if choice == "off":
            break
        elif choice == "report":
            print(f"Bread: {resources['bread']} slice(s)")
            print(f"Ham: {resources['ham']} slice(s)")
            print(f"Cheese: {resources['cheese']} pound(s)")
        elif choice in recipes:
            sandwich = recipes[choice]
            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                coins = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins, sandwich["cost"]):
                    sandwich_maker_instance.make_sandwich(choice, sandwich["ingredients"])
        else:
            print("Invalid input.")

if __name__=="__main__":
    main()
