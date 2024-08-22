#integer_to_roman
def intToRoman(num: int) -> str:
    romanDict = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM'}
    romanStr = ''
    temp = num
    numCount = len(str(num))
    i = 1
    while i <= numCount:
        rem = temp % 10
        temp //= 10
        rem = int(str(rem) + ('0' * (i - 1)))
        if rem in romanDict:
            romanStr = romanDict[rem] + romanStr
        else:
            firstNum = int(str(rem)[0])
            if firstNum != 6 and firstNum // 6 == 0:
                romanStr = (romanDict[int('1' + ('0' * (i - 1)))] * firstNum) + romanStr
            else:
                romanStr = romanDict[int('5' + ('0' * (i - 1)))] + (romanDict[int('1' + ('0' * (i - 1)))] * (firstNum - 5)) + romanStr
        i += 1
    return romanStr

if __name__ == '__main__':
    intToRoman(60)