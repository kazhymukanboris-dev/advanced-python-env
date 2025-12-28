def zamena(spisok):
    spisok[0], spisok[-1] = spisok[-1], spisok[0]

razmer = int(input("razmer: "))
a = list(map(int, input().split()))

print("Ishodniy massiv:", a)

zamena(a)

print("Massiv posle zameny:", a)
