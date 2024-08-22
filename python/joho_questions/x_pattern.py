#x_pattern
def xPattern(s: str) -> None:
    for i in range(len(s)):
        for j in range(len(s)):
            if i == j or i + j == len(s) - 1:
                print(s[j], end='')
            else:
                print(' ', end='')
        print()

if __name__ == '__main__':
    xPattern('balamurugan')