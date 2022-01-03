fin = open("mowing.in")
fout = open("mowing.out", 'w')

n = int(fin.readline())

movelist = []
for i in range(n):
    a = fin.readline().split()
    movelist.append((a[0], int(a[1])))

moveDict = {}
curcoord = (0,0)

curtime = 0
x = 10000000000000000
for direction, length in movelist:
    for i in range(length):
        (a,b) = curcoord
        if curcoord in moveDict:
            x = min(x, curtime-moveDict[curcoord])
        moveDict[curcoord] = curtime
        if direction == "N":
            b += 1
        elif direction == "S":
            b -= 1
        elif direction == "E":
            a += 1
        elif direction == "W":
            a -= 1
        curcoord = (a,b)
        curtime += 1

if x == 10000000000000000:
    x = -1
fout.write(str(x))