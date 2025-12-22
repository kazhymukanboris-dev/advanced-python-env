pokupki = input().split()

schetchik = {}

for tovar in pokupki:
    if tovar in schetchik:
        schetchik[tovar] = schetchik[tovar] + 1
    else:
        schetchik[tovar] = 1

print("Purchase frequency:")
for tovar in schetchik:
    print(tovar + ":", schetchik[tovar])

samiy_populyarniy = ""
max_kolvo = 0

for tovar in schetchik:
    if schetchik[tovar] > max_kolvo:
        max_kolvo = schetchik[tovar]
        samiy_populyarniy = tovar

print("\nMost popular item:", samiy_populyarniy)

print("\nPurchased once:", end=" ")
for tovar in schetchik:
    if schetchik[tovar] == 1:
        print(tovar, end=" ")
print()

print("\nSorted by frequency:")
for tovar1 in schetchik:
    for tovar2 in schetchik:
        if schetchik[tovar1] > schetchik[tovar2]:
            print(tovar1, schetchik[tovar1])
            break
