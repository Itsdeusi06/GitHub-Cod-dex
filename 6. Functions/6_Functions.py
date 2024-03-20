# 28. D.R.Y.
num = ["1","2","3","4","45","56","6", "asdf","778"]
numb = ["2341","2534","3231","44123","4541","5614231","6","778"]

print("hello wrld")
print(max(num))
print(range(1, 5))
print(len(num))
print(all(num))


# 29. Fortune Cookie
import random

random_fortune = [
  "Don't pursue happiness – create it.",
  "All things are difficult before they are easy.",
  "The early bird gets the worm, but the second mouse gets the cheese.",
  "Someone in your life needs a letter from you.",
  "Don't just think. Act!",
  "Your heart will skip a beat.",
  "The fortune you search for is in another cookie.",
  "Help! I'm being held prisoner in a Chinese bakery!",
  ]

def fortune():
  num = random.randint(0, 7)
  print(random_fortune[num])

fortune()

# 30. Mars Orbiter
def distance_to_miles(distance):
  km = int(input('How km: '))
  m = (km / 1609)
  print(m)

distance_to_miles(10000)


# 31. Calculator
def add(a, b):
  answer = a + b
  return answer

print(add(12, 9))

def subtract(a, b):
  answer = a - b
  return answer

print(subtract(19, 3))

def multiply(a, b):
  answer = a * b
  return answer

print(multiply(34273294, 23498723))

def divide(a, b):
  answer = a / b
  return answer

print(divide(234, 2355))

def exp(a, b):
  answer = a ** b
  return answer

print(exp(88, 23))


# 32. Stonks
stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56,
                49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(x):
    return stock_prices[x - 1]

def max_price(a, b):
    return max(stock_prices[a - 1:b])

def min_price(a, b):
    return min(stock_prices[a - 1:b])

# Let's test these functions
print(price_at(3))        # Output: 34.94
print(max_price(3, 6))    # Output: 35.82
print(min_price(3, 6))    # Output: 33.97


# 33. Drive-Thru
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
