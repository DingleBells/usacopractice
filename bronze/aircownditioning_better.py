N = int(input())
P = list(map(int, input().split()))
T = list(map(int, input().split()))

difs = [x - y for x, y in zip(P, T)]
print(sum(abs(x - y) for x, y in zip(difs + [0], [0] + difs)) // 2)