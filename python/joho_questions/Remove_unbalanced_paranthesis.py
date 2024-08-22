#Remove_unbalanced_paranthesis
def removeParanthesis(s, i):
    l = list(s)
    l.remove(i)
    return str(l)
ipString = input()
checkParanthesis = []
ipString = ipString if (ipString[0] == ")") else removeParanthesis(ipString, 0)
for i in range(0, len(ipString)):
    if i == 0 and ipString[i] == "(" :
        checkParanthesis.append(ipString[i])
    else :
        if len(checkParanthesis) > 0 :
            if checkParanthesis.