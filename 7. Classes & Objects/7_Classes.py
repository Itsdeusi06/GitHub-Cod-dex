# 34. Restaurants
class Restaurant:
    name = 'PitICullons'
    category = 2
    rating = 4.7
    delivery =  True

class Restaurant:
    name = ''
    category = 0
    rating = 0
    delivery =  False


# 35. Bob's Burgers
Bob_Burgers = Restaurant()


Bob_Burgers.id = 111
Bob_Burgers.name = 'Bob\'s Burgers'
Bob_Burgers.category = 'American Diner'
Bob_Burgers.rating = 4.8
Bob_Burgers.delivery = True

print(vars(Bob_Burgers))


Mcdonals = Restaurant()

Mcdonals.id = 1111
Mcdonals.name = 'McDonals'
Mcdonals.category = 'FastFood'
Mcdonals.rating = 10
Mcdonals.delivery = True

print(vars(Mcdonals))


Nafent = Restaurant()

Nafent.id = 111
Nafent.name = 'Nafent'
Nafent.category = 'Town food'
Nafent.rating = 3
Nafent.delivery = False

print(vars(Nafent))


# 36. Favorite Cities
class City:
    def __init__(self, name, county, population, landmarks):
        self.name = name
        self.county = county
        self.population = population
        self.landmarks = landmarks


Torroella = City('Torroella de Montgri', 'Girona', 10000, False)

print(vars(Torroella))


Girona = City('Girona', 'Catalunya', 50000, True)

print(vars(Girona))


Madrid = City('Madrid', 'España', 100000, False)

print(vars(Madrid))


# 37. Bank Accounts
class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance
   
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            print("Sorry, you don't have enough funds.")
            return 0

    def display_balance(self):
        print(self.balance)


customer = BankAccount("John", "Doe", "12345", "Savings", "54321", 500)
customer.deposit(250)  # This should print: "You've deposited $250. Your new balance is $750."
customer.withdraw(100) # This should print: "You've withdrawn $100. Your new balance is $650."
customer.display_balance()  # This should print: "Your current balance is $650."


# 38. Pokédex
class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught
    def speak(self):
        print(self.entry,self.name,self.types,self.description,self.is_caught, 'this is what',self.name,'says alsways',self.name, self.name)
        return print

Picka = Pokemon(25, 'Pikachu', 'Electric', 'cute and main pokemon', True)
Picka.speak()