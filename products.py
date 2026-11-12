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
    if is_int(price):
        price = int(price)
    if is_float(price):
        price = float(price)
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

def update_product():
    product_id = input("what product do you want to update? [by id]: ")
    while not is_int_and_positive(product_id):
        product_id = input("Only a positive id number: ")
    product_id = int(product_id)
    found = False
    product_to_update = None
    for item in products:
        if item["id"] == product_id:
            found = True
            product_to_update = item
            break
    if not found:
        return "Sorry, couldn't find the product. please try again later"
    else:
        print("""
        Product found!!!
        What do you wanna update in the product?
        1. name
        2. category
        3. price
        4. status
        """)
        choose = input()
        while not update_product_checker(choose):
            choose = input("Only a number from the menu: ")
        choose = int(choose)
        if choose == 1:
            new_name = input("Enter new name for the product you chose: ")
            while not check_str(new_name):
                new_name = input("Only a non empty name: ")
            product_to_update["name"] = new_name
            print(f"product number {product_id} name, changed to {new_name}")
        elif choose == 2:
            new_category = input("Enter a new category name for the product you chose: ")
            while not check_str(new_category):
                new_category = input("Only a non empty name: ")
            product_to_update["category"] = new_category
            print(f"product number {product_id} category, changed to {new_category}")
        elif choose == 3:
            new_price = input("Enter a new price fot the product you chose: ")
            while not is_int_and_positive(new_price):
                new_price = input("Only a positive price: ")
            if is_int(new_price):
                new_price = int(new_price)
            if is_float(new_price):
                new_price = float(new_price)
            product_to_update["price"] = new_price
            print(f"product number {product_id} price, changed to {new_price}")
        elif choose == 4:
            current_status = product_to_update["status"]
            print(f"product status is now {current_status}, do you wanna change it? [Y/N]")
            user_choice = input()
            while user_choice not in ["Y", "N"]:
                user_choice = input("Please choose [Y/N]")
            if user_choice == "Y":
                product_to_update["status"] = not current_status
                print("status has changed successfully")
            print("status stayed the same as you asked.")
    for i in range(len(products)):
        if products[i]["id"] == product_id:
            products.pop(i)
            products.insert(i, product_to_update)
            return "Update progres has finished"

    return "update product isn''t working if it reached here"


def delete_product():
    product_id = input("Enter id number to delete:")
    while not is_int(product_id):
        product_id = input("only a positive number: ")
    product_id = int(product_id)
    decision = input("Are you sure that you want to delete this project forever? [Y/N]")
    while not check_str(decision) or (decision != "Y" and decision != "N"):
        decision = input("Enter your correct answer [Y/N]")
    if decision == "Y":
        for item in products:
            if item["id"] == product_id:
                products.remove(item)
                return "product was deleted"
    else:
        return "Didn't delete anything"
    return "You're not supposed to get here"





def products_manager():
    choose = print_product_management()
    while choose != 6:
        if choose == 1:
            print(add_product())
        elif choose == 2:
            print(display_all_products())
        elif choose == 3:
            print(search_product())
        elif choose == 4:
            print(update_product())
        elif choose == 5:
            print(delete_product())
        choose = print_product_management()
    return "Back to main menu"
