請寫一個 is_odd(x) 函式，檢查輸入的參數 x 是不是奇數。
如果 x 是奇數則回傳 Ture；若 x 不是奇數則回傳 False。

def is_odd(x):
    if x % 2 == 1:
        return True
    else:
        return False

print(is_odd(33))
print(is_odd(546))


def is_odd(x):
    return x % 2 == 1

print(is_odd(33))
print(is_odd(546))
