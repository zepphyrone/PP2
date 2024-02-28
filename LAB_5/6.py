import re

user_input = input()
result = re.sub("[ ,.]",":", user_input)
print(result)