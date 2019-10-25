#練習課題 6

# *の並び方を以下のように出力する
# *
# **
# ***
# ****

'''
x = (int)(input('縦又は横の数: '))
s =''
for i in range(0, x):
    for j in range(0, x):
        if j <= i:
            s = s + '*'
    print(s)
    s = ''

'''

# *の並び方を以下のように出力してください
# *
#  *
#   *
#    *

x = (int)(input('縦又は横の数: '))

for i in range(x):
  
  s = ""
  
  for j in range(x):
    
    if i != j:
      s = s + " "
    else:
      s = s + "*"
      
  print(s)
