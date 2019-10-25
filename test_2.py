"課題 2"

#ニュートン法を用いて，x**2 + ax + b = 0 の方程式を解くプログラムを作成してください
# a, b, gosaはfloat型として入力

# hint:
# 二次関数: f(x) = x**2 + ax + b
# 頂点: f'(xs) = 0, xs = -a/2
# f(xs)によって解が存在するか，一個か，二個か判断
# 解が一個なら，頂点がⅹ軸と接触し，頂点 xs が解となる　
# 解が二個なら，頂点が x軸の下となり，x0の初期値＝ xs + gosa として頂点の右側にある解，そしてx0の初期値＝ xs - gosaとして頂点の左側にある解を探す

# gosa = 0.1, (a = 2, b = 3), (a=2, b= 1), (a=2, b= -3)で入力し，答えが正しいかどうを確認してみてください．

# f'(x) = 2x + a 

a = float(input("y = x² + ax + b の a を入れてね: "))
b = float(input("y = x² + ax + b の b を入れてね: "))
gosa = float(input("誤差の許容範囲はいくつにする？: "))

apex = (-a/2.0)*(-a/2.0) + a*(-a/2.0) + b

# 判別式を使う
num = 0
answer = []
d = a*a - 4*b

# 判別式 D の値の場合分け

if(d > 0):
  num = 2
elif(d < 0):
  answer.append("解なし")
else:
  x_apex = -a/2.0
  answer.append(x_apex)

# counter の初期化
counter = 0
  
x0 = apex + gosa
x1 = x0 - (x0**2 + a * x0 + b)/(2*x0 + a)

while abs(x1**2 + a * x1 + b) >= gosa:
  x0 = x1
  x1 = x0 - (x0**2 + a * x0 + b)/(2*x0 + a)
  counter += 1
  
if num == 2:
  answer.append(x1)
  

x0 = apex - gosa
x1 = x0 - (x0**2 + a * x0 + b)/(2*x0 + a)

while abs(x1**2 + a * x1 + b) <= gosa:
  x0 = x1
  x1 = x0 - (x0**2 + a * x0 + b)/(2*x0 + a)
  counter += 1
  
if num == 2:
  answer.append(x1)
  


'''
kaisu = 0
while abs(x1**3 -v) >= gosa:
    x0 = x1
    x1 = x0 - (x0**3 - v) / (3 * x0**2)
    kaisu += 1
'''
  
print(answer,counter)




