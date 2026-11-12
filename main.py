from validations import main_choose_checker

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
    pass
def active2():
    pass
def active3():
    pass
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
