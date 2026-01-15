import string

with open("text.txt", "r", encoding="utf-8") as fail:
    stroki = fail.readlines()

kolichestvo_strok = len(stroki)

slova = []
for stroka in stroki:
    stroka = stroka.lower()
    stroka = stroka.translate(str.maketrans("", "", string.punctuation))
    slova.extend(stroka.split())

kolichestvo_slov = len(slova)

kaitalangany = {}

for slovo in slova:
    kaitalangany[slovo] = kaitalangany.get(slovo, 0) + 1

with open("analysis.txt", "w", encoding="utf-8") as rezultat:
    rezultat.write("obshaia linia: " + str(kolichestvo_strok) + "\n")
    rezultat.write("obshie slova: " + str(kolichestvo_slov) + "\n")
    rezultat.write("povtorenie slov:\n")

    for slovo in kaitalangany:
        rezultat.write(slovo + ": " + str(kaitalangany[slovo]) + "\n")
