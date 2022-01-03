

# Find possible paths

def findPossiblePaths(n, k, grid):
    paths = []
    while k > 0:
        if k == 1:
            # Right then down:
            cur = ""
            cur += grid[0]
            for i in range(1,n):
                cur += grid[i][n-1]
            if "H" not in cur:
                paths.append(cur)
            # Down then right
            cur = ""
            for i in range(n):
                cur += grid[i][0]
            cur += grid[n-1][1:]
            if "H" not in cur:
                paths.append(cur)

        if k == 2:
            # Right some down all right rest
            for tp in range(1,n-1):
                cur = ""
                cur += grid[0][:tp+1]
                for j in range(1,n):
                    cur += grid[j][tp]
                cur += grid[n-1][tp+1:]
                if "H" not in cur:
                    paths.append(cur)
            # Down some right all down rest
            for tp2 in range(1,n-1):
                cur = ""
                for j in range(tp2):
                    cur += grid[j][0]
                cur += grid[tp2]
                for j in range(tp2+1,n):
                    cur += grid[j][n-1]
                if "H" not in cur:
                    paths.append(cur)

        if k == 3:
            # Right some, down some, right all, down all
            for right in range(1,n-1): # Right some
                for down in range(1,n-1):
                    cur = ""
                    cur = grid[0][:right+1] # Go right in this line
                    for tmp in range(1,down+1):
                        # print(grid[tmp][right])
                        cur += grid[tmp][right]
                    # print(cur)
                    cur += grid[down][right+1:] # Right all
                    for tmp in range(down+1, n): # down rest
                        cur += grid[tmp][n-1]
                    if "H" not in cur:
                        paths.append(cur)
            # Down some, right some, down all, right all
            for down in range(1,n-1):
                for right in range(1, n-1):
                    cur = ""
                    for tmp in range(down + 1): # Down some in this loop
                        cur += grid[tmp][0]
                    cur += grid[down][1:right+1] # Right some
                    for tmp in range(down+1, n): # Down rest
                        cur += grid[tmp][right]
                    cur += grid[n-1][right+1:] # Right rest
                    if "H" not in cur:
                        paths.append(cur)
        k -= 1
    return paths

n = int(input())
dlist = []
for i in range(n):
    a, k = map(int, input().split())
    temp = []
    for j in range(a):
        temp.append(input())
    dlist.append((a, k, temp))

# print(dlist)
for (a,k,temp) in dlist:
    print(len(findPossiblePaths(a,k,temp)))
