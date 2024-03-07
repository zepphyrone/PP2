def palindrome(a):
    reverse = a[::-1]
    if a == reverse:
        print("its palindrome")
    else:
        print("its not")

a = input()
palindrome(a)
    