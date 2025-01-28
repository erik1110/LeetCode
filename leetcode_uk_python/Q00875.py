class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l = 1
        r = max(piles)
        while l < r:
            k = ( l + r ) // 2
            target = 0
            for pile in piles:
                # same with math.ceil(float(piles[i]) / float(k)) 
                # but more efficient
                target += (pile + k - 1) // k
            if target > h:
                l = k + 1
            else:
                r = k
        return l
