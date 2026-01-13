def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
D = int(input("D: "))

alymy = A * D
bolymy = B * C

g = gcd(alymy, bolymy)

alymy = alymy// g
bolymy = bolymy // g

print("Result:", alymy, "/", bolymy)
