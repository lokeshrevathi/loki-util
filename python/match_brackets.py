#match_brackets
def isValidBrackets(s: str) -> int:
    sbStack = []
    pStack = []
    count = 0
    i = 0
    while i < len(s):
        if s[i] == '(':
            sbStack.append(s[i])
        elif s[i] == ')' and len(sbStack) > 0:
            sbStack.pop()
        elif s[i] == ')' and len(sbStack) == 0:
            break
        i += 1
    if len(sbStack) == 0:
        count = s.count('(')
    if i < len(s): count = 0
    print(count)

if __name__ == '__main__':
    isValidBrackets('(()hihello(loki(()))')