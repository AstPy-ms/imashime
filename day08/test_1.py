""" 課題1: 文字列と辞書のメソッド """
# 授業で紹介した文字列のメソッド（9種類）と辞書のメソッド(9種類)を
# それぞれ実行し, その結果をprintで出力して動作を確認せよ。
s = "Today is Friday."
month = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5}

for i in month.keys():
  print(i, end=" ")

for i in month.values():
  print(i, end=" ")
