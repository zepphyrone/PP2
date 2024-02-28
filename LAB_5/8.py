import re

user_input = input()
result = re.findall("[a-zA-Z][^A-Z]*", user_input)
print(result)