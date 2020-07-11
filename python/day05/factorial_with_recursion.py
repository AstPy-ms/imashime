""" 確認問題 4 """
def factorial(n):
    if n == 1:
        return n #ここが終了条件
    else:
        return n * factorial(n - 1)
    
print(factorial(5))

# 再帰をPythonでやるのか...
