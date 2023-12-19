'''
Write a function that collects all value in an array of arrays and return an array of values collected.
'''

class Solution:
    def getArray(self, array: list):
        result = []
        for i in range(len(array)):
            if isinstance(array[i], list):
                result.extend(self.getArray(array[i]))
            else:
                result.append(array[i])
        return result

s = Solution()
s.getArray([[[["a", [["b", ["c"]], ["d"]]], [["e"]], [[["f", "g", "h"]]]]]])

# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']