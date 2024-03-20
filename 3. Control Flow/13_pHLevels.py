# 13. pH Levels
import random
ph = random.randint(0, 14)
if ph > 7:
  print("Basic")
if ph < 7:
  print("Acidic")
else:
  print("Neutral")