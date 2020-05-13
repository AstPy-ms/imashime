"課題 1"

#入力した値 n まですべての素数を出力してください
# n = 9, 素数 = 2, 3, 5, 7
# n = 19, 素数 = 2, 3, 5, 7, 11, 13, 17, 19

n = int(input("データください: ")) #integer型として入力

# hint: i を 2 から n まで，j を 2から i-1 まで，段々上げて，iをあるｊの値で割る可能なら素数ではない．

for i in range(2, n+1):  
  flg = 0
  for j in range(2, i):
    if(i % j == 0):
      flg += 1
  if flg == 0:
    print(i)


