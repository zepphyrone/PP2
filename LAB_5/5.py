import re

user_input = input()
result = re.findall(r'a.*b$', user_input)
print(result)