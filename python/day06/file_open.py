"確認問題 2"

f = open('dummy.csv', 'r')

for line in f:
    print(line[:-1])
    
f.close()
