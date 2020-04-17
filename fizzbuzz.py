def fizz_buzz_generator(N):
    for i in range(N):
        value = ''
        if i % 5 == 0:
            value += 'fizz'
        if i % 3 == 0:
            value += 'buzz'
        if i == 0 or value == '':
            value = str(i)
        yield value

for x in fizz_buzz_generator(101):
    print(x)