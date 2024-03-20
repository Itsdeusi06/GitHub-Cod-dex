co = int(input("What do you have left in pesos? "))
pe = int(input("What do you have left in soles? "))
br = int(input("What do you have left in reais? "))

co1 = 0.00025 * co
pe1 = 0.265379 * pe
br1 = 0.20 * br

print(co1 + pe1 + br1)


