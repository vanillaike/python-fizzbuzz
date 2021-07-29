'''
This module performs the fizzbuzz calculation for a given number
'''

def calculate_fizzbuzz(number):
    '''
    Given a number return the fizzbuzz value
    '''
    value = ''
    if number % 3 == 0:
        value += 'fizz'
    if number % 5 == 0:
        value += 'buzz'
    if number % 5 == 0:
        value += 'BANG'
    if number == 0 or value == '':
        value = str(number)
    return value
