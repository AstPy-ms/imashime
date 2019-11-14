""" 確認問題１ """
# x1からx4およびtest1, 2それぞれの型を出力し， タプルの特徴を確認せよ

x1 = '10.0'
x2 = 10.0
x3 = 10
x4 = (x1, x2, x3)
test1 = (5)
test2 = (5,)

print(type(test2))

# 型を調べる関数はtype() 
# 例） print(type(x1))

'''
実行結果

<class 'tuple'>
'''
