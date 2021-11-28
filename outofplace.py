# Count the number of items that are unsorted and return that number

fin = open("outofplace.in")
fout = open("outofplace.out", 'w')
n = int(fin.readline())
inlist= []
for i in range(n):
    inlist.append(int(fin.readline()))

sortedList = sorted(inlist)
counter = 0
for i in range(n):
    if sortedList[i] != inlist[i]:
        counter += 1

fout.write(str(counter-1))