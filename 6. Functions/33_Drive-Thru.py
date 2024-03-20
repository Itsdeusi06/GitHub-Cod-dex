def get_item(x):
    menu = {
        1: '🍔 Cheeseburger',
        2: '🍟 Fries',
        3: '🥤 Soda',
        4: '🍦 Ice Cream',
        5: '🍪 Cookie'
    }
    return menu.get(x, 'Invalid item number')

def welcome():
    print("Welcome to the menu:")
    print("1. 🍔 Cheeseburger")
    print("2. 🍟 Fries")
    print("3. 🥤 Soda")
    print("4. 🍦 Ice Cream")
    print("5. 🍪 Cookie")

welcome()

option = int(input('What would you like to order? '))
print(get_item(option))
