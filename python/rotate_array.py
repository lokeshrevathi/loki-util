#rotate_array
def rotate(nums: list[int], k: int) -> None:
    rotatedNums = nums.copy()
    nums.clear()
    if k % len(rotatedNums) == len(rotatedNums) or k % len(rotatedNums) == 0:
        i = 0
    else:
        i = len(rotatedNums) - (k % len(rotatedNums))
    endCondition = len(rotatedNums)
    while i < endCondition:
        nums.append(rotatedNums[i])
        if i == len(rotatedNums) - 1 and (k % len(rotatedNums) != len(rotatedNums) and k % len(rotatedNums) != 0):
            i = 0
            endCondition = len(rotatedNums) - (k % len(rotatedNums))
        else:
            i += 1
    for j in rotatedNums:
        print(j, end=' ')
        

if __name__ == '__main__':
    rotate(nums=[1], k=14)