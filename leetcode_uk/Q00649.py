class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        r_q = deque()
        d_q = deque()
        for i in range(len(senate)):
            if senate[i] == "R":
                r_q.append(i)
            else:
                d_q.append(i)
        while r_q and d_q:
            r = r_q.popleft()
            d = d_q.popleft()
            if r < d:
                r_q.append(r+len(senate))
            else:
                d_q.append(d+len(senate))
        return "Radiant" if r_q else "Dire"
