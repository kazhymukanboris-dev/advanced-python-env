k = input().strip()

if k[0] == 'x':
    if k[1] == '+':
        m = int(k[4]) - int(k[2])
    else:
        m = int(k[4]) + int(k[2])

elif k[2] == 'x':
    if k[1] == '+':
        m = int(k[4]) - int(k[0])
    else:
        m = int(k[0]) - int(k[4])

else:
    if k[1] == '+':
        m = int(k[0]) + int(k[2])
    else:
        m = int(k[0]) - int(k[2])

print(m)
