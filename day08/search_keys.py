"""　課題2： リストとタプルを使った辞書生成　"""
# 県名(prefectures)をキー、各県の人口(populations)を値とした辞書を作成せよ
# 以下の県名と人口の順番は対応していることとする
# 辞書をprintで出力し対応がとれていることを示すこと。
prefectures = ('鹿児島県', '山形県', '茨城県', '大阪府', '北海道')
populations = [1612800, 1089806, 2882943, 8824566,  5285430]

dic = {}

# ここにprefecturesをキーとした辞書を作成するプログラムを書け
for i in range(len(prefectures)):
  dic[prefectures[i]] = populations[i]

# 自分で作った辞書の名前を入れて型と中身を表示させる
# ___は消すこと。_の数と実際の文字数は対応しない
print(type(dic))
print(dic)
