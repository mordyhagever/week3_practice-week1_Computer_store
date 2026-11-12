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

def update_quantity(cart):
    updated_item = {}
    item = input("Enter a product id to change quantity: ")
    while is_int_and_positive(item):
        item = input("Only a positive number: ")
    item = int(item)
    quantity = input("Enter amount of the product to add: ")
    while not is_int_and_positive(quantity):
        quantity = input("Only a positive number: ")
    quantity = int(quantity)
    for item in cart:
        if item["id"] == item:
            if item["stock"] >= quantity:
                updated_item["product"] = item
                updated_item["quantity"] = quantity
            else:
                return "Not enough in stock!!!"
    return updated_item

def remove_item(cart):
    item_id = input("Enter a product id to remove from cart: ")
    while not is_int_and_positive(item_id):
        item_id = input("Only a positive number:")
    item_id = int(item_id)
    for product in cart:
        if product["id"] == item_id:
            cart.remove(product)
            return "Product has been removed from cart!"
    return "Couldn't find the product"

def calc_cart(cart):
    sum_cart = 0
    if not cart:
        return None
    for item in cart:
        item_price = item["price"] * item["quantity"]
        sum_cart += item_price
    return sum_cart

def add_discount(cart_price):
    discount = input("Enter discount percentage: ")
    while not discount_checker(discount):
        discount = input("Only a positive number between 1 and 100")
    discount = int(discount)
    final_price = round(cart_price - cart_price * (discount / 100), 2)
    return final_price


def print_menu():
    print("""
    ======= CART MENU ======
    ==== New cart opened ====
    1. Add items
    2. update item quantity
    """)

def sales_manager():
    new_cart = new_sale()
    new_item = add_items()
    new_cart.append(new_item)




