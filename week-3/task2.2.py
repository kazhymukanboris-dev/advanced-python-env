def pryamougolnik(a, b):
    return a * b

print("Perviy pryamougolnik")
a1, b1 = map(int, input().split())
print("Ploshad:", pryamougolnik(a1, b1))

print("Vtoroy pryamougolnik")
a2, b2 = map(int, input().split())
print("Ploshad:", pryamougolnik(a2, b2))

print("Tretiy pryamougolnik")
a3, b3 = map(int, input().split())
print("Ploshad:", pryamougolnik(a3, b3))
