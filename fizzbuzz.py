'''
This module is the main entrypoint into fizzbuzz
'''
import fizzbuzz_calculator

def fizz_buzz_generator(upper_limit):
    '''
    This generator is used to return the fizzbuzz values for a range
    '''
    for i in range(upper_limit):
        yield fizzbuzz_calculator.calculate(i)

for x in fizz_buzz_generator(101):
    print(x)
