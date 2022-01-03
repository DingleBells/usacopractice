n = int(input())
flowers = list(map(int, input().split()))

counter = 0
for i in range(n):
    for j in range(i, n):
        avg = sum(flowers[i:j+1]) / (j-i + 1)
        for flower in flowers[i:j+1]:
            if flower == avg:
                counter += 1
                break

print(counter)