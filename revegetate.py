# Make everything 1
# Then iterate through each connection
# If it is connected to a number that is smaller than it,
# take the largest of the smalls and add one to whatever that one is

fin = open("revegetate.in")
fout = open('revegetate.out', 'w')

n, m = map(int, fin.readline().split())

pastList = []

for line in fin.readlines():
    p1, p2 = sorted(map(int, line.split()))
    pastList.append((p1-1, p2-1))

pastList.sort()
out = [1]*n
for a,b in pastList:
    if out[a] == out[b]:
        out[b] += 1
        for c,d in pastList[:pastList.index((a,b))]:
            if out[c] == out[d]:
                out[d] += 1

fout.write(''.join(map(str, out)))