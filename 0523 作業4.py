請寫一個函式 compare_value(x, y)，比較參數 x 和 y 的大小，
若 x 大於 y 則回傳 1；若 x 等於 y 則回傳 0；若 x 小於 y 則回傳 -1。

def compare_value(x,y): 
    if x > y:
        return 1 
    elif x == y: 
        return 0
    else:
        return -1

print(compare_value(3,5))
print(compare_value(5,5))
print(compare_value(5,3))
