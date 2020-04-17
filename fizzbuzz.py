def calculate_value(number):
    value = ''
    if number % 5 == 0:
        value += 'fizz'
    if number % 3 == 0:
        value += 'buzz'
    if number == 0 or value == '':
        value = str(number)
    return value

def fizz_buzz_generator(upper_limit):
    for i in range(upper_limit):
        yield calculate_value(i)

for x in fizz_buzz_generator(101):
    print(x)
