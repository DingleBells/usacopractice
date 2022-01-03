# Try all possible starting points
import os

fin = open("cbarn.in", 'r')
fout = open("cbarn.out", 'w')

n = int(fin.readline().strip())
mylist = []
for line in fin.readlines():
    mylist.append(int(line.strip()))


def startSim(start, inlist, totalcows):
    distance = 0
    numCows = totalcows
    for room in inlist[start:] + inlist[:start]:
        numCows -= room
        distance += numCows
    return distance

total = sum(mylist)
minimum = 1000000000000000000
for i in range(len(mylist)):
    minimum = min(startSim(i, mylist, total), minimum)

fout.write(str(minimum))