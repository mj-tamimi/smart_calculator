def add(number1, number2):
    print(number1 + number2)
    
def subtract(number1, number2):
    print(number1 - number2)
    
def multiply(number1, number2):
    print(number1 * number2)
    
def divide(number1, number2):
    print(number1 / number2)

def power(number1, number2):
    print(number1 ** number2)
    

print("calculator")

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

operation = input("enter symbol:   ")

if operation == "+":
    print("The operation is: Addition")
    print("--------------------------")
    add(number1, number2)

elif operation == "-":
    print("The operation is: subtraction")
    print("--------------------------")
    subtract(number1, number2)

elif operation == "*":
    print("The operation is: multiplication")
    print("--------------------------")
    multiply(number1, number2)

elif operation == "/":
    
    if number2 == 0:
        print("You cannot divide by '0'.")
    else:
        print("The operation is: division")
        print("--------------------------")
        divide(number1, number2)
    
elif operation == "**":
    print("The operation is: power")
    print("--------------------------")
    power(number1, number2)

if operation == "%":
    print("The operation is: remainings")
    print("--------------------------")
    print(number1 % number2)
    
if operation == "**":
    print("The operation is: power")
    print("--------------------------")
    power(number1, number2)
