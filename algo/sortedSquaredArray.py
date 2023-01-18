'''

Write a function that takes in a non-empty array of integers that are sorted
in ascending order and returns a new array of the same length with the squares
of the original integers also sorted in ascending order.

'''
def sortedSquaredArray(array):
    res = []
    left = 0
    right = len(array) - 1
 
    while left <= right:
        left_num = array[left]**2
        right_num = array[right]**2
        if left_num > right_num:
            res.append(left_num)
            left += 1
        else:
            res.append(right_num)
            right -= 1

    return res[::-1]
