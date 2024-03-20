class Restaurant:
    name = ''
    category = 0
    rating = 0
    delivery =  False

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