# Add
from html.entities import name2codepoint


def add(n1,n2):
    return n1+n2

# Sub
def substrate(n1,n2):
    return n1 - n2

# multiple
def multiple(n1,n2):
    return n1 * n2

# divide
def divide(n1,n2):
    return n1 / n2

# Operator
operators = {
    "+":add,
    "-":substrate,
    "*":multiple,
    "/":divide
}

def calculator():
    num1 = float(input('Enter a value..  '))
    for symbol in operators:
        print(symbol)
    to_continue = True 
    while to_continue:  
        chosen = input('Enter a choice..  ')
        num2 = float(input('Enter the next value.. '))
        cal_function = operators[chosen]
        answer = cal_function(num1,num2)
        print(f'{num1} {chosen} {num2} = {answer}')
        if input("Type 'yes' to continue or 'no' to exit") == "yes":
            num1 = answer
        else:
            to_continue = False
            calculator()
        
calculator()
