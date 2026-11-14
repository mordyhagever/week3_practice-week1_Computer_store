from validations import *
from db import sales, products

def print_reports_menu():
    print("""
    ============= REPORTS =============

1. Total Sales
2. Total Revenue
3. Best Selling Products
4. Average Sale
5. Sales History
6. Category Statistics
7. Back
    """)
    choose = input()
    while not reports_choose_checker(choose):
        choose = input("only a number between 1 and 7")
    choose = int(choose)
    return choose

def total_sales():
    if not sales:
        return "There's no sales available"
    return len(sales)

def total_revenue():
    total = 0
    if not sales:
        return "There's no sales available"
    for sale in sales:
        total += sale["total"]

    return total

def best_selling_product():
    if not sales:
        return "There's no sales available"
    all_selling = []
    for sale in sales:
        for item in sale["items"]:
            all_selling.append((item["name"], item["quantity"]))
    top5 = sorted(all_selling, key=lambda item: item[1], reverse=True)[:5]
    return top5

def average_sale():
    if not sales:
        return "There's no sales available"
    total = total_revenue()
    length = total_sales()
    return total / length

def sales_history():
    if not sales:
        return "There's no sales available"
    for sale in sales:
        print(sale)
    return "All sales are displayed"

def category_statistics():
    if not sales:
        return "There's no sales available"
    categories = {}
    all_selling = []
    for sale in sales:
        for item in sale["items"]:
            all_selling.append((item["name"], item["quantity"]))

    for product in products:
        if product["category"] not in categories:
            category = product["category"]
            categories[category] = 0


    for sold in all_selling:
        for product in products:
            if sold[0] == product["name"]:
                category = product["category"]
                categories[category] += sold[1]
    return categories


def reports_manager():
    choose = print_reports_menu()
    while choose != 7:
        if choose == 1:
            print(f"number of total sales: {total_sales()}")
        elif choose == 2:
            print(f"total revenue is: {total_revenue()}")
        elif choose == 3:
            print(f"top 5 selling products: {best_selling_product()}")
        elif choose == 4:
            print(f"average sale price: {average_sale()}")
        elif choose == 5:
            print("All sales:")
            sales_history()
        elif choose == 6:
            print(f"Category statistics: \n{category_statistics()}")
        choose = print_reports_menu()

    return "Back to main menu"



