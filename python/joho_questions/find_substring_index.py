#find_substring_index
def getSubStringIndex(s1: str, s2: str) -> int:
    i = 0
    j = 0
    while i < len(s1):
        if s1[i] == s2[j]:
            if j == len(s2) - 1:
                break
            i += 1
            j += 1
        else:
            i += 1
            j = 0
    if i < len(s1):
        return i - j
    else:
        return -1

if __name__ == '__main__':
    print(getSubStringIndex('testing12', '123'))