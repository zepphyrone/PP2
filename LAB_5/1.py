import re

user_input = input()
result = re.search(r'ab*', user_input)
print(result)