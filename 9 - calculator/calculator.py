def _sum(a, b):
    '''
    Return the sum of two numbers passed as parameters.
    E.g.: _sum(2,3), will return 5.
    '''
    return a + b

def _sub(a, b):
    '''
    Return the subtraction of two numbers passed as parameters.
    E.g.: _sub(3,2), will return 1.
    '''
    return a - b

def _div(a, b):
    '''
    Return the division of two numbers passed as parameters.
    E.g.: _div(4,2), will return 2.
    '''
    if b != 0:
        return a / b
    else:
        return "Invalid division"

def _mult(a, b):
    '''
    Return the multiplication of two numbers passed as parameters.
    E.g.: _mult(2,3), will return 6.
    '''
    return a * b

def calculator():
    '''This is the function that makes the calculus'''
    
    print("This is a simple calculator with the basics operators")
    first_number = float(input("Type the first number: "))
    continue_calculating = True
    while continue_calculating:
        for operator in operators: print(operator, end="   ")
        operator_selected = str(input("1=> Choose an operator: "))
        operation = operators[operator_selected]
        second_number = float(input("Type the second number: "))
        result = operation(first_number, second_number)
        print(f"{first_number} {operator_selected} {second_number} = {result}")
        
        keep_result = input("Would you like to do another operation with the\
 current result?\n[y] for yes\n[n] for new calculus\n[e] for exit\n--> ")

        if keep_result == 'y':
            first_number = result
            continue_calculating = True
        elif keep_result == 'n':
            continue_calculating = False
            calculator()
        else:
            continue_calculating = False

operators = {
    "+": _sum,
    "*": _mult,
    "-": _sub,
    "/": _div,
}

calculator()
