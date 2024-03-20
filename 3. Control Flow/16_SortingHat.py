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
