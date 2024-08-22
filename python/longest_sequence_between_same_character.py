#longest_sequence_between_same_character
def longestSequence(s: str) -> int:
    n = len(s)
    op = -1
    i = 0
    while i < n - 1:
        j = n - 1
        while j > i:
            if s[i] == s[j]:
                op = j - i - 1
                break
            j -= 1
        if j > i:
            break
        i += 1
    return op

if __name__ == '__main__':
    print(longestSequence("aab"))