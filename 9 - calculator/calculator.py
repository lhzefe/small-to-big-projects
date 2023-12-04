def operation(operator: str, a, b):
    '''
    Return the result based on the operation's choice.
    E.g.: operation(+), will return the result of _sum(a,b).
    '''
    
    if operator == "+":
        return _sum(a, b)
    elif operator == "-":
        return _sub(a, b)
    elif operator == "*":
        return _mult(a, b)
    elif operator == "/" and b != 0:
        return _div(a, b)
    else:
        return "invalid operation"

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
    return a / b

def _mult(a, b):
    '''
    Return the multiplication of two numbers passed as parameters.
    E.g.: _mult(2,3), will return 6.
    '''
    return a * b

print("This is a simple calculator with the basics operators *, -, + and /")
first_number = float(input("Type the first number: "))
operator = str(input("Choose an operator: "))
second_number = float(input("Type the second number: "))
print (operation(operator, first_number, second_number))
