class RecentCounter(object):

    def __init__(self):
        self.time = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.time.append(t)
        while self.time[0] < t - 3000:
            self.time.popleft()
        return len(self.time)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)