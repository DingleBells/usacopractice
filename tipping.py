fin = open("cowtip.in")
fout = open('cowtip.out', 'w')
grid = []
n = int(fin.readline())
for line in fin.readlines():
    grid.append(line)


result = 0
for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if grid[i][j] == "1":
            result += 1
            for a in range(0, i + 1):
                strlist = list(grid[a])
                for b in range(0, j + 1):
                    if grid[a][b] == "0":
                        strlist[b] = "1"
                        grid[a] = ''.join(strlist)
                    else:
                        strlist[b] = "0"
                        grid[a] = ''.join(strlist)

fout.write(str(result))