
def insertion_sort(n):
    for i in range(1, len(n)):
        key = n[i]
        j = i - 1
        # 大於 key 的數字往後挪
        while j >= 0 and key < n[j]:
            n[j+1] = n[j]
            j -= 1
        # 最後再將 key 補在應該插入的位置
        n[j+1] = key

arr = [10, 11, 13, 12, 6]
insertion_sort(arr)
print(arr)