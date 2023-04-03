class Tab:

    menu = {
        'wine' : 5.50,
        'beer' : 3.50,
        'soft_drink' : 2.50,
        'beef' : 15.50,
        'chicken' : 10.50,
        'veggie' : 12.50,
        'dessert' : 6.50,
    }

    # starting point for total price and items list
    def __init__(self):
        self.total = 0
        self.items = [ ]

    # function to add items to the bill and increase total according to menu
    def add(self, item):
        self.items.append(item)
        self.total += self.menu[item]

    # function to print bill with added tax, tip
    def print_bill(self, tax, service):
        tax = (tax/100) * self.total
        service = (service/100) * self.total
        placeholder = ""
        total = self.total + tax + service
        
        # each item gets printed, dublicates removed
        for item in set(self.items):
            num = self.items.count(item)
            # :20 after item gives 20 char distance between $ and first char of item
            print(f'{num} x {item:20}${self.menu[item]*num}')

        print('')
        print(f'VAT{placeholder:21}${tax:.2f}')
        print(f'Service charge{placeholder:10}${service:.2f}')
        print('')
        print(f'{"Total":24}${total:.2f}')
