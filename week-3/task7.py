x,y,z,t = list(map(int,input().split()))
def ptriugolnik (x,y):
    return (x * y) / 2 

def priamougolnik (z,t):
    return z * t

ploshad = ptriugolnik(x, y) + priamougolnik(z, t)

print(ploshad)

