n = int(input())
nlist = []
elist = []

for i in range(n):
    direction, x, y = input().split()
    if direction == "E":
        elist.append((int(x), int(y), i))
    else:
        nlist.append((int(x), int(y), i))

nlist.sort()
elist.sort(key=lambda x: x[1])

stopped = [None] * n
for ncow in nlist:
    for ecow in elist:
        """
        Cows cannot collide if ncow's x is less than ecow's x
        Also if ncow's y is greater than ecow's y
        """
        if ncow[0] > ecow[0] and ncow[1] < ecow[1]:
            # print(f"Checking ncow with coords {ncow} and ecow with coords {ecow}")
            ndist = ecow[1]-ncow[1]
            edist = ncow[0]-ecow[0]

            if ndist > edist and stopped[ecow[2]] is None: # north cow gets there first
                stopped[ncow[2]] = ndist
                break

            elif ndist < edist and stopped[ecow[2]] is None:
                stopped[ecow[2]] = edist

for thing in stopped:
    if thing is None:
        print("Infinity")
    else:
        print(thing)