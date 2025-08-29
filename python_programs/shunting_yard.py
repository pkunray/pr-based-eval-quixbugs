def shunting_yard(tokens):
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }

    rpntokens = []
    opstack = []
    for token in tokens:
        if isinstance(token, int):
            rpntokens.append(token)
        elif token in precedence:
            # Pop operators from the stack to the output queue if they have higher or equal precedence
            while opstack and opstack[-1] != '(' and precedence[token] <= precedence[opstack[-1]]:
                rpntokens.append(opstack.pop())
            opstack.append(token)
        elif token == '(':  # Push '(' to the stack
            opstack.append(token)
        elif token == ')':
            # Pop from the stack to the output queue until '(' is encountered
            while opstack and opstack[-1] != '(': 
                rpntokens.append(opstack.pop())
            if opstack and opstack[-1] == '(':  # Pop the '(' from the stack
                opstack.pop()
            else:
                raise ValueError("Mismatched parentheses")
        else:
            raise ValueError(f"Unrecognized token: {token}")

    # Pop all the operators from the stack to the output queue
    while opstack:
        top = opstack.pop()
        if top in '()':
            raise ValueError("Mismatched parentheses")
        rpntokens.append(top)

    return rpntokens