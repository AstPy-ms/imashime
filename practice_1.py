#練習課題 1

#総当たりを用いて，数の立方根の近似値を探すプログラムを作成してください

# gosa = 0.01, step = 0.001，そしてv = -27，27と28で入力し，計算が正しいかどうか確認
# gosa = 0.01, step = 1，そしてv = 27と28で入力して，探す回数と結果を確認
# gosa = 0.01, setp = 0.00001, そしてv = 27と28で入力して，探す回数と結果を確認

# 以上の結果について考察してください

v = float(input('v:　'))
gosa = float(input('gosa:　'))
step = float(input('step:　'))
if v < 0:
    step = -step #マイナス方向で答えを探す

kaisu = 0
x = 0.0 #探す回答

#ここにコードを書いてください
# while x**3 が　vに近づかない　および x がｖより小さい
#答えを探す，計算回数をカウントする

while abs(x**3 - v) >= gosa and abs(x) <= abs(v):
  x += step
  kaisu += 1

print('探す回数 =',kaisu)

#○○に記入してください
if abs(x**3 - v) >= gosa:
    print('誤差が大きくて十分近い答えはなかった．誤差＝', abs(x**3 - v))
else:
    print('立方根の近似値は',x)
    

#考察
#
#

