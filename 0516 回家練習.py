1.有一直三角形, 若已知其較短兩邊長為10cm, 8cm, 則另一邊為幾公分?
(請使用 math.pow(x,y) 與 math.sqrt(x))

import math

a = 8
b = 10
c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))

print(f"另一邊的長度為 {c:.2f} 公分")



2.有一直三角形, 若已知其兩邊長為10cm, 8cm, 則另一邊可能為幾公分?

import math

a = 8
b = 10
c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))

print(f"另一邊的長度為 {c:.2f} 公分")