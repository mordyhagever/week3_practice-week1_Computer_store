from db import products, sales
from validations import *

def get_next_id():
    if not sales:
        return 1
    else:
        last_sale = sales[-1]
    return last_sale["id"] + 1


def new_sale():
    new_cart = []
    print("""
    ============ NEW SALE ============ 
    """)
    return new_cart

def add_items(cart):
    new_item_dict = {}
    found = False
    already_exist = False
    add_item = 0
    while not found:
        add_item = input("Enter a product id to add: ")
        while not is_int_and_positive(add_item):
            add_item = input("Only a non negative id number: ")
        add_item = int(add_item)
        for item in products:
            if item["id"] == add_item:
                found = True
        if not found:
            print("Couldn't find id")

    for product in cart:
        if add_item == product["product_id"]:
            already_exist = True
    if already_exist:
        return "Products is already in cart, please choose 'update quantity'!"


    enough = False
    while not enough:
        quantity = input("Enter amount of the product to add: ")
        while not is_int_and_positive(quantity):
            quantity = input("Only a positive number: ")
        quantity = int(quantity)
        for item in products:
            if item["id"] == add_item:
                if item["stock"] >= quantity:
                    new_item_dict["product_id"] = add_item
                    new_item_dict["name"] = item["name"]
                    new_item_dict["quantity"] = quantity
                    new_item_dict["unit_price"] = item["price"]
                    new_item_dict["total"] = new_item_dict["unit_price"] * new_item_dict["quantity"]
                    enough = True
                else:
                    print("Not enough in stock!!!")
    return new_item_dict


def update_quantity(cart):
    print("Enter plus or minus: ")
    action = str(input())
    while action != "+" and action != "-":
        action = str(input("Only + or -"))
    item = input("Enter a product id to change quantity: ")
    while not is_int_and_positive(item):
        item = input("Only a positive number: ")
    item = int(item)

    quantity = input("Enter amount of the product to add or decrease: ")
    while not is_int(quantity):
        quantity = input("Only a number: ")
    quantity = int(quantity)
    for product in cart:
        if product["product_id"] == item:
            if action == "+":
                for stuff in products:
                    if item == stuff["id"]:
                        if stuff["stock"] < quantity:
                            return "Not enough in stock"
                        else:
                            product["quantity"] += quantity
                            return "Item has been updated"
            elif action == "-":
                if product["quantity"] >= quantity:
                    product["quantity"] -= quantity
                else:
                    return "Not enough in stock!!!"
        else:
            return "Product isn't in cart"

    return "Item has been updated successfully"

def remove_item(cart):
    item_id = input("Enter a product id to remove from cart: ")
    while not is_int_and_positive(item_id):
        item_id = input("Only a positive number:")
    item_id = int(item_id)
    for product in cart:
        if product["product_id"] == item_id:
            cart.remove(product)
            return "Product has been removed from cart!"
    return "Couldn't find the product"

def calc_cart(cart):
    sum_cart = 0
    if not cart:
        return None
    for item in cart:
        for product in products:
            if item["product_id"] == product["id"]:
                item_price = product["price"] * item["quantity"]
                sum_cart += item_price
    return sum_cart

def add_discount(cart_price):
    discount = input("Enter discount percentage: ")
    while not discount_checker(discount):
        discount = input("Only a positive number between 1 and 100")
    discount = int(discount)
    final_price = round(cart_price - cart_price * (discount / 100), 2)
    return discount, final_price


def print_menu():
    print("""
    ======= CART MENU ======
    ==== New cart opened ====
    1. Add items
    2. update item quantity
    3. remove an item from cart
    4. calculate cart checkout
    5. Enter a discount if you want 
    6. show cart
    7. Close the sale
    """)
    choose = input("Enter an action from the menu: ")
    while not sales_choose_checker(choose):
        choose = input("only a number from the menu: ")
    choose = int(choose)
    return choose

def update_products(cart):
    for item in cart:
        for product in products:
            if item["product_id"] == product["id"]:
                product["stock"] -= item["quantity"]
                return "Stock has been updated successfully"
    return "Couldn't find product"

def show_cart(cart):
    return cart




def sales_manager():
    sale = {}
    after_discount = None
    sale["id"] = get_next_id()
    new_cart = new_sale()
    final_price = None
    choose = print_menu()
    while choose != 7:
        if choose == 1:
            new_item = add_items(new_cart)
            if not isinstance(new_item, dict):
                print(new_item)
            else:
                new_cart.append(new_item)
                print(f"""\n
                Product ID: {new_item["product_id"]}
                Quantity: {new_item["quantity"]}
                
                added successfully!""")
        elif choose == 2:
            print(update_quantity(new_cart))
        elif choose == 3:
            print(remove_item(new_cart))
        elif choose == 4:
            final_price = calc_cart(new_cart)
            print(f"final price before discount: {final_price}")
        elif choose == 5:
            final_price = calc_cart(new_cart)
            after_discount = add_discount(final_price)
            print(f"Final price after discount: {after_discount[1]}")
        elif choose == 6:
            all_items = show_cart(new_cart)
            for item in all_items:
                print(item)
        choose = print_menu()
    final_price = calc_cart(new_cart)
    update_products(new_cart)
    sale["items"] = new_cart
    sale["subtotal"] = final_price
    if isinstance(after_discount, tuple):
        sale["discount"] = after_discount[0]
        sale["total"] = after_discount[1]
    else:
        sale["discount"] = 0
        sale["total"] = final_price
    sales.append(sale)
    print(f"""
    ========= SALE SUMMARY =========
    """)
    for item in new_cart:
        print(f"{item["name"]}:    {item["quantity"]} x {item["unit_price"]} = {item["total"]}")
    print("------------------------------")
    print(f"Subtotal:       {sale["subtotal"]}")
    print(f"Discount:       {sale["discount"]}%")
    print(f"Total:          {sale["total"]}")

    return "sale has been closed and updated successfully"








