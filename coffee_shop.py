import logging
import sys

#Creating my coffee shop logger
coffee_shop = logging.getLogger(__name__)
coffee_shop.setLevel(logging.INFO)


#Creating the File Handler
coffee_shop_handler = logging.FileHandler("coffee.log")

#Creating a Formatter
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

#Add the formatter to the handler 
coffee_shop_handler.setFormatter(formatter)

#Add the handler to the logger
coffee_shop.addHandler(coffee_shop_handler)

#Mera Coffee Menu
print("The Coffee Shop Menu is: ")
coffee_menu = {
    "A": {"name": "Espresso", "price": 2.00},
    "B": {"name": "Latte", "price": 3.50},
    "C": {"name": "Cappuccino", "price": 3.00},
    "D": {"name": "Mocha", "price": 3.75},
    "E": {"name": "Iced Coffee", "price": 2.50},
    "F": {"name": "Hot Chocolate", "price": 2.75},
    "X": {"name": "End Order", "price": 0.00}
}

def show_menu():
    for item in coffee_menu:
        print(f"{item}, {coffee_menu[item]}")
    titles = ", ".join([value["name"] for value in coffee_menu.values()])
    coffee_shop.info(f"The Items available in menu are: {titles}")

show_menu()

choice = input("What would you like to purchase? Please choose any option from the above. ")
if choice in coffee_menu:
    info = coffee_menu[choice]
    coffee_shop.info(f"The chosen item is: {info['name']}")

    quantity = int(input(f"Please enter the quantity of {info['name']}: "))
    final_quantity = quantity * info["price"]
    coffee_shop.info(f"The final price for {quantity} {info['name']} is {final_quantity}")
    coffee_shop.info("Closing the session")

elif any(choice.upper() == item["name"].upper() for item in coffee_menu.values()):
    for code, info in coffee_menu.items():
        if info["name"].upper() == choice.upper():
            coffee_shop.info(f"The chosen item is: {info['name']}")
            
            quantity = int(input(f"Please enter the quantity of {info['name']}: "))
            final_quantity = quantity * info["price"]
            coffee_shop.info(f"The final price for {quantity} {info['name']} is {final_quantity}")
            coffee_shop.info("Closing the session")
            
            break
else:
    coffee_shop.error(f"The chosen item '{choice}' does not exist in the menu.")




