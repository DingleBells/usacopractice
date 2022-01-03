# Make a list that is initially all zeroes
# Put the cows that need to be in a certain spot in that spot by changing the value to the number of the cow
# Then put the relative order of the cows in the list
# Start from the back of the list
# If the value is not already in the list
# If the number in front of the value is already in the list
# Add value to the latest possible 0 that is in behind the list
# If the number behind it is in the list
# Move the pointer to the current element
# Find the first empty spot and return the index

fin = open('milkorder.in')
fout = open('milkorder.out', 'w')

n, m, k = map(int, fin.readline().split())
spots = [0] * n
relOrder = list(map(int, fin.readline().split()))
insists = []
for i in range(k):
    cow, where = map(int, fin.readline().split())
    insists.append((cow, where))

for (cow, where) in insists:
    spots[where-1] = cow
    print(cow, where)
print(spots)

# [3,0,5,0,0,0]
# 4,5,6
pointer = n-1
for i in range(len(relOrder)-1, -1, -1):
    print("i",i)
    if relOrder[i] not in spots:
        for b in range(pointer,-1,-1):
            print(b)
            if spots[b] == 0:
                spots[b] = relOrder[i]
                break
    else:
        pointer = spots.index(relOrder[i])

print(spots)

if 1 not in spots:
    for c in range(n):
        print(c)
        if spots[c] == 0:
            fout.write(str(c+1))
            break

else:
    fout.write(str(spots.index(1)+1))