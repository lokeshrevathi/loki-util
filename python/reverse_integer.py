#reverse_integer
def reverse(x: int) -> int:
    print(x.bit_length())
    if x.bit_length() > 30:
        if x < 0:
            return x
        return 0
    temp = abs(x)
    rev = 0
    while temp:
        rem = temp % 10
        rev = (rev * 10) + rem
        temp //= 10
    if x < 0:
        return rev * -1
    return rev

if __name__ == '__main__':
    print(reverse(-2147483412))