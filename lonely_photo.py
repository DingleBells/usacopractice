n = int(input())
instring = input()

inlist = []
prevLetter = instring[0]
streak = 0
for letter in instring:
    if letter != prevLetter:
        inlist.append((prevLetter, streak))
        prevLetter = letter
        streak = 0
    streak += 1
inlist.append((prevLetter, streak))

# Check doubles:

# HHH GG n, k: (
# HHHG
# HHG
# HGG

counter = 0
# print(inlist)
for i in range(len(inlist)-1):
    # print(i)
    # print(inlist[i], inlist[i+1], inlist[i][1] - 1 + inlist[i+1][1] - 1)
    counter += inlist[i][1] - 1
    counter += inlist[i+1][1] - 1

for j in range(len(inlist)-2):
    if inlist[j+1][1] == 1:
        # print(j, inlist[j], inlist[j+1], inlist[j+2], inlist[j][1] * inlist[j+2][1])
        counter += inlist[j][1] * inlist[j+2][1]

print(counter)

# counter = 0
# for startIndex in range(n):
#     gCount = 0
#     hCount = 0
#     for endIndex in range(startIndex, n):
#         if instring[endIndex] == "G":
#             gCount += 1
#         else:
#             hCount += 1
#
#         if hCount == 1 and gCount >= 2:
#             counter += 1
#         elif hCount >= 2 and gCount == 1:
#             counter += 1
#
#         if hCount >= 2 and gCount >= 2:
#             break
#
# print(counter)