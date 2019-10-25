""" 確認問題 2""" 


def greeting(name, text):
    """
    Input: name　名前，text　挨拶文，count 繰返し回数（指定されなければデフォルト値）
    """
    for i in range(count):
        print(f' {name}さん、{text}！')

#上記の関数を回数を３回に指定して呼び出すコードを記述しなさい．
#上記の関数を呼び出す際にCountを指定しなかった場合にどのような動作をするのか，コードを記述して確認しなさい．

name = input("お名前は？: ")
greet = input("したい挨拶は？: ")
count = int(input("何回挨拶しますか？"))

greeting(name, greet)
