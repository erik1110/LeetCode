def permutations(arr):
    # 基礎情況：如果 arr 長度為 1，返回包含這個單一元素的列表
    if len(arr) == 1:
        return [arr]

    # 結果列表，用於儲存所有排列
    result = []

    # 遍歷 arr 中的每個元素
    for i in range(len(arr)):
        # 當前元素
        current = arr[i]
        # 剩餘元素列表
        remaining = arr[:i] + arr[i+1:]

        # 遞歸計算剩餘元素的排列
        for perm in permutations(remaining):
            # 將當前元素插入到排列的每個位置
            result.append([current] + perm)
    
    return result

# 測試
test_list = ['A', 'B', 'C']
print(permutations(test_list))
