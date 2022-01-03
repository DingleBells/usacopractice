n = int(input())
s = input()

ans = 0

for i in range(n):
    lhs = 0
    if i > 0 and s[i-1] != s[i]:
        lhs += 1
        k = i-2
        while k >=0 and s[k] == s[i-1]:
            k -= 1
            lhs += 1

    rhs = 0
    if i+1 < n and s[i+1] != s[i]:
        rhs += 1
        k = i + 2
        while k < n-1 and s[k] == s[k+1]:
            k += 1
            rhs += 1
    ans += lhs*rhs + max(ans, lhs-1) + max(ans, rhs-1)

print(ans)#????