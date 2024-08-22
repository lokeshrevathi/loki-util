#Find_nth_Value
def findNthValue(n, currentValue, count):
    if (n == count):
        return currentValue
    else :
        i = 0
        s = str(currentValue)
        while i < len(s):
            if (s[i] != "3" and s[i] != "4"):
                break
            i = i + 1
        if (i == len(s)):
            count = count +1
    return findNthValue(n, currentValue + 1, count)
n = int(input())
count = 1
print(findNthValue(n, 1, count))