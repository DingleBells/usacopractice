# If two stations are connected, mark it with a number

fin = open('factory.in')
fout = open('factory.out', 'w')

n = int(fin.readline())

# walkways = [i for i in range(n+1)]
# print(walkways)
# for i in range(n-1):
#     a, b = map(int, fin.readline().split())
#     print(a,b)
#     original = walkways[a]
#     print(f"Replacing all of {walkways[a]}s with {walkways[b]}")
#     for e in range(n+1):
#         if walkways[e] == original:
#             walkways[e] = walkways[b]
#
#     print(walkways)
#
#
# if len(set(walkways)) == 2:
#     fout.write(str(walkways[1]))
# else:
#     fout.write('-1')

outgoing = [0]*101
incoming = [0]*101

for i in range(n-1):
    a,b = map(int, fin.readline().split())
    outgoing[a] += 1
    incoming[b] += 1

ans = -1
for i in range(n):
    if outgoing[i] == 0  and ans != -1:
        ans = -1
        break
    if outgoing[i] == 0:
        ans = i

fout.write(str(ans))