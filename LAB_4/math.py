# 1
import math
d = int(input())
r = math.radians(d)
print(r)

# 2 
a, b, h = map(int, input().split())
area = ((a+b) / 2) * h
print(area)

# 3
a, b = map(int, input().split())
area = int((pow(b , 2) *a) / (4 * math.tan((math.pi / a))))
print(area)

# 4
a, b = map(int, input().split())
area = a * b
print(float(area))