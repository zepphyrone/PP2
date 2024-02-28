import re

user_input = input()
result = re.findall(r'a(bb|bbb)$', user_input)
print(result)