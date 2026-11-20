# Menu.py

menu = {
    "coffee": 80000,
    "tea": 50000,
    "cake": 120000
}

def show_menu():
    print("\n========== Coffee Menu ==========")

    for product, price in menu.items():
        print(f"{product} : {price:,} Toman")

    print("=================================")