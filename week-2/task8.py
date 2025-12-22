soz1 = input().strip()
soz2 = input().strip()

if len(soz1) != len(soz2):
    print("no")
else:
    a = sorted(soz1)
    b = sorted(soz2)

    if a == b:
        print("yes")
    else:
        print("no")
