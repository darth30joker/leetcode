# https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter(object):

    def __init__(self):
        self.queue = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        if self.queue and t - self.queue[-1] > 3000:
            self.queue = []

        self.queue.append(t)

        n = 0
        for i in self.queue[::-1]:
            if t - i <= 3000:
                n += 1

        return n


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3001))
print(obj.ping(3002))
