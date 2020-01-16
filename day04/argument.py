""" 確認問題 1"""
#引数を位置で指定する場合とキーワードで指定する場合でどのように結果が変わるのか確認しなさい．

def f(first, second, third):
    print(f'first = {first}, second = {second}, third = {third}')

#ここに上記のf関数を引数を位置で指定するコードを記述すること
f(3, 2, 1)

#ここに上記のf関数をキーワードで指定するコードを記述すること

f(third = 3, second = 2, first = 1)
