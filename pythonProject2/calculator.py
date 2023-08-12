#calculator
def add(n1,n2):
    return n1+n2

def substract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def devide(n1,n2):
    return n1/n2
operations = {
    '+': add,
    '-': substract,
    '*': multiply,
    '/': devide}

num1 = int(input('what is your first number'))

for keys in operations:
    print(keys)
operation_symbol = input('pick an operation symbol from the line above')

num2 = int(input('what is your second number'))

calculation_function = operations[operation_symbol]
answer = calculation_function(num1,num2)
print(f'{num1} {operation_symbol} {num2} = {answer}')