""" 練習課題2: map関数1 """
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in map(fib, [2, 6, 4]):
    print(i)

""" 練習課題3: map関数2（多重代入文） """
L1 = [1, 28, 36]
L2 = [2, 57, 9]
for i in map(min, L1, L2):
    print(i)
