#smalest_missing_integer
def smalestmissingInteger(nums: list[int]) -> int:
    i = 1
    while i in nums:
        i += 1
    else:
        return i

def smalestmissingIntegerWithOofN(nums: list[int]) -> int:
    

if __name__ == '__main__':
    print(smalestmissingInteger([1,2,3]))