# 1
def generaator(n):
    for i in range(n+1):
        yield i**2


for i in generaator(int(input())):
    print(i)

# 2
def generatoorss(n):
    for i in range(n):  
        if i % 2 == 0:
            yield i
        elif n % 2 == 0 and i == n - 1:
            yield ''
        else:
            yield ','


for i in generatoorss(int(input())):
    print(i ,end='')

# 3 
def generattors(n):
    for i in range(n):  
        if i % 3 == 0 and i % 4 == 0:
            yield i


for i in generattors(int(input())):
    print(i)
    
# 4
def generatoors(n ,k):
    for i in range(n,k):  
        yield i ** 2


for i in generatoors(int(input()),int(input())):
    print(i)

# 5
def geneatoors(n):
    i = 0
    while n > i:
        yield n
        n = n-1

for i in geneatoors(int(input())):
    print(i)