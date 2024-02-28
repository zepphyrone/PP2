import re

def camel_snake(user_input):
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', user_input).lower()


user_input = input()
converted = camel_snake(user_input)
