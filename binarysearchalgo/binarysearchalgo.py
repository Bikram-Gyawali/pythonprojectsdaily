# the program requires user with a list of numbers frm 0 to any range having diffence of 2
# when user inputs random number to be searched the program begins its search by dividing the list into two halves.the first half is checked first and if found next half is ignored /rejected and so on with the next half .the search occurs till user input is found or the subarray sizze becomes zero.this can be applied for any social media or e-platform with bundle of services

# implementing binary search

# with iteration method
def binarySearch(aList, item):
    first = 0
    last = len(aList)-1
    while first <= last:
        i = (first+last)//2
        if aList[i] == item:
            return '  found at positioin'.format(item=item, i=i)
        elif aList[i] > item:
            last = i-1
        elif aList[i] < item:
            first = i+1
        else:
            return ' not fofund in the list'.format(item=item)


def binarySearchRecursive(aList, item):
    first = 0
    last = len(aList)-1

    if len(aList) == 0:
        return ' was not found in the list'.format(item=item)
    else:
        i = (first+last)//2
        if item == aList[i]:
            return ' found'.format(item=item)
        else:
            if aList[i] < item:
                return binarySearchRecursive(aList[i+1:], item)
            else:
                return binarySearchRecursive(aList[:i], item)


print("binarySearch", binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 8))
print("binarysearchRecursive", binarySearchRecursive(
    [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 16))
