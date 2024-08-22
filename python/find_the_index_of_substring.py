#find_the_index_of_substring
def getSubStringIndex(hayStack: str, needle: str) -> int:
    subStringSize = len(needle)
    i = 0
    while i < len(hayStack):
        j = 0
        # innerI = i
        while j < subStringSize and i < len(hayStack):
            if hayStack[i] != needle[j]:
                break
            else:
                i += 1
                j += 1
        if j == subStringSize:
            i -= j
            break
        else:
            i -= j
        i += 1
    if i < len(hayStack):
        return i
    else:
        return -1
    
if __name__ == '__main__':
    s1 = "leetcode"
    s2 = "leeto"
    print(getSubStringIndex(s1, s2))