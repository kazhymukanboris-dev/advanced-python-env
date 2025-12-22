str1 = input().strip()
str2 = input().strip()

ln = len(str2)
check = set()
mix = str2 + str2

for x in range(ln):
    check.add(mix[x:x+ln])

count = 0
for y in range(len(str1) - ln + 1):
    if str1[y:y+ln] in check:
        count += 1

print(count)
