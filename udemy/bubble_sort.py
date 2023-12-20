
def bubble_sort(n):
    step = 0
    for i in range(len(n)-1):
        swapped = False
        for j in range(len(n)-1):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
                swapped = True
                step += 1
        if not swapped:
            break
    return n

my_list = [5, 4, 5, 91, 10, 11, 12, 13]
bubble_sort(my_list)