# 06. Data Types
name = 'Erlich Bachman'
user_id = 16180339887
progress = 0.75
exp = 60
verified = True
year = 2023
age = 32
xp = 70
xp = 80
print(xp)


# 07. Temperature
fahrenhei = 54
celsius = (fahrenhei - 32) / 1.8
print(celsius)


# 08. BMI
weight = 92.3
height = 1.86

bmi = weight / (height**2)

print(bmi)


# 09. Pythagorean Theorem
import math
costat1 = int(input("enter costat1: "))
costat2 = int(input("enter costat2: "))

hipotenusa = math.sqrt(costat1*costat1 + costat2*costat2)
print(hipotenusa)


# 10. Currency
co = int(input("What do you have left in pesos? "))
pe = int(input("What do you have left in soles? "))
br = int(input("What do you have left in reais? "))

co1 = 0.00025 * co
pe1 = 0.265379 * pe
br1 = 0.20 * br

print(co1 + pe1 + br1)


