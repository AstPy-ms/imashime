''' 課題： 次の仕様を満す関数を実装せよ'''

def findAnEven(L) :
    ''' L を int型の要素を持つリストとする
        L に最初に現れる偶数を返す
        L が偶数を含まなければ ValueError を引き起こす '''

    for i in L:
      if i % 2 == 0:
        return i
    raise ValueError(L)
    
try :
    even = findAnEven([1,2,5])
    even = findAnEven([1,3,5])
except ValueError as errL:
    print("Canot find even in ", errL)
print(even)
