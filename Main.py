# Main.py

from Menu import show_menu
from Order import add_order, show_orders, orders
from Billing import calculate_total, print_invoice

def main():
    while True:
        print("\n========== Coffee Shop ==========")
        print("1. Show Menu")
        print("2. Add Order")
        print("3. Show Orders")
        print("4. Calculate Total")
        print("5. Print Invoice")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_menu()

        elif choice == "2":
            add_order()

        elif choice == "3":
            show_orders()

        elif choice == "4":
            if not orders:
                print("There are no orders yet.")
            else:
                total = calculate_total(orders)
                print(f"Total Order Amount: {total:,} Toman")

        elif choice == "5":
            print_invoice(orders)

        elif choice == "6":
            print("Thank you for visiting! Goodbye!")
            break

        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()