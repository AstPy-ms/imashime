# 課題2

x = float(input())

if x < 0:
  x = -1 * x
  
error_range = 0.01
step = gosa ** 3
count = 0
answer = 0.0
  
while abs(answer ** 3 - x) >= error_range and answer <= x:
  answer += step
  count += 1
    
print("試行回数=", count)
  
if abs(answer ** 3 - x) >= error_range:
    print("誤差でかい!")
else:
    print(answer)
    

## 考察

'''
今回は総当り法を用いているので、入力された数の絶対値が大き狩れば大きいほどかかる時間が伸びるのではと考えられる。
さらにいくつかの`error_range`を試したが、それを小さくすればするほどかかる時間が伸びた。
このことから、誤差の許容範囲を狭くするとかかる時間がかかることがわかった。これは、総当り法でもその他のアルゴリズムでも同じだと考えている。

これらのことから、総当り法はアルゴリズムだけでは簡単に見えるが、数が極端に大きかったり小さかったりする場合には向かないことがわかった。

'''


