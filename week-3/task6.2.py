import math
a,b,c,d,e = list(map(int,input().split()))

poluperimetr1 = (a + b + e ) / 2
ploshad1 = math.sqrt(poluperimetr1 * (poluperimetr1-a) * (poluperimetr1-b) * (poluperimetr1-e))

poluperimetr2 =  (c + d + e)  / 2
ploshad2 = math.sqrt(poluperimetr2 * (poluperimetr2-c) * (poluperimetr2-d) * (poluperimetr2-e))

chetyrehugolnik = ploshad1 + ploshad2

print(chetyrehugolnik)