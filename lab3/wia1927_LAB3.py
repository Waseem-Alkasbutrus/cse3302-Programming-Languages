# Name         : Waseem Alkasbutrus
# ID           : 1001849127
# TODO: TURNED IN ON
# OS           : Ubuntu 20.04.5 LTS (Not on a virtual machine)
# Python Ver   : Python 3.8.10

# Define basic operations
from fileinput import filename
from unittest import result


def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def times(a, b):
    return a * b

def divide(a, b):
    return a / b

# Add operation functions into dictionary
op_dict = {
    '+': plus,
    '-': minus,
    '*': times,
    '/': divide
}

# scan each character and make sure it is a valid operand (0 - 9) or a valid operation (exists in op_dict)
def scan_input(char_stream):
    split_stream = char_stream.split(" ")

    for token in split_stream:
        if (token.isdigit() == False or len(token) != 1) and (token not in op_dict):
            split_stream = "[ERROR] '" + token + "' is not a valid token"
        
    return split_stream

def parse_input(token_stream):
    # Test 1: Not enough tokens for a single expression
    if len(token_stream) < 3:
        return "[ERROR] Not enough tokens (at least 3)"

    # Test 2: Operator before 2 operands
    if not token_stream[0].isdigit() or not token_stream[1].isdigit():
        return "[ERROR] Operators must have 2 operands"

    # Test 3: Incorrect number of operators
    operands = list(filter(lambda token: token.isdigit(), token_stream))

    if (len(token_stream) -  len(operands)) > (len(operands) - 1):
        result = "[ERROR] Too many operators"
    elif (len(token_stream) - len(operands)) < (len(operands) - 1):
        result = "[ERROR] Not enough operators"
    else:
        result = "all good"

    return result
            

# iterates through the token stream and apply operations
def evaluate(token_stream, verbose=False):
    operands = []

    for token in token_stream:
        # if token is an operand, push to stack
        if token.isdigit():
            operands.append(token)

            if verbose:
                print(operands, " <- ", token)
        # if token is operation, apply operation to the top 2 operands in the stack and push result on that same stack
        else:
            # obtain operation function from dictionary
            operation = op_dict.get(token)

            # obtain 2 operands
            a = float(operands.pop())
            b = float(operands.pop())
            
            result = operation(a, b)
            
            # push result of operation to operands stack
            operands.append(result)

            if verbose:
                print(operands, " <- ", a, token, b)
    
    return operands

def solve_RPN(char_stream):
    # make sure all tokens are valid tokens
    token_stream = scan_input(char_stream)

    if "ERROR" in token_stream:
        result = [token_stream]
    else:
        parse_result = parse_input(token_stream)
        
        if "ERROR" in parse_result:
            result = [parse_result]
        else:
            # make sure all token sequences are valid, and apply operations in input
            result = evaluate(token_stream)

    return result[0]


input= open("input_RPN.txt", "r")

for expression in input:
    result = str(solve_RPN(expression.strip('\n')))
    print(result)
