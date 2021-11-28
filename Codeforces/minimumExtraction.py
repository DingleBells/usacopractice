n = int(input())
for i in range(n):
    length = int(input())
    inlist = list(map(int, input().split()))
    if length == 1:
        print(inlist[0])
    else:
        while (min(inlist) < 0) or (len(inlist) == 2 and max(inlist) - min(inlist) > min(inlist)):
            a = min(inlist)
            inlist.pop(inlist.index(a))
            inlist[:] = [x - a for x in inlist]
            print(inlist)
        print(min(inlist))