# Ask the user for the first number
# Ask the user for the second number
# Ask the user for the operation
# Perform the operation
# Print the result

print('Welcome to the calculator!')

print('Enter the first number:')
number1 = input()
print('Enter the second number:')
number2 = input()
print('What operation would you llike to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide')
operation = input()

if operation == '1':
    output = int(number1) + int(number2)
elif operation == '2':
    output = int(number1) - int(number2)
elif operation == '3':
    output = int(number1) * int(number2)
elif operation == '4':
    output = int(number1) / int(number2)
    
print(f'The result is {output}')