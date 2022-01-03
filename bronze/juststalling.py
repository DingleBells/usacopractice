n = int(input())
cows = list(map(int, input().split()))
stalls = list(map(int, input().split()))

stalls.sort(reverse=True)
cows.sort()

ans = 1

for i in range(n-1, -1, -1):
    cow = cows[i]
    counter = 0
    for stall in stalls:
        if stall < cow:
            break
        counter += 1
    ans *= (counter - (n - i - 1))
print(ans)
