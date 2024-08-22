#adjecent_times
def adjacentTimes(s: str) -> str:
    n = len(s)
    c = ''
    op = ''
    i = 0
    while i < n:
        if ord(s[i]) < 48 or 57 < ord(s[i]):
            c = s[i]
            i += 1
            continue
        num = 0
        while i < n and 48 <= ord(s[i]) and ord(s[i]) <= 57:
            num = num * 10 + int(s[i])
            i += 1
        else:
            op = op + (str(c) * num)
    return op

if __name__ == '__main__':
    ip = "a10b20c100"
    print("input = ", ip)
    print("output = ", adjacentTimes(ip))