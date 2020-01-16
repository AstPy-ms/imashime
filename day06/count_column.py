"課題 2"
#dummy.csvの行数をカウントしなさい．
count = -1
f = open('dummy.csv', 'r+')

for line in f:
    count += 1

print(count)
f.close()
