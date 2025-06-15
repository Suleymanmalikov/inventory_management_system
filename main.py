
from inventory import Inventory
from product import Product
import utils


def main():
    products = utils.read_products_from_json('products.json')['products']
    myInventory = Inventory()
    for product in products:
        myInventory.add_product(Product(product['name'], product['price'], product['quantity']))
    print("1. View Inventory\n" \
        "2. Add Product\n" \
        "3. Remove Product\n" \
        "4. Restock product\n" \
        "5. Show Total Inventory Value\n" \
        "6. Exit\n")
    while(True):
        user_input = input()
        match user_input.lower():
            case "1":
                print()
                myInventory.view_inventory()
                print()
                continue
            case "2":
                name = input("Enter Product Name: ")
                price = float(input("Enter Product Price: "))
                quantity = int(input("Enter Product Quantity: "))
                print(myInventory.add_product(Product(name, price, quantity)))
            case "3":
                print("\nplease put the name: ")
                name_of_product = input()
                print(myInventory.remove_product_by_name(name_of_product))
            case "4":   
                name_of_product = input("input Name of Product: ")
                new_quantity = int(input("Input new quantity: "))
                print(myInventory.restock_product_by_name(name_of_product, new_quantity))

            case "5":
                print(f"Total value in inventory is ${myInventory.show_total_inventory_value():,}")
            case "help":
                print("1. View Inventory\n" \
                    "2. Add Product\n" \
                    "3. Remove Product\n" \
                    "4. Restock product\n" \
                    "5. Show Total Inventory Value\n" \
                    "6. Exit\n")
            case "6":
                exit()
            case default:
                print("Choose number between 1-6")

if __name__ == "__main__":
    main()