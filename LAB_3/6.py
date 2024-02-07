str = input()
def reverse_str(str2):
    words = str.split()
    for i in range(len(words) - 1, -1, -1):
        print(words[i], end=" ")
reverse_str(str)