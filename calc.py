#simple calculator

#ask the user to input the first number
num1 = float(input("enter the first number:"))

#ask the user to input the second number 
num2 = float(input("enter the second number:"))

#ask the user to choose an operation
operation = input("enter an operation (+, -, *,/): ")

#perform operation
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation.")
