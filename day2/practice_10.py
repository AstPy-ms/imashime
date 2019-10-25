# 練習課題10

x = float(input())

if x < 0:
  print("正の値をいれてください")
  
else:
  
  gosa = 0.01
  step = gosa ** 2
  count = 0
  answer = 0.0
  
  while abs(answer ** 2 - x) >= gosa and answer <= x:
    answer += step
    count += 1
    
  print("試行回数=", count)
  
  if abs(answer ** 2 - x) >= gosa:
    print("誤差でかい")
  else:
    print(answer)
    

