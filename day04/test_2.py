""" 課題 2 """
# -*- coding: utf-8 -*-
# TODO: キーワードと文を入力とし，文の中にキーワードが含まれていれば True ，含まれていなければ False を返す関数を記述しなさい．
# TODO: 実際に関数を呼び出すコードを記述し，動作を確認しなさい．

#ここに自分のコードを記述すること．

def judge(key, sentence):
    
    judge = key in sentence
    print(judge)

def main():

    keyword = input("キーワードはなんですか？: ")
    sentence = input("文はなんですか？: ")

    judge(keyword, sentence)
    
if __name__ == "__main__" :
    main()
