from db import products
from validations import *

def new_sale():
    new_cart = []
    print("""
    ============ NEW SALE ============ 
    """)
    return new_cart

def add_items():
    new_item_dict = {}
    add_item = input("Enter a product id to add: ")
    while not is_int_and_positive(add_item):
        add_item = input("Only a non negative id number: ")
    add_item = int(add_item)
    quantity = input("Enter amount of the product to add: ")
    while not is_int_and_positive(quantity):
        quantity = input("Only a positive number: ")
    quantity = int(quantity)
    for item in products:
        if item["id"] == add_item:
            if item["stock"] >= quantity:
                new_item_dict["product"] = add_item
                new_item_dict["quantity"] = quantity
            else:
                return "Not enough in stock!!!"
    return new_item_dict

def update_quantity():
    updated_item = {}
    item = input("Enter a product id to change quantity: ")
    while is_int_and_positive(item):
        item = input("Only a positive number: ")
    item = int(item)
    quantity = input("Enter amount of the product to add: ")
    while not is_int_and_positive(quantity):
        quantity = input("Only a positive number: ")
    quantity = int(quantity)
    for item in products:
        if item["id"] == item:
            if item["stock"] >= quantity:
                updated_item["product"] = item
                updated_item["quantity"] = quantity
            else:
                return "Not enough in stock!!!"
    return updated_item









def sales_manager():
    pass
