# https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict = {}

        current_large_number = None
        current_repeat_times = 0

        for i in nums:
            if i not in num_dict:
                num_dict[i] = 0

            num_dict[i] += 1

            if current_repeat_times == 0:
                current_large_number = i
                current_repeat_times = 1

            if num_dict[i] > current_repeat_times:
                current_large_number = i
                current_repeat_times = num_dict[i]

        return current_large_number


solution = Solution()
        
print(solution.majorityElement([3, 2, 3]))
print(solution.majorityElement([2,2,1,1,1,2,2]))