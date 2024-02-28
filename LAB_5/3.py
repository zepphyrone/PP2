import re

user_input = input()
result = re.findall(r'[a-z]+_[a-z]+', user_input)
print(result)