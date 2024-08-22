#is_palindrome
def isPalindrome(x: int) -> bool:
    rev = 0
    if (x >= 0):
        temp = x
        while temp != 0:
            rev = (rev * 10) + (temp % 10)
            temp = temp // 10
        if rev == x:
            return True
        else:
            return False
    else:
        return False
    
if __name__ == '__main__':
    x = int(input("Enter a number to check palindrome or not: "))
    print(isPalindrome(x))