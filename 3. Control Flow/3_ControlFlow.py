# 11. Coin Flip
import random

num = random.randint(0, 1)   # Generates a random number that's either 0 or 1

if num > 0.5:
  print('Heads')
else:
  print('Tails')


# 12. Grades
import random
grade = random.randint(0, 100)
if grade > 60:
  print("You passed!")
else:
  print("You failde:(")


# 13. pH Levels|
import random
ph = random.randint(0, 14)
if ph > 7:
  print("Basic")
if ph < 7:
  print("Acidic")
else:
  print("Neutral")


# 14. Magic 8 Ball
import random
magic8ball = random.randint(1, 9)
Question = input("Question: ")
if magic8ball == 1:
  print("Yes - definitely.")
if magic8ball == 2:
  print("It is decidedly so.")
if magic8ball == 3:
  print("Without a doubt.")
if magic8ball == 4:
  print("Reply hazy, try again.")
if magic8ball == 5:
  print("Ask again later.")
if magic8ball == 6:
  print("Better not tell you now.")
if magic8ball == 7:
  print("My sources say no.")
if magic8ball == 8:
  print("Outlook not so good.")
if magic8ball == 9:
  print("Very doubtful.")


# 15. The Cyclone|
height = int(input("How tall are you? "))
credits = int(input("How many credits you have? "))

if height >= 137 and credits >= 10:
  print("Enjoy the ride!")
elif height < 137 and credits < 10:
  print("You are poor and short. Go home!")
elif height < 137:
  print("You are not tall enough to ride")
elif credits < 10:
  print("You don't have enough credits")


# 16. Sorting Hat|
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

            #QUESTION 1
print("Q1) Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")
Q1 = int(input("Aswer (1 or 2): "))
if Q1 == 1:
  Gryffindor += 1 
  Ravenclaw += 1
elif Q1 == 2:
  Hufflepuff += 1 
  Slytherin += 1
else:
  print("Wrong input")

            #QUESTION 2
print("Q2) When I'm dead, I want people to remember me as:")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")

Q2 = int(input("Aswer (1 to 4): "))
if Q2 == 1:
  Hufflepuff += 2 
elif Q2 == 2:
  Slytherin += 2
elif Q2 == 3:
  Ravenclaw += 2
elif Q2 == 4:
  Gryffindor +=2
else:
  print("Wrong input")

            #QUESTION 3
print("Q3) Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")

Q3 = int(input("Aswer (1 to 4): "))
if Q3 == 1:
  Slytherin += 4 
elif Q3 == 2:
  Hufflepuff += 4
elif Q3 == 3:
  Ravenclaw += 4
elif Q3 == 4:
  Gryffindor += 4
else:
  print("Wrong input")

max_value = max(Gryffindor, Ravenclaw, Hufflepuff, Slytherin)
if max_value == Gryffindor:
  print("🦁 Gryffindor")
elif max_value == Ravenclaw:
  print("🦅 Ravenclaw")
elif max_value == Hufflepuff:
  print("🦡 Hufflepuff")
elif max_value == Slytherin:
  print("🐍 Slytherin")
else:
  print("You don't know any of them")
