#num_subarray_product_less_than_K
import math
def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
        return findNoOfSubArray(nums,k)

def findNoOfSubArray(l: list[int], k: int, end=1, start=0, count=0, range=1) -> int:
    if 0 == end: end = start + range
    if range == len(l) + 1: return count
    print(l[start: end])
    count+=1
    if math.prod(l[start: end]) >= k:
        print(count)
        count -= 1
    if len(l) == end:
        range += 1
        start = 0
        end = start + range
    else:
        start += 1
        end += 1
    return findNoOfSubArray(l, k, end, start, count, range)

if __name__ == '__main__':
    print(numSubarrayProductLessThanK([1,1,1], 2))