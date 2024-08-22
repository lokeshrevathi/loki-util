#valid_parantheses
def isValid(s: str) -> bool:
    if len(s) == 1:
        return False
    openBrackets = []
    for i in s:
        if i == '(' or i == '{' or i == '[':
            openBrackets.append(i)
        elif len(openBrackets) > 0:
            openBracket = openBrackets.pop()
            if ((openBracket == '(' and i == ')') or (openBracket == '[' and i == ']') or (openBracket == '{' and i == '}')) == False:
                return False
        else:
            return False
    if len(s) == len(openBrackets):
        return False
    if len(openBrackets) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    s = '()['
    print(isValid(s))