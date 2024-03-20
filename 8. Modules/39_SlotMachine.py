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