# Billing.py

def calculate_total(orders):
    total = 0

    for order in orders:
        total += order["price"] * order["quantity"]

    return total

def calculate_discount(total):
    if total > 1000000:
        discount = total * 0.10
    else:
        discount = 0

    return discount

def print_invoice(orders):
    if not orders:
        print("There are no orders to print an invoice.")
        return

    print("\n========== Invoice ==========")

    for order in orders:
        product = order["product"]
        quantity = order["quantity"]
        price = order["price"]

        print(f"Product: {product}")
        print(f"Quantity: {quantity}")
        print(f"Amount: {price * quantity:,} Toman")
        print("-----------------------------")

    total = calculate_total(orders)
    discount = calculate_discount(total)
    final_amount = total - discount

    print(f"Total: {total:,.0f} Toman")
    print(f"Discount: {discount:,.0f} Toman")
    print(f"Final Amount: {final_amount:,.0f} Toman")

    print("=============================")