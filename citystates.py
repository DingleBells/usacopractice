fin = open("citystate.in")
fout = open("citystate.out", 'w')

n = int(fin.readline())

count = {}
for i in range(n):
    inp = fin.readline().split()
    city = inp[0]
    state = inp[1]
    if city[:2] != state:
        key = city[:2] + state
        if key not in count:
            count[key] = 0
        count[key] += 1

ret = 0
for key in count:
    otherKey = key[2:] + key[:2]
    if otherKey in count:
        ret += count[key] * count[otherKey]

fout.write(str(ret//2))