class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        height = 0
        max_h = 0
        for i in range(len(gain)):
            height += gain[i]
            max_h = max(max_h, height)
        return max_h
