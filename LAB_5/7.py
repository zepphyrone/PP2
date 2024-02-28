import re

def snake_camel(user_input):
    return re.sub(r'_([a-z])', str.upper, user_input)


user_input = input()
converted = snake_camel(user_input)
print(converted)