# Create a prefix array to store the number of H G J
fin = open("bcount.in")
fout = open("bcount.out", 'w')

n, q = map(int, fin.readline().split())

pSum = [[0,0,0]]
for i in range(n):
    thing = int(fin.readline())
    toAdd = pSum[i].copy()
    toAdd[thing-1] += 1
    pSum.append(toAdd)
# print(pSum)

out = []
for b in range(q):
    x, y = map(int, fin.readline().split())
    newL = []
    for i in range(3):
        newL.append(pSum[y][i] - pSum[x-1][i])
    out.append(newL)

for thing in out:
    fout.write(f"{thing[0]} {thing[1]} {thing[2]}\n")