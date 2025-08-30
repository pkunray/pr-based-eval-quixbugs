def rpn_eval(tokens):
    if not tokens:
        raise ValueError('Empty input not allowed')

    def op(symbol, a, b):
        return {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b
        }[symbol](a, b)

    stack = []

    for token in tokens:
        if isinstance(token, float):
            stack.append(token)
        elif token in ('+', '-', '*', '/'):
            if len(stack) < 2:
                raise ValueError('Insufficient operands')
            a = stack.pop()
            b = stack.pop()
            if token == '/' and a == 0:
                raise ZeroDivisionError('Division by zero')
            stack.append(op(token, b, a))
        else:
            raise ValueError(f'Invalid token: {token}')

    if len(stack) != 1:
        raise ValueError('Malformed expression')

    return stack.pop()

"""
Reverse Polish Notation

Four-function calculator with input given in Reverse Polish Notation (RPN).

Input:
    A list of values and operators encoded as floats and strings

Precondition:
    all(
        isinstance(token, float) or token in ('+', '-', '*', '/') for token in tokens
    )

Example:
    >>> rpn_eval([3.0, 5.0, '+', 2.0, '/'])
    4.0
"""
