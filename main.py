from validations import main_choose_checker
from products import products_manager
from inventory import inventory_manager
from sales import sales_manager

def print_menu():
    print("""
    =================================
         COMPUTER STORE SYSTEM
    =================================

1. Products Management
2. Inventory Management
3. Sales Management
4. Reports
5. Exit

Choose an option:
    """)
    choose = input()
    while not main_choose_checker(choose):
        choose = input("Only a number from the menu: ")
    choose = int(choose)
    return choose


def active1():
    print(products_manager())
def active2():
    print(inventory_manager())
def active3():
    print(sales_manager())
def active4():
    pass

def main_menu():
    choose = print_menu()
    while choose != 5:
        if choose == 1:
            active1()
        elif choose == 2:
            active2()
        elif choose == 3:
            active3()
        elif choose == 4:
            active4()
        choose = print_menu()
    return "Progress has finished successfully"

main_menu()