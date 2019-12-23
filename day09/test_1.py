def copy(L1, L2):
  """L1とL2をリストとする．L2をL1のコピーに更新する"""
  while len(L2) > 0:
    #L2から全ての要素を削除する
    L2.pop()
    #L2の最後の要素を削除
    for e in L1:
      #L2にL1の要素を追加
      L2.append(e)
  print(L1, L2)

L1 = [1,2,3]
L2 = [4,5]
copy(L1,L2)

L1 = [1,2,3]
L2 = L1[:]
