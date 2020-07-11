"""確認問題3: """
# 最小公約数および最大公約数を求める関数findExtremeDivisorsを使って多重代入を試せ

def findExtremeDivisors(n1, n2):
    maxVal , minVal = None, None
    for i in range(2, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            if minVal == None:
                minVal = i
            maxVal = i
    return (minVal, maxVal)

minD, maxD = findExtremeDivisors(100, 200)    
D = findExtremeDivisors(100, 200)   

print(minD, maxD, D, type(minD), type(maxD), type(D))
# minD, maxD, Dそれぞれの中身と型を調べよ

'''
実行結果

2 100 (2, 100) <class 'int'> <class 'int'> <class 'tuple'>

'''
