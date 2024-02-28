import re

user_input = input()
result = re.sub("[a-zA-Z][^A-Z]*", " ", user_input)
print(result)