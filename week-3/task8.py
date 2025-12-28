san = int(input())

for num in range(1, san + 1):
    podhodit = True

    for digit in str(num):
        d = int(digit)

        if d == 0 or num % d != 0:
            podhodit = False
            break

    if podhodit:
        print(num)
