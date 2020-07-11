''' 確認スクリプト 7'''

def findZeroSum (a, b, c) :
    for d1 in [a, -a] :
        for d2 in [b, -b] :
            for d3 in [c, -c] :
                s = d1 + d2 + d3
                if s == 0 :
                     raise ValueError(f"A zero sum set is {d1} {d2}, {d3}")
try :
    findZeroSum(1, 2, 3)
except ValueError as errMsg :
    print(errMsg)
else :
    print("Zero sum set does not exist")
