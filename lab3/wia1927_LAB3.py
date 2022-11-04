# Name         : Waseem Alkasbutrus
# ID           : 1001849127
# TODO: TURNED IN ON
# OS           : Ubuntu 20.04.5 LTS (Not on a virtual machine)
# Python Ver   : Python 3.8.10

# Define basic operations
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
            print(token + " is not a valid token")
        
    return split_stream

# TODO: make sure to check if its a valid sequence of tokens
# iterates through the token stream and apply operations
def parse_input(token_stream):
    operands = []

    for token in token_stream:
        # if token is an operand, push to stack
        if token.isdigit() == True:
            operands.append(token)

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

            print(operands, " <- ", a, token, b)
    
    return operands

# Example inputs
scanned_line = "6 5 + 4 * 3 2 + 1 * /"
canvas_example = "4 2 5 * + 1 3 2 * + /"

# make sure all tokens are valid tokens
token_stream = scan_input(scanned_line)

# make sure all token sequences are valid, and apply operations in input
result = parse_input(token_stream)

print(result)