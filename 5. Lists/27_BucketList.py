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