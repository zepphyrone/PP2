import math
r = int(input())
def sphere_volume(radius):
    volume = 4/3 * math.pi * r ** 3
    print(volume)

sphere_volume(r)  