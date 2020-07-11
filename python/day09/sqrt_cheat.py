import io
from google.colab import drive
drive.mount('/content/drive')


def sqrt(x, epsilon):
    return x**(0.5)

# ファイル読み込み -> リストに書き出し
# Google Colaboratory用に書き直してます
with open("/content/drive/My Drive/fortmu/プログラミング基礎演習/testdata.txt","r+") as f:

  for line in f:
    L=line.split()
    x, epsilon = float(L[0]), float(L[1])
    print('x =', x, 'epsilon =', epsilon, 'result =', sqrt(x, epsilon))
