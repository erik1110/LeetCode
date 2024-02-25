def partition(arr, p, r):
    x = arr[r] # pivot
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            # swap
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    temp = arr[i+1]
    arr[i+1] = arr[r]
    arr[r] = temp
    return i + 1
    
def quicksort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q - 1)
        quicksort(arr, q + 1, r)
    return arr
        
arr = [12, 3, 40, 13, -4, 10, 94, 100, -40, 3.41]

quicksort(arr, 0, len(arr) - 1)