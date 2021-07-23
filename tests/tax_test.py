def test_tax_usa():
    """
     USA Tax calculation
    """
    state = input("what state do you live in :")

    if state in ('TN', 'TX', 'FL'):
        tax = 0.09
    elif state == 'MD':
        tax = 0.06
    else:
        tax = 0.00
    print("You pay:" + str(tax))
    return tax
