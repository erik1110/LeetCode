def binarySearch(array, target):
    # Write your code here.
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right -= 1
        else:
            left += 1
    return -1
  
