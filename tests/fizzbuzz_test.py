'''
Tests for the fizzbuzz calculator
'''
from fizzbuzz import calculator

def test_three():
    '''
    Multiples of 3 should be fizz
    '''
    value = calculator.calculate_fizzbuzz(3)
    assert value == 'fizz'

def test_six():
    '''
    Multiples of 3 should be fizz
    '''
    value = calculator.calculate_fizzbuzz(6)
    assert value == 'fizz'

def test_9():
    '''
    Multiples of 3 should be fizz
    '''
    value = calculator.calculate_fizzbuzz(9)
    assert value == 'fizz'

def test_thirty_three():
    '''
    Multiples of 3 should be fizz
    '''
    value = calculator.calculate_fizzbuzz(33)
    assert value == 'fizz'

def test_five():
    '''
    Multiples of 5 should be buzz
    '''
    value = calculator.calculate_fizzbuzz(5)
    assert value == 'buzz'

def test_ten():
    '''
    Multiples of 5 should be buzz
    '''
    value = calculator.calculate_fizzbuzz(10)
    assert value == 'buzz'

def test_twenty():
    '''
    Multiples of 5 should be buzz
    '''
    value = calculator.calculate_fizzbuzz(20)
    assert value == 'buzz'

def test_forty():
    '''
    Multiples of 5 should be buzz
    '''
    value = calculator.calculate_fizzbuzz(40)
    assert value == 'buzz'

def test_fifteen():
    '''
    multiples of 3 and 5 should be fizzbuzz
    '''
    value = calculator.calculate_fizzbuzz(15)
    assert value == 'fizzbuzz'

def test_thirty():
    '''
    multiples of 3 and 5 should be fizzbuzz
    '''
    value = calculator.calculate_fizzbuzz(30)
    assert value == 'fizzbuzz'

def test_forty_five():
    '''
    multiples of 3 and 5 should be fizzbuzz
    '''
    value = calculator.calculate_fizzbuzz(45)
    assert value == 'fizzbuzz'

def test_sixty():
    '''
    multiples of 3 and 5 should be fizzbuzz
    '''
    value = calculator.calculate_fizzbuzz(60)
    assert value == 'fizzbuzz'
