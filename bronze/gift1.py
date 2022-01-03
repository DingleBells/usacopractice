fin = open('gift1.in', 'r')
fout = open('gift1.out', 'w')

giftDict = {}

# Read in the names

n = int(fin.readline())
for i in range(n):
    line = fin.readline()
    name = line.strip()
    giftDict[name] = 0
print(giftDict)

while True:
    try:
        whoFrom = fin.readline().strip()
        print("whofrom:", whoFrom)
        amount, numPeople = map(int, fin.readline().split())
        for i in range(numPeople):
            giftDict[fin.readline().strip()] += amount
        giftDict[whoFrom] -= amount + (amount % numPeople)
    except:
        break

for key in giftDict:
    fout.write(key + ' ' + str(giftDict[key]) + '\n')
