# https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True

        return self.is_power_of_two(n, 1)

    def is_power_of_two(self, n, i):
        if i * 2 == n:
            return True
        if i * 2 > n:
            return False

        return self.is_power_of_two(n, i * 2)
        

solution = Solution()
print(solution.isPowerOfTwo(1))
print(solution.isPowerOfTwo(20))
print(solution.isPowerOfTwo(32))
print(solution.isPowerOfTwo(3))
