a = input()

upper = 0
lower = 0

for i in range(len(a)):
    if a[i] >= 'a' and a[i] <= 'z':
        lower += 1
    else:
        upper += 1

print("number of upper case letters:", upper)
print("number of lower case letters:", lower)