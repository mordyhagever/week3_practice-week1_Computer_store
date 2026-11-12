from db import products
from products import search_product
from validations import *

def print_inventory_menu():
    print("""
    ======= INVENTORY MENU =======
    
    1. Show full stock
    2. Search item in stock
    3. add to a product stock
    4. decrease a product stock
    5. show out of stock products
    6. show low stock products
    7. back to main menu
    """)
    choose = input()
    while not inventory_choose_checker(choose):
        choose = input("Only a positive number from the menu: ")
    choose = int(choose)
    return choose


def show_full_inventory():
    for item in products:
        print(item)
    return "Full inventory is showing now"

def search():
    return search_product()

def add_to_product():
    product_id = input("Enter product id: ")
    while not is_int_and_positive(product_id):
        product_id = input("Only a positive number: ")
    product_id = int(product_id)
    how_much = input("Enter how many products to add: ")
    while not is_int_and_positive(how_much):
        how_much = input("only a positive number: ")
    how_much = int(how_much)
    for item in products:
        if item["id"] == product_id:
            item["stock"] += how_much
    return "\nstock was updated successfully!"

def remove_from_product():
    product_id = input("Enter product id: ")
    while not is_int_and_positive(product_id):
        product_id = input("Only a positive number: ")
    product_id = int(product_id)
    how_much = input("Enter how many products to decrease: ")
    while not is_int_and_positive(how_much):
        how_much = input("only a positive number: ")
    how_much = int(how_much)
    for item in products:
        if item["id"] == product_id:
            if item["stock"] >= how_much:
                item["stock"] -= how_much
                return "\nstock was updated successfully!"
            else:
                return "not enough stock to decrease"
    return "couldn't find the product"


def out_of_stock():
    zero_stock = []
    for item in products:
        if item["stock"] == 0:
            zero_stock.append(item)
    return zero_stock

def low_stock():
    low = input("Enter what's considered low stock: ")
    while not is_not_negative(low):
        low = input("Only a non negative number: ")
    low = int(low)
    low_list = []
    for item in products:
        if item["stock"] <= low:
            low_list.append(item)
    return low_list




def inventory_manager():
    choice = print_inventory_menu()
    while choice != 7:
        if choice == 1:
            print(show_full_inventory())
        elif choice == 2:
            print(search())
        elif choice == 3:
            print(add_to_product())
        elif choice == 4:
            print(remove_from_product())
        elif choice == 5:
            print("OUT OF STOCK:")
            print(out_of_stock())
        elif choice == 6:
            print("LOW STOCK:")
            print(low_stock())
        choice = print_inventory_menu()
    return "Back to main menu"



