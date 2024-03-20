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

