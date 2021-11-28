# http://www.usaco.org/index.php?page=viewproblem2&cpid=1011
# Brute force all the possible triangles

fin = open("triangles.in")
fout = open("triangles.out", 'w')

numPosts = int(fin.readline())
pointlist = []
for i in range(numPosts):
    a,b = map(int, fin.readline().split())
    pointlist.append((a,b))

maxarea = 0
for (x1, y1) in pointlist:
    for (x2, y2) in pointlist:
        if (x1,y1) != (x2,y2) and y1 == y2:
            for (x3, y3) in pointlist:
                if (x1,y1) != (x3,y3) and x1 == x3:
                    maxarea = max(maxarea, abs(y1-y3)*abs(x1-x2))

fout.write(str(maxarea))
