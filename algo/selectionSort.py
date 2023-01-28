def selectionSort(array):
    # Write your code here.
    currentIndex = 0

    while currentIndex < len(array) - 1:
        smallIndex = currentIndex
        for i in range(currentIndex+1, len(array)):
            if array[smallIndex] > array[i]:
                smallIndex = i
        array[smallIndex], array[currentIndex] = array[currentIndex], array[smallIndex]
        currentIndex += 1
    return array
