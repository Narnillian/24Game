from replit import db

counter=0
iteration_counter_keys = db.prefix("shuffler_ iterations")
for i in iteration_counter_keys:
  print(i,end="")
  counter+=1

  spaces=73-len(i)-len(str(db[i]))
  for j in range(spaces):
    print(" ",end="")
  print(db[i])

print(f"There are {counter} keys with the prefix |shuffler_ iterations|")
