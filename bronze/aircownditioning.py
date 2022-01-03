
def splitlist(difflist):
    paritions = []
    start = 0
    for i in range(len(difflist)):
        # Opposite signs: Split list
        if difflist[i] * difflist[start] < 0:
            paritions.append(difflist[start:i])
            start = i
        elif difflist[i] == 0:
            paritions.append(difflist[start:i])
            start = i+1

    paritions.append(difflist[start:])

    return paritions

# a = splitlist([1,3,5,-1,7,0,5,3,-2,-1])
# print(a)

def findMax(partitions):
    if len(partitions) == 0:
        return 0
    elif len(partitions) == 1:
        return abs(partitions[0])
    # Find minimum by finding least abs value
    smallest = min(map(abs, partitions))
    # Increase/decrease by smallest steps
    for i in range(len(partitions)):
        if partitions[i] > 0:
            partitions[i] -= smallest
        else:
            partitions[i] += smallest
    # Add the results to the counter
    counter = smallest
    # Repeat again
    partitions = splitlist(partitions)
    # print(counter, partitions)
    # Return our final value
    for partition in partitions:
        # print(counter, findMax(partition))
        counter += findMax(partition)
    return counter
n = int(input())
want = list(map(int, input().split()))
current = list(map(int, input().split()))

changeList = []

for i in range(n):
    changeList.append(current[i] - want[i])
ans = 0
for partition in splitlist(changeList):
    ans += findMax(partition)

print(ans)