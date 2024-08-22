#remove_duplicate_count_of_distinct_value
def remove_duplicate(duplicateList):
    distinctList = []
    i = 0
    length = len(duplicateList)
    while i < length:
        j = 0
        while j < i:
            if duplicateList[i] == duplicateList[j]:
                break
            j += 1
        if j == i:
            distinctList.append(duplicateList[i])
        i += 1
    return distinctList

if __name__ == "__main__":
    print(__name__)
    li = [1,1,2,3,4,5,5,5,6,7]
    print(len(remove_duplicate(li)))