#zigzag_conversion
def zigzagConversion(s: str, numRows: int) -> str:
    l = [[] for i in range(numRows)]
    zc = 0
    i = 0
    k = 0
    j = 0
    if numRows <= 1:
        return s
    while True:
        while j < numRows and -1 < j and k != len(s):
            if zc % 2 == 0:
                l[j].append(s[k])
                j += 1
                k += 1
            else:
                l[j].append(s[k])
                j -= 1
                i += 1
                k += 1
        else:
            zc += 1
            if zc % 2 == 0 and k < len(s):
                j = 0
                l[j].pop()
                k -= 1
            elif k < len(s):
                j = numRows - 1
                l[j].pop()
                k -= 1
        if k == len(s):
            break
    return ''.join([j for i in l for j in i])


if __name__ == '__main__':
    print(zigzagConversion('PAYPALISHIRING', 1))