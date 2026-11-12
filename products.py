from validations import *
from db import products

def get_next_id():
    last_product = products[-1]
    return last_product["id"] + 1


def print_product_management():
    print("""
    --------- PRODUCTS MANAGEMENT ---------

1. Add Product
2. Display All Products
3. Search Product
4. Update Product
5. Delete Product
6. Back to Main Menu
    """)
    choose = input()
    while not products_menu_checker(choose):
        choose = input("Only a number from the menu: ")
    choose = int(choose)
    return choose

def add_product():
    product_name = input("Enter product name: ")
    while not check_str(product_name):
        product_name = input("Enter a non empty name: ")
    category = input("Enter category")
    while not check_str(category):
        category = input("Enter a non empty category: ")
    price = input("Enter product's price: ")
    while not is_int_and_positive(price):
        price = input("only a positive number: ")
    price = int(price)
    quantity = input("Enter quantity")
    while not is_not_negative(quantity):
        quantity = input("quantity has to be non negative: ")
    quantity = int(quantity)
    product_data = {}
    product_data["id"] = get_next_id()
    product_data["name"] = product_name
    product_data["category"] = category
    product_data["price"] = price
    product_data["stock"] = quantity
    if quantity > 0:
        product_data["active"] = True
    else:
        product_data["active"] = False
    products.append(product_data)
    return product_data

def display_all_products():
    active_products = []
    for item in products:
        if item["active"]:
            active_products.append(item)
    return active_products

def search_product():
    print("""
    What's your search type?
    1. search by id
    2. search ny name or partly name
    3. search by category
    """)
    choose = input()
    while not search_product_checker(choose):
        choose = input("Only a number from the menu: ")
    choose = int(choose)
    if choose == 1:
        search_id = input("Enter id to search: ")
        while not is_int_and_positive(search_id):
            search_id = input("id must be a positive number: ")
        search_id = int(search_id)
        for item in products:
            if item["id"] == search_id:
                print(item)
                return "Product was printed successfully"
        return "Couldn't find product"
    elif choose == 2:
        search_name = input("Enter name or part of name to search: ")
        while not check_str(search_name):
            search_name = input("only a non empty search: ")
        for item in products:
            if search_name in item["name"]:
                print(item)
        return "Finished the search"
    else:
        search_category = input("Enter product category: ")
        while not check_str(search_category):
            search_category = input("only a non empty category")
        for item in products:
            if item["category"] == search_category:
                print(item)
        return "Finished the search"




def products_manager():
    choose = print_product_management()
