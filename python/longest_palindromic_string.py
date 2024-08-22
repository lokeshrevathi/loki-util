#longest_palindromic_string
def getLongestPalindromicString(s: str) -> str:
    palindromeStr = ''
    i = 0
    while i < len(s):
        j = i
        tempStr = ''
        while j < len(s):
            tempStr += s[j]
            if tempStr == tempStr[::-1] and len(tempStr) > len(palindromeStr):
                palindromeStr = tempStr
            j += 1
        i += 1
    return palindromeStr

if __name__ == '__main__':
    print(getLongestPalindromicString('frdmalayalamalayalakabas'))