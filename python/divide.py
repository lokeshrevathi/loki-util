#divide
def divide(dividend: int, divisor: int) -> int:
    i = abs(divisor)
    count = 0
    if abs(dividend) == abs(divisor):
        count = 1
    elif abs(divisor) == 1:
        count = abs(dividend)
        i = abs(dividend)
    while i < abs(dividend):
        count += 1
        i += abs(divisor)
    if dividend < 0:
        count = -count
    if divisor < 0:
        count = -count
    return count

if __name__ == '__main__':
    print(divide(7, -3))