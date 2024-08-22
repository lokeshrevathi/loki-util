#flames
def flames(n1: int, n2: int) -> str:
    flames = {'f':'Freind', 'l':'Love', 'a':'Affection', 'm':'Marraige', 'e':'Enemy', 's':'Sister'}
    emojie = {'f':'\U0001F49D', 'l':'\U0001F498', 'a':'\U0001F49B', 'm':'\U0001F935'+'\U0001F470', 'e':'\U0001F494', 's':'\U0001F478'}
    f = 'flames'
    a=list(n1)
    b=list(n2)
    i = 0
    while i < len(a):
        j = 0
        while j < len(b):
            if (i < len(a) and j < len(b)) and (a[i] != '' and b[j] != '') and a[i] == b[j]:
                a[i] = ''
                b[j] = ''
                i += 1
                j += 1
            else:
                j += 1
        i += 1
    c = len(''.join(a)) + len(''.join(b))
    i = 0
    while len(f) != 1:
        strikeIndex = (i + c) % len(f)
        strikeIndex -= 1
        l = list(f)
        l[strikeIndex] = ''
        f = ''.join(l)
        if strikeIndex == -1:
            i = len(f)
        else:
            i = strikeIndex
    print('Your\'s relationship is ',emojie[f], flames[f])  #U+1F610


if __name__ == '__main__':
    n1 = input('Enter your name => ').replace(' ', '').lower()
    n2 = input('Enter your crush name => ').replace(' ', '').lower()
    flames(n1, n2)