placeholder = ""
select_category = ""
items = []
total = 0
service = 0
tax = 7

drinks_menu = {
    'water' : 2.50,
    'soft drinks' : 3.50,
    'beer' : 4.50,
    'wine' : 5.50
}
food_menu = {
    'chicken' : 10.50,
    'veggie' : 12.50,
    'beef' : 15.50,
    'dessert' : 6.50
}
menu = food_menu | drinks_menu

def total_price(total, tax, service):
    return total + tax + service

def print_receipt():
    print(f'\n{placeholder:22}Thank you for dining with us!\n')
    for item in set(items):
        num = items.count(item)
        print(f'{num} x {item:20}${menu[item]*num:.2f}')
    print(f'\nVAT{placeholder:21}${tax:.2f}')
    print(f'Service charge{placeholder:10}${service:.2f}\n')
    print(f'{"Total":24}${total_price(total, tax, service):.2f}')

def show_menu():

    print(f'{placeholder:35}MENU')
    print(f'\n{placeholder:34}DRINKS')
    print(f'{placeholder:35}FOOD')
    print(f'{placeholder:31}PRINT RECEIPT\n')

def category_drinks(): 
    global total   

    print(f'\n{placeholder:30}DRINK SELECTION:\n')

    for key, val in drinks_menu.items():
        print(f'{key.upper():30}${val}')
        print('')
    
    while True:
        select_drink = input('Please select a drink (by name) or go back (0) >> ')            
        if select_drink == '0':
            break
        else:
            items.append(select_drink)  
            total += drinks_menu[select_drink]

        another = input('Add another? (y/n) >> ')
        if another == 'y':
            continue
        else:
            select_category == 'food'
            break                

def category_food():   
    global total     

    print(f'\n{placeholder:30}FOOD SELECTION:\n')

    for key, val in food_menu.items():
        print(f'{key.upper():30}${val}')
        print('')
    
    while True:
        select_food = input('Please select a food (by name) or go back (0) >> ')
        if select_food == '0':
            break
        else:
            items.append(select_food)
            total += food_menu[select_food]

        another = input('Add another? (y/n) >> ')
        if another == 'y':
            continue
        else:
            select_category == 'drinks'
            break          

def category_receipt():
    global tax
    global total
    global service
    tax = (tax/100) * total
    service = (service/100) * total
    
    tip = input('Would you like to add a tip? (y/n) >> ')
    if tip == 'y':
        service = int(input('How much would you like to add (in $): '))
        print_receipt()
    else:
        print_receipt()
