"""復習課題1: ファイルのおまじないの正体"""

file_list1 = []
file_list2 = []
f = open('./user_list.csv','r')
for line in f:    
    file_list1 = line[:-1]
    file_list2 = line
f.close()
print(file_list2)
print(file_list1)
print(file_list1)
print(file_list2)
print(file_list1)
print(file_list2)
print(len(file_list1))
print(len(file_list2))

'''
実行結果

河原 ヒカル,かわはら ひかる,女,77,千葉県,298-0012
河原 ヒカル,かわはら ひかる,女,77,千葉県,298-001
河原 ヒカル,かわはら ひかる,女,77,千葉県,298-001
河原 ヒカル,かわはら ひかる,女,77,千葉県,298-0012
河原 ヒカル,かわはら ひかる,女,77,千葉県,298-001
河原 ヒカル,かわはら ひかる,女,77,千葉県,298-0012
32
33

'''
