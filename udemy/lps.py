def lps(word):
    '''
    只要 word[i] != word[j] 不相同 
    lps[j-1] 可以說明在 i 之前部分匹配的長度，並嘗試從這個新的位置繼續匹配，就不用重新計算
    '''
    j = 0
    i = 1
    lps = [0] * len(word)
    while i < len(word):
        if word[i] == word[j]:
            lps[i] = j + 1
            i += 1
            j += 1
        else:
            if j > 0:
                j = lps[j-1]
            else:
                lps[i] = 0
                i += 1
    return lps

word = "AABAACAABAA"
lps(word)
# [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]