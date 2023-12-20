

def selection_sort(n):
    for i in range(len(n)):
        mini_index = i
        for j in range(i, len(n)):
            if n[j] < n[mini_index]:
                mini_index = j
        n[mini_index], n[i] = n[i], n[mini_index]
        
arr = [12, 11, 13, 5, 6]
selection_sort(arr)
print(arr)