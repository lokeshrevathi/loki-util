#Alternate sorting
listLength = int(input())
ioList = []
firstHalf = []
secondHalf = []
opList = []
for i in range(listLength):
    ioList.append(int(input()))
ioList = sorted(ioList)
firstHalf = ioList[0 : listLength // 2]
secondHalf = ioList[listLength - 1 : (listLength // 2) - 1 : -1]
for i in range(0, listLength // 2):
    opList.append(secondHalf[i])
    opList.append(firstHalf[i])
if listLength % 2 != 0:
    opList.append(secondHalf[len(secondHalf) - 1])
for i in opList:
    print(i, end=" ")