''' 課題 ： try-except ブロックを用いて，以下の仕様にあった関数 sumDigits を実装せよ '''

import re

def sumDigits(s) :
    """ s を文字列とする
        s の中の数字の合計を返す
        例えば， s が 'a3b3c' ならば 5 を返す． 
        'a23bc3' ならば 8 を返す """

    answer = 0
    
    for i in range(len(s)):
      if s[i].isdigit() == True:
        answer += int(s[i])

    return answer

print(sumDigits('a3b3c'), sumDigits('a23bc3'))
