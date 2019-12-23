import io
from google.colab import drive
drive.mount('/content/drive')


def sqrt(x, epsilon):  #x – epsilon <= result*result <= x + epsilonを満たすresultを返す

  step = epsilon ** 2
  answer = 0.0
  
  while abs(answer ** 2 - x) >= epsilon and answer <= x:
    answer += step
    
  #print("試行回数=", count)
  
  if abs(answer ** 2 - x) >= epsilon:
    pass
    #print("誤差でかい")
  else:
    return answer

# ファイル読み込み -> リストに書き出し
# Google Colaboratory用に書き直してます
with open("/content/drive/My Drive/fortmu/プログラミング基礎演習/testdata.txt","r+") as f:

  for line in f:
    L=line.split()
    x, epsilon = float(L[0]), float(L[1])
    print('x =', x, 'epsilon =', epsilon, 'result =', sqrt(x, epsilon))
