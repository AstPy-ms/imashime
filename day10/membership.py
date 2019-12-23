def membership(L1,L2,e):

  answer = []
  if e in L1:
    answer.append(1)
  if e in L2:
    answer.append(2)
  return tuple(answer)

L1 = [1, 2, 3, 5, 7]
L2 = [2, 3, 4, 6]
print(membership(L1,L2,5))
