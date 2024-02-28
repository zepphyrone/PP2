import re

user_input = input()
result = re.findall(r'[A-Z][a-z]+', user_input)
print(result)