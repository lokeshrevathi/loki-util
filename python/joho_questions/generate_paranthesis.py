#genetate_paranthesis
import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import valid_parantheses as vp
import util

def generateParanthesis(n: int) -> list[str]:
    pBuckets = ('(' * n) + (' ' * n)
    pPtr = n - 1
    ptr = pPtr
    genParanthesises = []
    i = 1
    while 0 < pPtr:
        genParanthesis = pBuckets.replace(' ', ')')
        print(genParanthesis)
        print(vp.isValid(genParanthesis))
        if (genParanthesis not in genParanthesises) and vp.isValid(genParanthesis):
            # print(genParanthesis)
            genParanthesises.append(genParanthesis)
        ptr = pPtr + i
        if ptr < (n * 2) -1:
            print(pPtr, ptr)
            pBuckets = util.swapCharInString(pBuckets, ptr - 1, ptr)
            i += 1
        else:
            pPtr -= 1
            i = 1
    return genParanthesises

if __name__ == '__main__':
    print(generateParanthesis(3))