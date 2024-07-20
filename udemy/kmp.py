def kmp(str1, str2):
    '''
    str1: 被搜尋
    str2: 關鍵字
    '''
    i = 0
    j = 0
    counter = 0

    # count str2 lps
    lps_list = lps(str2)

    while i < len(str1):
        if str1[i] == str2[j]:
            i += 1
            j += 1
            if len(str2) == j:
                counter += 1
                j = lps_list[j-1]
        else:
            if j > 0:
                j = lps_list[j-1]
            else:
                i += 1
    return counter

str1 = "ABCDABCDABD"
str2 = "ABCD"
kmp(str1, str2)
