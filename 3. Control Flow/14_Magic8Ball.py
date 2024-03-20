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