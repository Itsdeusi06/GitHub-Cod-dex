# 22. Grocery List
grocery  = ['🥚 Eggs', '🥑 Avocados ', '🍪 Cookies ', '🌶 Hot Pepper Jam ', '🫐 Blueberries','🥦 Broccoli']

print(grocery)


# 23. To-Do List
todo = ['🏦 Get quarters.','🧺 Do laundry.','🌳 Take a walk.','💈 Get a haircut.','🍵 Make some tea.','💻 Complete Lists chapter.','💖 Call mom.','📺 Watch My Hero Academia.']
# Index:        0 / 8              1 / 7             2 / 6              3 / 5             4 / 4                  5 / 3               6 / 2                   7 / 1

print(todo[0])
print(todo[1])
print(todo[2])
print(todo[3])
print(todo[4])
print(todo[5])
print(todo[6])
print(todo[7])
print(todo[-1])
print(todo[-2])
print(todo[-3])
print(todo[-4])
print(todo[-5])
print(todo[-6])
print(todo[-7])
print(todo[-8])
print(todo[0 : 7])
print(todo[-7 : 7])
####  print(todo[9])  #### Ens dira: IndexError: list index out of range 


# 24. Inventory
lego_parts = [8980, 7323, 5343, 82700, 92232, 1203, 7319, 8903, 2328, 1279, 679, 589]

print(min(lego_parts))
print(max(lego_parts))


# 25. Reading List
reading_list = ['Zero to One', 'The Lean Startup', 'The Mom Test', 'Make It Stick', 'Life in Code']

reading_list.append('Zero to Sold')

reading_list.remove('Zero to One')

reading_list.pop(0)

print(reading_list)


# 26. Mixtape
playlist = ['FARDOS', 'GATA ONLY', 'M.A.I', 'YOUNG MIKO: BZRP MUSSIC SESSION']

for i in range(len(playlist)):
  print(playlist[i])


# 27. Bucket List
things_to_do = [
  'Learn python.',
  'Learn C++.',
  'Go to another country to study',
  'Work in a good paid/time work place.',
  'Found a good gril to we my wife.',
  'Have good friend to share emotions with',
  'Get a house and a car (if possible a porche 911 or Kupra Formentor)',
  'Idk what more',
  'I had never tought this'
]


things_to_do.append(input('Some thing good you expected rn: '))

things_to_do.remove('Idk what more')

things_to_do.pop(7)


for i in (things_to_do):
  print(i)