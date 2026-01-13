def obvertka(soz, eni):
    bolshek = []
    for i in range(0, len(soz), eni):
        bolshek.append(soz[i:i+eni])
    return "\n".join(bolshek)

text = input()
razmer = int(input())
print(obvertka(text, razmer)).