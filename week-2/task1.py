jol = input().strip()

count = 0
for pos in range(len(jol) - 4):
    part = jol[pos:pos+5]
    if part == ">>-->" or part == "<--<<":
        count += 1

print(count)