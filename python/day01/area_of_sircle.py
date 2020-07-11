"""課題2"""
#入力が半径の値で，円の面積と円周を計算して出力するプログラムを作成しよう．
#入力: 半径の値（float型）
#出力: 円の面積＝半径ｘ半径ｘ3.14 と　円周＝2x半径ｘ3.14

radius = (int)(input("radius is:"))

cir = 2 * radius * 3.14
area = radius * radius * 3.14

print("円周は" + str(cir) + "で、面積は" + str(area) + "です。")

print(f'円周は{cir}で、面積は{area}です。')
  
print("円周は{}で、面積は{}です。".format(cir, area))