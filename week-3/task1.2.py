eda = list(map(int, input("Zapolni massiv: ").split()))
if len(eda) > 15:
    print("oshibka, razmer massiva bolshe 15")
else:
   l = len(eda)
   s = sum(eda)
   ariforta = s / l

print("summa massiva:", s)
print("mean of massive:", ariforta)

eda2 = list(map(int, input("Zapolni massiv eda2: ").split()))
if len(eda2) > 15:
    print("oshibka, razmer massiva bolshe 15")
else:
   l2 = len(eda2)
   s2 = sum(eda2)
   ariforta2 = s2 / l2

print("summa massiva:", s2)
print("mean of massive:", ariforta2)

eda3 = list(map(int, input("Zapolni massiv eda3: ").split()))
if len(eda3) > 15:
    print("oshibka, razmer massiva bolshe 15")
else:
   l3 = len(eda3)
   s3 = sum(eda3)
   ariforta3 = s3 / l3

print("summa massiva:", s3)
print("mean of massive:", ariforta3)
