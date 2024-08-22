#double_arrow_pattern
def double_arrow_triangle(arrowSize: int) -> None:
    i = 0
    halfHeight = arrowSize // 2
    fullHeight = (halfHeight * 2) - 1
    lengthIndex = 0
    secondHalfCount = 2
    while i < fullHeight:
        if (i // halfHeight) == 0:
            lengthIndex = i
        else:
            lengthIndex = i - secondHalfCount
            secondHalfCount += 2
        j = 0
        while j < halfHeight * 2:
            if (lengthIndex - (j % halfHeight)) >= 0:
                print('*', end='')
            else:
                print(' ', end='')
            j += 1
        print()
        i += 1

if __name__ == '__main__':
    n = int(input())
    double_arrow_triangle(n)