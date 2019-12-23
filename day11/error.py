''' 確認スクリプト 9'''

n = 10
data = [i*i for i in range(n)]

def getVal(i) :
    assert 0 <= i <= n-1,f"Out of range:i={i}"
    assert type(i) == int,f"Typeerror:type={type(i)}"
    return data[i]

try:
  print(getVal(7.8),getVal(11))
except AssertionError as msg:
  print(f"AssertionError is occured:{msg}")
