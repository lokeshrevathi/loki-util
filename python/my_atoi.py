#my_atoi
def myAtoi(s: str) -> int:
    tempStr = '0'
    val = 0
    s = s.replace(' ', '')
    for index, i in enumerate(s):
        if i != '-' and i != '+' and (48 > ord(i) or ord(i) > 57):
            val = int(tempStr)
            return bound(val)
        elif (i == '-' or i == '+') and index == 0:
            j = index + 1
            count = 0
            while s[j] == '-' or s[j] == '+':
                count += 1
                j += 1
            if count == 0:
                if len(s) > 1:
                    tempStr = i
                else:
                    return 0
            else:
                return 0
        elif(i == '-' or i == '+') and index != 0:
            val = int(tempStr)
            return bound(val)
        else:
            tempStr += i
    val = int(tempStr)
    return bound(val)

def bound(val: int) -> int:
    lower_bound = -2**31
    upper_bound = 2**31 - 1
    if val < lower_bound:
        return lower_bound
    elif val > upper_bound:
        return upper_bound
    else:
        return val

if __name__ == '__main__':
    print(myAtoi('+-66'))