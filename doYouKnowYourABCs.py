numList = sorted(list(map(int, input().split())))
smallest = numList[0]
secondSmallest = numList[1]
largest = numList[-1]
print(f"{smallest} {secondSmallest} {largest - smallest - secondSmallest}")