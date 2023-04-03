from bar_tab import Tab
from bar_categories import *

while True:
    show_menu()
    select_category = input('Please select a category (1 drinks / 2 food / 3 receipt). To close the app press 0. >> ')
    if select_category == '1':
        category_drinks()
    elif select_category == '2':
        category_food()
    elif select_category == '3':
        category_receipt()
        break
    elif select_category == '0':
        break
    else:
        print('Please select a valid category!')