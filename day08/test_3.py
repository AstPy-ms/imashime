""" 課題3: 下手くそな翻訳機（英語とフランス語の翻訳機） """
# プログラムの一部が___で消されているのでそこに必要なものを追加して翻訳機を完成させよ。
# _の数と実際の文字数は対応しない

# 辞書の定義
EtoF= {'bread': 'pain', 'wine':'vin', 'with':'avec', 'I':'Je', 'eat':'mange', 'drink':'bois', 'John':'Jean', 'friends':'amis', 'and':'et', 'of':'du', 'red':'rouge'}
FtoE= {'pain':'bread', 'vin':'wine', 'avec':'with', 'Je':'I', 'mange':'eat', 'bois':'drink', 'Jean':'John', 'amis':'friends', 'et':'and', 'du':'of', 'rouge':'red'}
dicts = {'English to French': EtoF, 'French to English': FtoE}

# 入力された単語wordが辞書に含まれる場合はその変換後の単語を返す
# 含まれない場合は含まれていないことがわかるよう"をつけて返す
def translateWord(word, dictionary):    
    if word in dictionary:
        return dictionary[word]
    elif word != "":
        return '"' + word + '"'
    else:
        return word

# 入力されたフレーズと辞書から変換した単語をtranslationに追加していき翻訳されたフレーズを返す
def translate(phrase, dicts, direction):
    UCLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LCLetters = 'abcdefghijklmnopqrstuvwxyz'
    letters = UCLetters + LCLetters
    dictionary = dicts[direction]
    #print(dictionary)
    translation = ''
    word = ''
    comma_flag = 0
    
    # 一文字ずつ処理、スペースが来たら翻訳する
    '''
    for c in phrase:
        #print(c)
        #split()的なことをやる
        if c in letters:
            word = word + c
        else:
            #print(word)
            translation = dictionary[word]
    '''
    # 苦渋の選択
    sentence = phrase.split()
    
    for i in sentence:
        if "," in i:
            i = i[:-1]
            comma_flag = 1
        if comma_flag == 1:
            translation = translation + translateWord(i, dictionary) + "," + " "
            comma_flag = 0
        else:
            translation = translation + translateWord(i, dictionary) + " "
    return translation

# 英語からフランス語
print(translate('I drink good red wine, and eat bread.', dicts, 'English to French'))

# フランス語から英語
#print(translate('Je bois du vin rouge.', dicts, ___)) 
