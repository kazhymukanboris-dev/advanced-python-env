let = set("ABCEHKMOPTXY")

k = int(input())
for j in range(k):
    s = input().strip()

    good = True

    if len(s) != 6:
        good = False
    elif s[0] not in let:
        good = False
    elif not s[1:4].isdigit():
        good = False
    elif s[4] not in let:
        good = False
    elif s[5] not in let:
        good = False

    if good:
        print("Yes")
    else:
        print("No")
