印星星(三)：

def print_pattern(n):
    for i in range(1, n+1, 2):
        print(" " * ((n - i) // 2) + "*" * i + " " * ((n - i) // 2))
    for i in range(n-2, 0, -2):
        print(" " * ((n - i) // 2) + "*" * i + " " * ((n - i) // 2))

print_pattern(5)