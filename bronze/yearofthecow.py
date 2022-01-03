zodiacYears = ["Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat"]
zodiacDict = {
"Ox":0, "Tiger":1, "Rabbit":2, "Dragon":3, "Snake":4, "Horse":5, "Goat":6, "Monkey":7,
                 "Rooster":8, "Dog":9, "Pig":10, "Rat":11
}

def determineYearsApart(z1, z2, next):
    years = 0
    curindex = zodiacDict[z1]

    while True:
        if zodiacYears[curindex] == z2 and years != 0:
            return years
        if next:
            curindex = (curindex + 1) % 12
            years += 1
        else:
            if curindex == 0:
                curindex = 11
            else:
                curindex -= 1
            years -= 1

def solve(inlist): # assuming that inlist contains (person, next, zodiac, from)
    cowDict = {"Bessie":("Ox", None, 0)} # {name:(zodiac, nextCow, yearsFromNext)}
    for (person, next, zodiac, fromWho) in inlist:
        n = determineYearsApart(cowDict[fromWho][0],zodiac, next)
        # print(person, fromWho, n)
        cowDict[person] = (zodiac, fromWho, n)

    # print(cowDict)
    curSum = 0
    curCow = "Elsie"
    nextCow = cowDict["Elsie"][1]
    while nextCow != None:
        curSum += cowDict[curCow][2]
        # print(curCow, nextCow, curSum)
        curCow = nextCow
        nextCow = cowDict[curCow][1]

    return curSum

n = int(input())

inlist = []
for i in range(n):
    a = input().split()
    inlist.append((a[0], a[3]=="next", a[4], a[7]))

# print(inlist)
print(abs(solve(inlist)))