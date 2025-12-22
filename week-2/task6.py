soz = input().split()

uzin = 0
for elm in soz:
    if len(elm) > uzin:
        uzin = len(elm)

for pos in range(len(soz)):
    soz[pos] = soz[pos] + "_" * (uzin - len(soz[pos]))

print(soz)
