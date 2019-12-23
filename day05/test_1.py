""" 課題 1 """

def f(x):
    x = x + 1
    return x

def g(x):
    x = x + 2
    return x

def h(x):
    x = x * 3
    return x

x = 1
print('f(x):', f(x))
print('g(x):', g(x))
print('g(f(x))', g(f(x)))

# h(g(f(x))) と　f(g(h(x))) の結果を比較しなさい．

print('h(g(f(x)))', h(g(f(x))))
print('f(g(h(x)))', f(g(h(x))))

'''
実行結果

f(x): 2
g(x): 3
g(f(x)) 4
h(g(f(x))) 12
f(g(h(x))) 6
'''
