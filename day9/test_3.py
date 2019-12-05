# 第０項からスタートします。

def Tribonacci(num):

  global count
  count += 1

  if num == 0:
    return 0
  elif num == 1:
    return 0
  elif num == 2:
    return 1
  else:
    return Tribonacci(num-1) + Tribonacci(num-2) + Tribonacci(num-3)

num = int(input("第何項までのトリボナッチ数列が欲しいですか？: "))
count = 0
print(f'第{num}項の数は{Tribonacci(num)}で、{count}回再帰をしました。')
