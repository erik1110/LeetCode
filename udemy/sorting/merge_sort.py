
def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i == len(left):
        result.extend(right[j:])
    else:
        result.extend(left[i:])
    return result

def merge_sort(n):
    if len(n) == 1:
        return n
    else:
        middle = len(n) // 2
        left = n[:middle]
        right = n[middle:]
        return merge(merge_sort(left), merge_sort(right))
    
arr = [12, 11, 90, 5, 6]
merge_sort(arr)