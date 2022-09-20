'''
12. Integer to Roman
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

'''
class Solution:
    def intToRoman(self, num: int) -> str:
        pum = {1: ["I", "V", "X"], 2: ["X", "L", "C"], 3: ["C", "D", "M"], 4: ["M", None, None]}
        val = num
        count = 0
        while num >= 1:
            num = num / 10
            count += 1
        result = ""
        for i in range(count, 0 , -1):
            result += self.romanChange(pum[i], int(str(val)[-i]))
        return result

    def romanChange(self, var, num):
        v1, v2, v3 = var[0], var[1], var[2]
        if var[2] is not None:
            result = {0: "",
                      1: v1,
                      2: v1 * 2,
                      3: v1 * 3,
                      4: v1 + v2,
                      5: v2,
                      6: v2 + v1,
                      7: v2 + v1 * 2,
                      8: v2 + v1 * 3,
                      9: v1 + v3}
        else:
            result = {0: "",
                      1: v1,
                      2: v1 * 2,
                      3: v1 * 3}
        return result[num]