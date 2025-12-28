import math

def kvadrat(side):
    return side * side

def pryamougolnik(length, width):
    return length * width

def krug(radius):
    return math.pi * radius * radius

print("1 - kvadrat")
print("2 - pryamougolnik")
print("3 - krug")

vibor = int(input("Vyberite figuru: "))

if vibor == 1:
    side = float(input("Storona kvadrata: "))
    area = kvadrat(side)
    print("Ploshad kvadrata =", area)

elif vibor == 2:
    length = float(input("Dlina: "))
    width = float(input("Shirina: "))
    area = pryamougolnik(length, width)
    print("Ploshad pryamougolnika =", area)

elif vibor == 3:
    radius = float(input("Radius: "))
    area = krug(radius)
    print("Ploshad kruga =", area)

else:
    print("Neverny vybor")
