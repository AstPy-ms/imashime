"""　練習課題1: オブジェクトとしての関数　"""

# 再帰を使って階乗を取る
def factR(n):
    if n == 1:
        return n
    else:
        return n * factR(n-1)

# 絶対値や整数値をとる
# fにはabsやintが入る
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])        
        
count = 0
L = [1, -2, 3.33]
print('L = ', L)
print('Apply abs to each element of ', L)
applyToEach(L, abs)
print('L = ', L)
print('Apply int to each element of ', L)
applyToEach(L, int)
print('L = ', L)
# factRに適用する場合をかけ
print('Apply factorial to each element of ', L)
'''
for i in range(len(L)):
  L[i] = factR(L[i])
'''
applyToEach(L, factR)
print('L = ', L)
