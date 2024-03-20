# 39. Slot Machine
import random
def play():
  symbol = ['🍒', '🍇', '🍉', '7️⃣']
  results = random.choices(symbol, k=3)
  print(f'{results[0]}  | {results[1]}  | {results[2]}')
  if results == '7️⃣' and results == '7️⃣' and results == '7️⃣':
    print('Jackpot! 💰')
  else:
    print('Try again (Y or N)')

while True:
  play()
  play_again = input('Do you wna play agian? (Y or N): ')
  if play_again.lower() == 'Y' or play_again.lower() == 'y' or play_again.lower() == 'yes' or play_again.lower() == 'Yes':
    continue
  else:
    break
  

# 40. Solar System
from math import pi

from random import choice as ch

r = 0

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planet = ch(planets)

if random_planet == 'Mercury':
  r = 2440
elif random_planet == 'Venus':
  r = 6052
elif random_planet == 'Earth':
  r = 6371
elif random_planet == 'Mars':
  r = 3390
elif random_planet == 'Saturn':
  r = 58232
else:
  print('Oops! An error occorred')

area = 4 * pi * r ** 2

print(f'The area of the planet {random_planet} is {area}')


# 41. Countdown
