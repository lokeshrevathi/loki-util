#extract_value_from_text_file
import json

def extractValue() -> None:
    numericValueHeader = ['REV', 'QTY', 'CHARGES', 'ALLOW/REIM', 'RSN', ' AMOUNT']
    stdLineLength = 0
    textFileStr = open('sample.txt','r').read().split('\n')
    objLists = []
    flag = 0
    i = 0
    c = 0
    while i < len(textFileStr):
        if '----' in textFileStr[i]:
            flag = 0
            c = 0
        if flag == 1 or 'ADJ REASON CODES:' in textFileStr[i]:
            if flag == 0:
                i += 1
                flag = 1
                continue
            if c == 0:
                keys = textFileStr[i] + '  ' + textFileStr[i + 1] + '  ' +  textFileStr[i + 2]
                stdLineLength = len(textFileStr[i])
                keyList = [k for k in keys.split('  ') if k != '']
                keyDict = getHeaderValueWithIndexRanges(keyList, keys)
                # print(keyDict)
                keyStartInds = {dval[0]:dval[1] for dval in list(keyDict.values())}
                # print(keyStartInds)
                # break
            else:
                values = constructStringForGivenLength(textFileStr[i], stdLineLength) + '  ' + constructStringForGivenLength(textFileStr[i + 1], stdLineLength) + '  ' + constructStringForGivenLength(textFileStr[i + 2], stdLineLength)
                valueList = splitAndReturnValueWithIndex(values)
                flagI = 0
                i1 = 0
                objList = []
                while i1 < len(keyList):
                    j1 = 0
                    objDict = {'key':keyList[i1],
                                'value':''}
                    while j1 < len(valueList):
                        indexes = getStartEndIndex(keyList[i1], keys)
                        keyIndStart = indexes[0]
                        keyIndEnd = indexes[1]
                        valInd = valueList[j1][1]
                        isIndexPresent = keyIndStart <= valInd and valInd <= keyIndEnd
                        if ((keyList[i1] in numericValueHeader and isNumeric(valueList[j1][0]))) or (keyList[i1] not in numericValueHeader):
                            if isIndexPresent:
                                flagI = 1
                                if len(objList) < len(keyList): 
                                    objDict['value'] = valueList[j1][0]
                                    valueList.remove(valueList[j1])
                                    break
                                else:
                                    newL = []
                                    for iterInd, iterVal in enumerate(objList):
                                        if iterVal['key'] == keyList[i1]:
                                            if type(objList[iterInd]['value']) is list:
                                                newL += objList[iterInd]['value']
                                            else:
                                                newL = [objList[iterInd]['value']]
                                            newL.append(valueList[j1][0])
                                            valueList.remove(valueList[j1])
                                            objList[iterInd]['value'] = newL
                                    # objDict['value'] = newL
                        j1 += 1
                    if len(objList) < len(keyList):
                        objList.append(objDict)
                    if i1 == len(keyList) - 1 and len(valueList) != 0:
                        print(valueList)
                        for keyI1, valI2 in enumerate(valueList):
                            print(valI2[1], len(textFileStr[i]))
                            if valI2[1] > len(textFileStr[i]):
                                valueList[keyI1][1] = valI2[1] - (len(textFileStr[i]) * (valI2[1] // len(textFileStr[i])))
                                i1 = -1
                    i1 += 1
                print(valueList)
                objLists.append(objList)
            c += 1
            i += 3
        else:
            i += 1
    objStr = json.dumps(objLists, indent=4)
    open('op.json', 'a')
    open('op.json', 'w').write(objStr)
    # for i in objLists:
    #     for j in i:
    #         print(j)
    #     print()
    print(objStr)

def getHeaderValueWithIndexRanges(l: list[str], s: str) -> dict[str, list[int]]:
    d = {}
    for i in l:
        d[i] = getStartEndIndex(i, s)
    return d

def constructStringForGivenLength(s: str, stdLength: int, ConstructBy=' ') -> str:
    sLen = len(s)
    newS = s
    if sLen != stdLength:
        newS = newS + (ConstructBy * (stdLength - sLen))
    return newS

def getStartEndIndex(s: str, strs: str) -> list[int]:
    start = strs.find(s)
    startInd = start
    endInd = start + len(s) - 1
    if start > 1 and endInd <= len(strs):
        i = start
        while strs[i - 1] == ' ':
            i -= 1
        startInd = i
    if (start == 0 and endInd <= len(strs)) or (start > 1 and endInd <= len(strs)):
        i = start + len(s) - 1
        while i < len(strs) - 1 and strs[i + 1] == ' ':
            i += 1
        endInd = i
    return [startInd, endInd]

def splitAndReturnValueWithIndex(s: str) -> list[list[str]]:
    i = 0
    valIndexes = []
    str = ''
    index = -1
    while i < len(s):
        if s[i] != ' ':
            str += s[i]
        elif (s[i] == ' ' or i == len(s) - 1) and str != '':
            index = i - len(str)
            valIndexes.append([str, index])
            str = ''
        if i == len(s) - 1 and str != '':
            valIndexes.append([str, i - (len(str) - 1)])
        i += 1
    return valIndexes

def isNumeric(s: str) -> bool:
    return s.replace('.', '').replace('-', '').isdigit()

if __name__ == '__main__':
    extractValue()
    # print(False == False)