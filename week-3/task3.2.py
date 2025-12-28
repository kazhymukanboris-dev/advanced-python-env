soz = input("Vvedite stroku: ")

words = soz.split()
result = []

for a in words:
    sorted_word = "".join(sorted(a))
    result.append(sorted_word)

print(" ".join(result))
