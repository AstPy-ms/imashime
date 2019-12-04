# 途中までしかやってないっす。善処します。

""" 自主課題: より複雑な情報検索と辞書の活用 """
# user_listをロードしてリストにして
# そこから出身地と名前で辞書を作成、名前はリスト表現を使用
# 指定した県が出身地の人の人数と名前を書き出すプログラムをかく
# 最後に県名を指定するとその県出身の人の名前と人数を答えるようにする

import io
from google.colab import drive
drive.mount('/content/drive')

# ファイル読み込み -> リストに書き出し
# Google Colaboratory用に書き直してます
with open("/content/drive/My Drive/fortmu/プログラミング基礎演習/user_list.csv","r+") as f:

  data=[]
  for line in f:    
    data.append(line[:-1])

# 各要素を更にカンマごとに分ける
data_split=[]
for s in data:
    data_split.append(s.split(","))
# print(data_split)

# リスト内に含まれる県名をすべて抽出する
prefectures = []
for i in range(1, len(data_split)):
  prefectures.append(data_split[i][4])
print(prefectures)

# リスト内から重複を消して県名リストを完成させる
sorted_prefectures = set(prefectures)
print(sorted_prefectures)

# 各県毎の出身者名リストを辞書で作成する


#  県を指定すると名前を返す


#  県を指定すると名前と人数を返す（人名をリスト形式でなく表示できるとなおよし）
#  出力例： 石川県出身の人は石野 まさみ, 尾形 由宇の合計2名です。


