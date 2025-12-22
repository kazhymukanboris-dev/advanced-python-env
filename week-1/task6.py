first = int(input())
operation = input()
second = int(input())

if operation == "-":
    calculation = first - second
elif operation == "+":
    calculation = first + second
elif operation == "*":
    calculation = first * second
elif operation == "/":
    calculation = first // second
else:
    print("Unknown operation")
    exit()

print(first, operation, second, "=", calculation) 
