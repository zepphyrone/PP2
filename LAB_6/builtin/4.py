import time
import math

def root(n, msec):
    time.sleep(msec / 1000)
    result = math.sqrt(n)
    print(result)

n = int(input())
msec = int(input())
root(n, msec)