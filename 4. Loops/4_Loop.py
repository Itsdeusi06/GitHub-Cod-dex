# 17. Enter PIN
print('BANK OF CODÉDEX')

pin = int(input('Enter your PIN: '))

while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 1234:
  print('PIN accepted!')


# 18. Guess Number
guess = 0

while guess != 6:
  guess = int(input("Guess the number:  "))

print("You got it!")


# 19. Detention
for i in range(100):
  print("I will not use Snapchat in class")


# 20. 99 Bottles
for x in range(99, 0, -1):
  print(f"{x} bottles of beer on the wall")
  print(f"{x} bottles of bear")
  print("Take one down, pass it around")
  

# 21. Fizz Buzz|
for i in range(1,100):
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
   print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)