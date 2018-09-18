first_number = int(input("Enter your first number :"))
operand = input("Enter your operand :")
second_number = int(input("Enter your first number :"))

def add(first_number,second_number):
    return first_number + second_number


def subtract(first_number,second_number):
    return first_number - second_number

def multiply(first_number,second_number):
    return first_number * second_number

def divide(first_number,second_number):
    return first_number /second_number


if operand == "+":
    result = add(first_number, second_number)
elif operand == "-":
    result = subtract(first_number, second_number)
elif operand == "*":
    result = multiply(first_number, second_number)
elif operand == "/":
    result = divide(first_number, second_number)

print(result)
