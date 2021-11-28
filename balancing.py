# idea: Optimize later, start with a brute force
# The horzontal and vertical lines both need to be even
# Make a function ot find # cows in each quadrant given x and y lines
import statistics
fin = open("balancing.in")
fout = open("balancing.out", 'w')

def findCowsInQuadrants(xLine, yLine, inlist):
    topLeft, topRight, botLeft, botRight = 0,0,0,0
    for (x,y) in inlist:
        left = None
        above = None
        if x < xLine:
            left = True
        elif x > xLine:
            left = False
        if y > yLine:
            above = True
        elif y < yLine:
            above = False

        if above and left:
            topLeft += 1
        elif above and not left:
            topRight += 1
        elif not above and left:
            botLeft += 1
        elif not above and not left:
            botRight += 1
    return max(topLeft, topRight, botLeft, botRight)

N,B = map(int, fin.readline().split())
coordlist  = []
x_vals = []
y_vals = []
for i in range(N):
    x,y = map(int,fin.readline().split())
    x_vals.append(x)
    y_vals.append(y)

ans = N
for x in x_vals:
    for y in y_vals:
        xdiv = x + 1
        ydiv = y + 1
        d1 = d2 = d3 = d4 = 0
        for i in range(N):
            if x_vals[i] < xdiv and y_vals[i] > ydiv:
                d1 += 1
            elif x_vals[i] > xdiv and y_vals[i] > ydiv:
                d2 += 1
            elif x_vals[i] < xdiv and y_vals[i] < ydiv:
                d3 += 1
            else:
                d4 += 1
        m = max(d1, d2, d3, d4)
        ans = min(m, ans)
fout.write(str(ans))
