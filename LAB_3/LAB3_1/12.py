user_input = input()
def histogram(numbers):
    for number in numbers:
        print('*' * number)

number_list = [int(num) for num in user_input.split()]

histogram(number_list)