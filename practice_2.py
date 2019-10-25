#練習課題 2

#二分法を用いて，数の立方根の近似値を探すプログラムを作成してください

# gosa = 0.01, v = -27，27と28で入力し，計算が正しいかどうか確認
# gosa = 0.01, v = 27と28で入力して，探す回数と結果を確認

# 練習課題１と比較して，二分法の計算効率について考察してください

# 求めたい元のデータ : v
# xmは中点
# x > 0のときで考える

v = float(input('v:　'))
gosa = float(input('gosa:　'))
vp = v

if v < 0:
    vp = -v #まずブラス方向として解を探す
    
x1 = 0.0
x2 = vp
xm = (x1 + x2) / 2.0

kaisu = 0

#○○に記入してください
while abs(xm**3 -vp) >= gosa:
    if ((xm**3 - vp) < 0):
        x1 = xm
    else:
        x2 = xm
    xm = (x1 + x2)/2.0
    kaisu += 1
    
if v < 0:
    xm = -xm
    
print('探す回数 =',kaisu)
print('立方根の近似値は',xm)

#考察
#

