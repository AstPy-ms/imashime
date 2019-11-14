""" 練習問題４　"""
# リストの可変性について理解せよ
weather = ['晴れ', '曇り', '雨']
rains = ['時雨', 'みぞれ', 'あられ', '霧']

weathers = [weather, rains]
weathers1 = [['晴れ', '曇り', '雨'], ['時雨', 'みぞれ', 'あられ', '霧']]

print(weathers)
print(weathers1)
print(weathers == weathers1)
print(id(weathers), id(weathers1))

rains.append('大雨')
print(weathers)
print(weathers1)
print(weathers == weathers1)

'''
実行結果

[['晴れ', '曇り', '雨'], ['時雨', 'みぞれ', 'あられ', '霧']]
[['晴れ', '曇り', '雨'], ['時雨', 'みぞれ', 'あられ', '霧']]
True
140452792914760 140452801723656
[['晴れ', '曇り', '雨'], ['時雨', 'みぞれ', 'あられ', '霧', '大雨']]
[['晴れ', '曇り', '雨'], ['時雨', 'みぞれ', 'あられ', '霧']]
False
'''
