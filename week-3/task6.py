def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

A = int(input("A: "))
B = int(input("B: "))

g = gcd(A, B)
lcm = (A * B) // g

print("GCD:", g)
print("LCM:", lcm)
