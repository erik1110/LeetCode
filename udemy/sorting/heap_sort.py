import math

arr = [15, 3, 17, 18, 20, 2, 1, 523, 3.4]

def buildMaxHeap(arr):
    heapSize = len(arr) - 1
    startIndex = math.floor(heapSize / 2)
    for i in range(startIndex, -1, -1):
        maxHeapify(i, arr, heapSize)
    return heapSize

def maxHeapify(i, arr, heapSize):
    l = i * 2 + 1
    r = i * 2 + 2
    if l <= heapSize and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r <= heapSize and arr[r] > arr[largest]:
        largest = r
    
    if largest != i:
        # swap
        temp = arr[i]
        arr[i] = arr[largest]
        arr[largest] = temp
        maxHeapify(largest, arr, heapSize)

def heapSort(arr):
    heapSize = buildMaxHeap(arr)
    for i in range(len(arr)-1, 0, -1):
        # exchange arr[0] with arr[i]
        temp = arr[0]
        arr[0] = arr[i]
        arr[i] = temp
        heapSize -=1
        maxHeapify(0, arr, heapSize)
    return arr


heapSort(arr)
# [1, 2, 3, 3.4, 15, 17, 18, 20, 523]