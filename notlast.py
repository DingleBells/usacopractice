fin = open("notlast.in")
fout = open("notlast.out", "w")

cowDict = {"Bessie":0,
           "Elsie":0,
           "Daisy":0,
           "Gertie":0,
           "Annabelle":0,
           "Maggie":0,
           "Henrietta":0}

n = int(fin.readline())

for i in range(n):
    cow, milk = fin.readline().split()
    cowDict[cow] += int(milk)

cowmilk = []
for cow in cowDict:
    cowmilk.append((cow, cowDict[cow]))

cowmilk.sort(key=lambda x: x[1])

smallest = cowmilk[0][1]
secSmallest= None
secSmallList = []

for (cow, milk) in cowmilk:
    print(milk, secSmallest, secSmallList)
    if milk > smallest and secSmallest == None:
        secSmallest = milk
        secSmallList.append(cow)
    elif milk == secSmallest:
        secSmallList.append(cow)
    elif secSmallest != None and milk > secSmallest:
        break

print(cowmilk)
print(secSmallList)
if len(secSmallList) == 1:
    fout.write(secSmallList[0])
else:
    fout.write("Tie")
