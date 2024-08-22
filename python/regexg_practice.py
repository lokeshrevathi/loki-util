#regexg_practice
import  re

if __name__ == '__main__':
    # reg = '^(([/d]{1,5})|(([/d]{1,5})[-]{1}([/d]{1,5})))$'
    reg = '^(\d{1,5})-(?!\1\b)\d{1,5}$'
    s = '12345-123'
    if re.search(reg, s):
        print('yes')
    else:
        print('no')