#jump_game
def canJump(nums: list) -> bool:
    # val = getValidIndex(nums, 0, nums[0])
    currentIndex = nums[0]
    stepMoved = nums[0]
    i = nums[0] - 1
    if len(nums) - 1 <= currentIndex or len(nums) == 1:
        return True
    while i < len(nums):
        if stepMoved > 0:
            val = getValidIndex(nums, currentIndex, nums[i])
            currentIndex += nums[val]
            stepMoved = nums[val]
        if i < currentIndex:
            i = currentIndex
        else:
            i += 1
        if currentIndex >= len(nums) - 1:
            i = len(nums) - 1
            break
    if i == len(nums):
        print(currentIndex, len(nums))
        return False
    else:
        print(currentIndex, len(nums))
        return True
    
def getValidIndex(nums: list, currentIndex: int, value: int) -> int:
    index = -1
    max = 0
    i = currentIndex + 1
    while i < currentIndex + value:
        if nums[i] > max:
            max = nums[i]
            index = i
        i += 1
    return index
    
if __name__ == '__main__':
    nums = [3,2,1,0,4]
    print(canJump(nums))