#remove_vowels_with_length_one
def isToRemove(s: str, c: str) -> bool:
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    if vowels.__contains__(c) and len(s) - len(s.replace(c, "")) <= 1:
        return True
    return False

def removeVowelsInStr(s: str) -> str:
    newS = ''
    for i in s:
        if isToRemove(s, i) == False:
            newS += i
    return newS

if __name__ == '__main__':
    print(removeVowelsInStr("Compuuter"))