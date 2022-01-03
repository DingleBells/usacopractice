fin = open("swap.in")
fout = open('swap.out', 'w')

n, k = map(int, fin.readline().split())
a1, a2 = map(int, fin.readline().split())
b1, b2 = map(int, fin.readline().split())

numlist = [i for i in range(n+1)]

# Reverse items from a1 to a2 and b1 to b2
# List becomes sorted after k+1 swaps

counter = 1
for i in range(n):
    numlist[a1:a2+1] = numlist[a1:a2+1][::-1]
    print(counter, numlist)
    counter += 1
    numlist[b1:b2+1] = numlist[b1:b2+1][::-1]
    print(counter, numlist)
    if numlist == [i for i in range(n+1)]:
        print('same')
        cycleCount = counter
        break
    counter += 1

print("Cycle after step:", cycleCount)

for i in range(k % cycleCount):
    numlist[a1:a2+1] = numlist[a1:a2+1][::-1]
    print(counter, numlist)
    counter += 1
    numlist[b1:b2+1] = numlist[b1:b2+1][::-1]
    print(counter, numlist)
    counter += 1


for num in numlist[1:]:
    fout.write(str(num) + '\n')