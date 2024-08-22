#length_of_longest_substring_in_given_string
def longest_sustring(s):
    s1 = []
    i = 0
    maxCount = 0
    sSize = len(s)
    while i < sSize:
        j = 0
        s1Size = len(s1)
        while j < s1Size:
            if s[i] == s1[j]:
                s1 = s1[j + 1 : s1Size]
                s1.append(s[i])
                break
            j += 1
        if j == s1Size:
            s1.append(s[i])
            maxCount = max(maxCount, len(s1))
            # count = len(s1)
            # if maxCount < count:
            #     maxCount = count
        i += 1
    return maxCount

if __name__ == '__main__':
    s = input()
    print(longest_sustring(s))