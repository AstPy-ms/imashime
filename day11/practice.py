''' 確認スクリプト 6'''

while True :
    ''' 確認スクリプト 5 の 1行目'''
    val = int(input('整数を入力して下さい: '))
    try : 
        val = int(val)
        ''' 確認スクリプト 5 の 2行目'''
        print('入力した整数の2乗は', val**2,'です')
        break
    except Error :
        print(val, ' は整数ではありません')

