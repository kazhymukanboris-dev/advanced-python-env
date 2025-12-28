san = int(input())

result = ""

for i in range(10):
    ostatok = san % 8
    result = str(ostatok) + result
    san = san // 8

print(result)
