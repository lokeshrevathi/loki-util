#binary search
def binarySearch(dataList, targetElement, left, right):
    mid = left + ((right -left) // 2)
    if (left > right):
        return -1
    elif (dataList[mid] == targetElement):
        return mid + 1
    elif (dataList[mid] > targetElement):
        return binarySearch(dataList, targetElement, left, mid -1)
    elif (dataList[mid] < targetElement):
        return binarySearch(dataList, targetElement, mid + 1, right)
dataList = [1,3,4,5,6,9,10,11,12,13,14,15,17]
targetElement = 15
print(binarySearch(dataList, targetElement, 0, len(dataList) - 1), " ", len(dataList))