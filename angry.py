# fin = open("angry.in")
# fout = open("angry.out", 'w')
#
# n = int(fin.readline())
# balelist = []
# for line in fin.readlines():
#     balelist.append(int(fin.readline()))
# balelist.sort()

def testBales(pos, inlist, time, counter): # Pos is the index of thing in array
    time += 1
    counter += 1
    if pos-1 >= 0:
        if inlist[pos-1] + time >= inlist[pos]:
            testBales(pos-1, inlist[:pos] + inlist[pos+1:], time, counter)
            testBales(pos, inlist[:pos] + inlist[pos+1:], time, counter)
    if pos <= len(inlist)-2:
        if inlist[pos+1] - time <= inlist[pos]:
            testBales(pos-1, inlist[:pos] + inlist[pos+1:], time, counter)
            testBales(pos, inlist[:pos] + inlist[pos+1:], time, counter)
    return counter
testlist = [3,4,5,6,8,13]
print(testBales(2, testlist, 0, 0))