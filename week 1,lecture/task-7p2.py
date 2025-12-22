#calculator
n1 = int(input("Enter the first number: "))
operation = input("Enter the operation (+, -, *, /): ")
n2 = int(input("Enter the second number: "))

if operation == "+":
    print("Add:", n1 + n2)
elif operation == "-":
    print("Subtract:", n1 - n2)
elif operation == "*":
    print("Multiply:", n1 * n2)
elif operation == "/":
    print("Divide:", n1 / n2)
else:
    print("Invalid operation")
