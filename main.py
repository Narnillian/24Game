import random
import time
try:
  #if replit is not available, do not try to log
  from replit import db
  has_replitdb = True
except:
  has_replitdb = False

def add(num1, num2):
  return num1+num2

def subtract(num1, num2):
  return num1-num2

def multiply(num1, num2):
  return num1*num2

def divide(num1, num2):
  return num1/num2


def find24(num1, num2, num3, num4):
  base_list = [num1, num2, num3, num4]
  print(f"Input: {base_list}")
  combos = []

  iterations=0
  #randomize the set over and over until I have the correct number of variations  
  while True:
    iterations+=1
    print(f"Number shuffler iterations: {iterations}")
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
      if has_replitdb:
        db[f"shuffler_ iterations{time.time()}"] = iterations
      break
  
  print(combos)
  
  iterations = 0
  while True:
    iterations+=1
    print(f"Operator shuffler iterations: {iterations}")
    unique = True
    operators = [add,subtract,multiply,divide]
    this_set = []
    random.shuffle(this_set)
    for i in combos:
      if this_set == i:
        unique = False
    if unique:
      combos.append(this_set)
    print(f"len(combos): {len(combos)}")
    if len(combos) == 256:
      if has_replitdb:
        db[f"shuffler_ operator_iterations{time.time()}"] = iterations
      break


print(time.time())
find24(1, 3, 5, 7)
print("The file ran!")
print(time.time())
