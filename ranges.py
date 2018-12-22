#for value in range(1,21):
    #print(value)

million = []
for value in range(1,1000001):
    million.append(value)

print(sum(million))

odds = []
for odd in range(1,21,2):
    odds.append(odd)

print(odds)

multiplesofthree = [value*3 for value in range(1,11)]

print(multiplesofthree)

cubes = []
for value in range(1,11):
    cubes.append(value**3) 
print(cubes)
