# First sort the list
# Set productions: Mildred = 7 Bessie = 7 Elsie = 7
# For each day in range(100)
# If there are notes for a cow on that day:
#   Change the cow's production by n
# call function getLeaderboard(mildred, bessie, elsie) and compare to previous leaderboard
# If leaderboards are different, then change counter by 1, else don't change


fin = open("measurement.in")
fout = open("measurement.out", 'w')

n = int(fin.readline())
notes = {}

for line in fin.readlines():
    [day, name, change] = line.split()
    if day in notes:
        notes[int(day)].append((name, int(change)))
    else:
        notes[int(day)] = [(name, int(change))]

def getLeaderboard(milkdict):
    abc = [("Mildred",milkdict["Mildred"]), ("Bessie",milkdict["Bessie"]), ("Elsie",milkdict["Elsie"])]
    abc.sort(key=lambda x:x[1], reverse=True)
    print(abc)
    if abc[0][1] == abc[1][1]:
        if abc[0][1] == abc[2][1]:
            return [abc[0][0], abc[1][0], abc[2][0]]
        else:
            return [abc[0][0], abc[1][0]]
    return [abc[0][0]]


milkDict = {"Mildred":7,
            "Bessie":7,
            "Elsie":7}
lb = [("Mildred",7), ("Bessie",7), ("Elsie",7)]
counter = 0
print(lb)
for day in range(101):
    if day in notes:
        for (name, change) in notes[day]:
            milkDict[name] += change
        newlb = getLeaderboard(milkDict)
        if newlb != lb:
            counter += 1
        print(milkDict)
        print(f"day:{day}, lb:'{lb}', newlb:'{newlb}', counter:{counter}")
        lb = newlb
fout.write(str(counter))