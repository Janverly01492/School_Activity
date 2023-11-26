inventory = {
    'Apple': {'price': 35.50, 'quantity': 150},
    'Banana': {'price': 75.50, 'quantity': 100},
    'Orange': {'price': 200.75, 'quantity': 100},
    'Guava': {'price': 150.25, 'quantity': 100}
}

total_purchased_value = 0 

def add_product(name, price, quantity):
    if name in inventory:
        inventory[name]['quantity'] += quantity
    else:
        inventory[name] = {'price': price, 'quantity': quantity}

def remove_product(name):
    if name in inventory:
        del inventory[name]
    else:
        print("Product not found in inventory.")

def display_inventory():
    print("Inventory:")
    for product, details in inventory.items():
        print(f"{product.title()}: Price - P{details['price']}, Quantity - {details['quantity']}")

def generate_receipt(cart):
    total_cost = 0
    print("----- Grocery Store Receipt -----")
    print("Product          Quantity    \tPrice")

    for product, quantity in cart.items():
        if product in inventory:
            if inventory[product]['quantity'] >= quantity:
                price = inventory[product]['price']
                cost = price * quantity
                total_cost += cost
                print(f"{product:15}{quantity:10}\t P{cost:.2f}")
                inventory[product]['quantity'] -= quantity  # Update inventory quantity
            else:
                print(f"Insufficient quantity in inventory for {product}. Cannot generate the receipt.")
                return
        else:
            print(f"Invalid product {product} in the cart. Cannot generate the receipt.")
            return

    print(f"\nTotal cost: P{total_cost:.2f}")

def buy_product(name, quantity):
    global total_purchased_value  
    if name in inventory:
        if inventory[name]['quantity'] >= quantity:
            inventory[name]['quantity'] -= quantity
            total_cost = inventory[name]['price'] * quantity
            total_purchased_value += total_cost  
            print(f"You have purchased {quantity} {name.title()}(s) for P{total_cost}.")
        else:
            print(f"Insufficient quantity in inventory for {name.title()}. Cannot complete the purchase.")
    else:
        print("Product not found in inventory.")

cart = {}  # Initialize the cart outside the loop
buying_enabled = True  # Flag to enable or disable buying

while True:
    print("\nOptions:")
    print("1. Add a product")
    print("2. Remove a product")
    print("3. Display inventory")
    print("4. Receipt")
    print("5. Buy a product")
    print("6. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        add_product(name, price, quantity)
        print(f"{name.title()} added to inventory.")
    elif choice == '2':
        name = input("Enter product name to remove: ")
        remove_product(name)
    elif choice == '3':
        display_inventory()
    elif choice == '4':
        if cart:
            generate_receipt(cart)
        else:
            print("No items in the cart.")
    elif choice == '5':
        if buying_enabled and any(product['quantity'] > 0 for product in inventory.values()):
            available_products = [product for product, details in inventory.items() if details['quantity'] > 0]
            if available_products:
                print("Available products:")
                for product in available_products:
                    print(product.title())

                while True:
                    name = input("Enter product name to buy (or 'done' to finish): ")
                    name = name.title()

                    if name.lower() == 'done':
                        break

                    if name in inventory and inventory[name]['quantity'] > 0:
                        quantity = int(input(f"Enter the quantity to buy for {name}: "))

                        if name in cart:
                            cart[name] += quantity
                        else:
                            cart[name] = quantity
                    elif name in inventory and inventory[name]['quantity'] == 0:
                        print(f"Sorry, {name.title()} is out of stock.")
                    else:
                        print("Product not found in inventory.")
            else:
                print("Inventory is empty. Cannot buy any products.")
        else:
            print("Buying is currently disabled. Inventory is out of stock.")
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please enter a valid option.")
