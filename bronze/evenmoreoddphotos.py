# Even + Even = Even
# Odd + Odd = Even
# Odd + Even  = Odd

# Number of evens > number of odds:
# Number of 2 * number of odds + 1
# Number of evens == number of odds:
# number of evens * 2
# Number of evens < number of odds:
# Pair odd cows until evens >= odds

n = int(input())
cowlist = list(map(int, input().split()))
evens = 0
odds = 0

for num in cowlist:
    if num % 2 == 0:
        evens += 1
    else:
        odds += 1


while odds > evens:
    odds -= 2
    evens += 1

if evens > odds + 1:
    evens = odds + 1

print(evens + odds)