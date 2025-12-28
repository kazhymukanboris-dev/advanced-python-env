import math

def ushburysh(a, b):
    return math.sqrt(a * a + b * b)

print("ushburysh1:")
a1, b1 = map(int, input().split())
s1 = ushburysh(a1, b1)

print("ushburysh2:")
a2, b2 = map(int, input().split())
s2 = ushburysh(a2, b2)

if s1 > s2:
    print("pervaya gipotenuza bolshe, vtoraya menshe")
elif s1 < s2:
    print("vtoraya gipotenuza bolshe, pervaya menshe")
else:
    print("gipotenuzy ravny")
