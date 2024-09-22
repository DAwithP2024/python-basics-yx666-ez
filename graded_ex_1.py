# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_sorted_products(products_list, sort_order):
    if sort_order == "asc":
        return sorted(products_list, key=lambda x: x[1])
    elif sort_order == "desc":
        return sorted(products_list, key=lambda x: x[1], reverse=True)


def display_products(products_list):
    for index, (name, price) in enumerate(products_list, start=1):
        print(f"{index}. {name} - ${price}")


def display_categories():
    for index, category in enumerate(products.keys(), start=1):
        print(f"{index}. {category}")
    try:
        choice = int(input("Select a product category : ")) - 1
        if choice not in range(len(products)):
            print("Invalid. Please try again.")
            return None
        return choice
    except ValueError:
        print("Invalid. Please enter a number.")
        return None


def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))


def display_cart(cart):
    total_cost = 0
    for name, price, quantity in cart:
        cost = price * quantity
        total_cost += cost
        print(f"{name} - ${price} x {quantity} = ${cost}")
    print(f"Total cost: ${total_cost}")


def generate_receipt(name, email, cart, total_cost, address):
    print(f"Customer: {name}")
    print(f"Email: {email}")
    print("Goods have been Purchased:")
    for name, price, quantity in cart:
        cost = price * quantity
        print(f"{quantity} x {name} - ${price} = ${cost}")
    print(f"Total cost: ${total_cost}")
    print(f"Deliver address: {address}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")


def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)


def validate_email(email):
    return "@" in email


def main():
    cart = []
    name = input("Please enter your name: ")
    while not validate_name(name):
        print("Invalid. Please enter a valid name which must have the first name and last name.")
        name = input("Please enter your name: ")

    email = input("Please enter your email address which must have '@': ")
    while not validate_email(email):
        print("Invalid. Please enter a valid email address.")
        email = input("Please enter your email address: ")

    while True:
        category_index = display_categories()
        if category_index is None:
            continue

        category_name = list(products.keys())[category_index]
        products_list = products[category_name]
        display_products(products_list)

        while True:
            print("\nOptions:")
            print("1. Select a product to buy")
            print("2. Sort the products according to the price")
            print("3. Go back to the category selection")
            print("4. Finish shopping")
            choice = input("Select your option: ")

            if choice == "1":
                try:
                    product_choice = int(input("Please enter the product number: ")) - 1
                    if product_choice not in range(len(products_list)):
                        print("Invalid product selection.")
                        continue
                    quantity = int(input("Please enter the product quantity: "))
                    if quantity <= 0:
                        print("Quantity cannot be zero.")
                        continue
                    add_to_cart(cart, products_list[product_choice], quantity)
                except ValueError:
                    print("Invalid. Please enter valid numbers.")
            elif choice == "2":
                sort_order = input("Sort ascending (1) or descending (2): ")
                sorted_list = display_sorted_products(products_list, "asc" if sort_order == "1" else "desc")
                display_products(sorted_list)
            elif choice == "3":
                break
            elif choice == "4":
                if cart:
                    display_cart(cart)
                    total_cost = sum(price * quantity for _, price, quantity in cart)
                    address = input("Please enter delivery address: ")
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day!")
                return
            else:
                print("Invalid. Please try again.")

""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()
