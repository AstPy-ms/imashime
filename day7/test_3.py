"""課題2"""
'''
# removeDupsを動かし挙動を確認せよ。また、正しく動くよう変更せよ。
def removeDups(L1, L2):
    for e1 in L1:
        if e1 in L2:
            L1.remove(e1)
L1 = [1, 2, 3, 4] 
L2 = [1, 2, 5, 6]
removeDups(L1, L2)
# この時のL1の中がどのようになっているか確認せよ
print(L1)
'''

#　　L1からL2と重複する要素を削除する正しいプログラムをremoveDups2として作成せよ
def removeDups2(L1, L2): 
    
    L1.sort() # ダミー行です
    for i in L1:
        if i in L2:
            L1.remove(i)
    print(L1)
                
removeDups2(L1, L2)


'''
実行結果

[2, 3, 4]
[3, 4]
'''
