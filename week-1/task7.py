
first = int(input())
operation = input()
second = int(input())

if operation == "-":
    calculation = first - second
    print(first, operation, second, "=", calculation)

elif operation == "+":
    calculation = first + second
    print(first, operation, second, "=", calculation)

elif operation == "*":
    calculation = first * second
    print(first, operation, second, "=", calculation)

elif operation == "/":
    if second == 0:
        print("Error: division by zero")
    else:
        calculation = first // second
        print(first, operation, second, "=", calculation)

else:
    print("Unknown operation")