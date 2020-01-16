#練習課題 2
#数が２または３で割る可能かどうかを判断するプログラムを作成してくだい．

x = (int)(input('x: '))
#2で割る可能
if x % 2 == 0:
    print('Divisible by 2') 
#2で割る不可能，3で割る可能
elif  x % 3 == 0:
    print('Not by 2')       
    print('But by 3')
#2でも3でも割る不可能
else:
    print('Not by 2 and by 3')  
