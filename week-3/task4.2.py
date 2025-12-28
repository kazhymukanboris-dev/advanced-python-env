def proverka(x, y, R, shetchik):
    if x * x + y * y < R * R:
        shetchik[0] = shetchik[0] + 1

R = float(input("R: "))

p1, p2 = map(float, input("Point P (x y): ").split())
f1, f2 = map(float, input("Point F (x y): ").split())
l1, l2 = map(float, input("Point L (x y): ").split())

shetchik = [0]

proverka(p1, p2, R, shetchik)
proverka(f1, f2, R, shetchik)
proverka(l1, l2, R, shetchik)

print("tochki vnutri kruga:", shetchik[0])
