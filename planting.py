fin = open("planting.in")
fout = open("planting.out", 'w')

n = int(fin.readline())

conDict = {}
for i in range(n-1):
    a,b = map(int, fin.readline().split())
    for thing in [a,b]:
        if thing in conDict:
            conDict[thing] += 1
        else:
            conDict[thing] = 1

fout.write(f"{max(conDict.values())+1}")