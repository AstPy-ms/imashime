""" 復習問題 """
#TODO: 商品名と支払額をinput関数で得る
#TODO: 支払額と商品額の差額をおつりとして表示する．
#Coffee 150円，Tea 160円，Orange 100円，Cola 120円

#ここに自分のコードを記述すること

product = ["Coffee", "Tea", "Orange", "Cola"]
price   = [150, 160, 100, 120]

num = []

money = int(input("所持金はいくらですか (例: 2000): "))

print("")

print("当店は/",end="")

for i in range(len(product)):
    print(product[i], price[i], end="円/")
    
print("を販売しています")

print("")
    
sum = 0

for i in range(len(product)):
    
    tmp = int(input(f'{product[i]} はいくつ買いますか？(例: 1): '))
    sum += tmp * price[i]
    print("")
    
print(f'合計は{sum}円で、おつりは{money - sum}円です。')
print("ありがとうございました。")
