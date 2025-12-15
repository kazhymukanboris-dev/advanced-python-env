data = input().split()

emp1 = int(data[0])
emp2 = int(data[1])
emp3 = int(data[2])

if emp1 > emp2 and emp1 > emp3: 
    highest = emp1
elif emp2 > emp1 and emp2 > emp3:
    highest = emp2
else:
    highest = emp3

if emp1 < emp2 and emp1 < emp3:
    lowest = emp1
elif emp2 < emp1 and emp2 < emp3:
    lowest = emp2
else:
    lowest = emp3

difference = highest - lowest
print(difference)