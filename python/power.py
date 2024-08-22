#power
def myPow(x: float, n: int) -> float:
    m = 0
    p = 1
    a = 1
    if (n >= 0):
        m = n
    else:
        m = n * (-1)
    for i in range(m):
        p = p * x
    if (n >= 0):
        return p
    else:
        return (1/p)
    
if __name__ == '__main__':
    print(myPow(4, 3), " ", pow(4, 3))