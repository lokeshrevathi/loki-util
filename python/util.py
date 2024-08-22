#utilities
def replaceCharByIndex(str, index, char):
    if len(char) > 1:
        raise Exception("Charecter size must be one...")
    newL = list(str)
    newL[index] = char
    return ''.join(newL)

def swapCharInString(str, index1, index2):
    s1 = str[index1]
    s2 = str[index2]
    newStr = replaceCharByIndex(str, index1, s2)
    newStr = replaceCharByIndex(newStr, index2, s1)
    return newStr