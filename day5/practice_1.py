#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 復習問題 """

import datetime

#old関数を完成させなさい．
def old(today , birthday):
    print('今年で %d 歳ですね' %(today.year - birthday.year))
    
def remainDay(birthday, today):
    a = datetime.date(today.year, birthday.month, birthday.day)
    b = datetime.date(today.year, today.month, today.day)
    print('誕生日まで後 %d 日' %(a-b).days)

#birthday = "2000/9/22"
birthday = input('生年月日を入力してください．')
birthday = datetime.datetime.strptime(birthday, '%Y/%m/%d') #入力された文字列をdatetime型に変換
today = datetime.datetime.now() #今日の日付（と現在時刻）を取得

print('知りたい項目を入力してください．')
print('1: 年齢')
print('2: 誕生日までの日数')
select = input('---> ')

if(select == "1"):
    #ここにold()を呼び出すコードを記述しなさい．0
    old(today, birthday)
elif(select == "2"):
    remainDay(birthday, today)
else:
    print("入力された番号には対応していません．")

