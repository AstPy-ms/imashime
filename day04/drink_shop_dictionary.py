""" 課題 3 """
#復習問題を関数を使って書き直しなさい．


things = {"coffee":150, "tea":160, "orange":100, "cola":120}


def change(item, money):

    for key, price in things.items():
        price = int(price)
        if key == item:
            if price <= money:
                print(f'{item}は{price}円なので、おつりは{money - price}円です。')
            else:
                print("所持金が足りません。")
                

def main():

    # 販売しているものの確認
    print("当店は、", end="")
    for item, price in things.items():
        print(f'{item}:{price}円、', end="")
    print("を販売しています。")

    # 何をいくつ買うか確認する
    tmp = str(input("何を買いますか？またいくら払いますか？(例: coffee,1000)  "))
    
    product = tmp.split(",")
    item = product[0]
    money = int(product[1])

    change(item, money)

if __name__ == "__main__":

    main()








