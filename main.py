import random
import time
from replit import db

def find24(num1, num2, num3, num4):
  base_list = [num1, num2, num3, num4]
  print(f"Input: {base_list}")
  combos = []

  iterations=0
  #randomize the set over and over until I have the correct number of variations  
  while True:
    iterations+=1
    print(f"Iterations: {iterations}")
    unique = True
    this_set = [num1, num2, num3, num4]
    random.shuffle(this_set)
    for i in combos:
      if this_set == i:
        unique = False
    if unique:
      combos.append(this_set)
    print(f"len(combos): {len(combos)}")
    if len(combos) == 24:
      db[f"shuffler_ iterations{time.time()}"] = iterations
      break
  
  print(combos)


print(time.time())
find24(1, 3, 5, 7)
print("The file ran!")