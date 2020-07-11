""" 課題 2 """
#１）再帰を用いてフィボナッチ数を求めなさい．
#２）このCellをコピ－し，新しく「課題3」として，フィボナッチ数を求める時の再帰呼び出しが何回行われているのかを調べなさい

def Fibonacci(num):

  global count
  count += 1

  if num == 0:
    return 0
  elif num == 1:
    return 1
  else:
    return Fibonacci(num-1) + Fibonacci(num-2)

num = int(input("第何項までのフィボナッチ数列が欲しいですか？: "))
count = 0
print(f'第{num}項の数は{Fibonacci(num)}で、{count}回再帰をしました。')

'''
実行結果

第何項までのフィボナッチ数列が欲しいですか？: 10
第10項の数は55で、177回再帰をしました。
'''
