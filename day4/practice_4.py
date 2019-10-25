""" 確認問題 3 """

def f(x): #仮引数の名前をx
    y = 1
    x = x + y
    print('f(x)の中 x = ', x)
    return x

x = 3
y = 2
z = f(x) #xの値を実引数とする
print('z = ', z)
print('y = ', y)
print('x = ', x)
