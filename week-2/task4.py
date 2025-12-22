n, m = map(int, input().split())
s = input().strip()

seen = set()
for i in range(n - m + 1):
    seen.add(s[i:i+m])

print(len(seen))
