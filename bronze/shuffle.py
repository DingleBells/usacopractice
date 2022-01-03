fin = open("shuffle.in")
fout = open("shuffle.out", "w")

n = int(fin.readline())
shuffle = list(map(int, fin.readline().split()))
ids = list(map(int, fin.readline().split()))
ans = [0]*n

for i in range(3):
    for j in range(n):
        ans[j] = ids[shuffle[j]-1]
    ids = ans.copy()

for i in ans:
    fout.write(str(i)+"\n")