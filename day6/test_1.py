"課題 1"
#フィボナッチ数列の結果をファイルに書き出しなさい．

def Fibonacci(num):

  global count
  count += 1

  if num == 0:
    return 0
  elif num == 1:
    return 1
  else:
    return Fibonacci(num-1) + Fibonacci(num-2)


f = open("test.csv", "a+")
# with open('~/Downloads/test.csv') as f:

num = int(input("第何項までのフィボナッチ数列が欲しいですか？: "))
count = 0

for i in range(num):
    result = f'第{i}項の数は{Fibonacci(i)}で、{count}回再帰をしました。'
    f.write(result + "\n")

"""
for line in f:
    print(line)
"""

f.close()

