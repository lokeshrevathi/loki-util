#maximum_subarray
def maxSubArray(nums: list[int]) -> int:
    sum = 0
    max = nums[0]
    i = 0
    while i < len(nums):
        if sum + nums[i] > nums[i]:
            sum += nums[i]
        else:
            sum = nums[i]
        if sum <= 0:
            sum = 0
            sum += nums[i]
        if sum > max:
            max = sum
        i += 1
    return max

if __name__ == '__main__':
    nums = [5,4,-1,7,8]
    print(maxSubArray(nums))