# Order.py

from Menu import menu

orders = []

def add_order():
    product = input("Enter product name: ").strip().lower()

    if product not in menu:
        print("This product is not available in the menu!")
        return

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero!")
            return

    except ValueError:
        print("Please enter a valid number!")
        return

    order = {
        "product": product,
        "price": menu[product],
        "quantity": quantity
    }

    orders.append(order)

    print("Order successfully added!")

def show_orders():
    if not orders:
        print("There are no orders yet.")
        return

    print("\n========== Orders ==========")

    for order in orders:
        print(f"Product: {order['product']}")
        print(f"Price: {order['price']:,} Toman")
        print(f"Quantity: {order['quantity']}")
        print("----------------------------")