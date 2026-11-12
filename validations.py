
def is_int(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

def is_not_negative(number):
    if not is_int(number):
        return False
    number = int(number)
    if number < 0:
        return False
    return True

def is_int_and_positive(number):
    if not is_int(number):
        return False
    number = int(number)
    if number < 1:
        return False
    return True

def check_str(word):
    if len(word) < 1:
        return False
    return True

def main_choose_checker(number):
    if not is_int(number):
        return False
    number = int(number)
    if number < 1 or number > 5:
        return False
    return True

def products_menu_checker(number):
    if not is_int(number):
        return False
    number = int(number)
    if number < 1 or number > 6:
        return False
    return True

def search_product_checker(number):
    if not is_int(number):
        return False
    number = int(number)
    if number > 3 or number < 1:
        return False
    return True


