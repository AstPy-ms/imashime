"課題 3"
#weather.csvを読み込んで，weather2.csvに書き込みなさい

f1 = open("weather.csv","r")
f2 = open("weather2.csv","w+")

for line in f1:
    f2.write(line)
    
f1.close()
f2.close()
