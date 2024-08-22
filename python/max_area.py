#max_area

def maxValArea(height: list[int]) -> int:
    maxVal = 0
    left = 0
    right = len(height) - 1
    while left < right:
        val = min(height[left], height[right]) * (right - left)
        maxVal = max(maxVal, val)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return maxVal

if __name__ == '__main__':
    print(maxValArea([]))
    s = int('1' + ('0' * 0))
    print(s)