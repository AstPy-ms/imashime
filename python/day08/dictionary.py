""" 練習課題5: 辞書（キーと値のペアに注意） """
monthNumbers = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 1: 'Jan', 2 : 'Feb', 3:'Mar', 4:'Apr', 5:'May', 10: 'Oct'}

print('The third month is  ' + monthNumbers[3])
dist = monthNumbers['Apr'] - monthNumbers['Jan']
# dist = monthNumbers[4] - monthNumbers[1] はNG
print('Apr and Jan are ', dist, 'months apart')

keys = []
for e in monthNumbers:
    keys.append(str(e))
print(keys)
keys.sort()
print(keys)
