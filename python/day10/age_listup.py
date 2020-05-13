L = [('Alice', 17), ('Bob', 11), ('Charlie', 3), ('Dave', 25), ('Ed', 20)]

def filter(L, age):
  name = []
  for i in L:
    if i[1] >= age:
      name.append(i[0])
  return name

print(filter(L, 25))
