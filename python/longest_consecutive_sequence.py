# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        nums.sort()

        if len(nums) == 1:
            return 1

        start = 0
        end = 0
        res = 0

        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] == 1:
                end = i + 1

            if nums[i+1] - nums[i] > 1:
                temp = len(nums[start:end + 1])
                start = i + 1

                if temp > res:
                    res = temp
            
        temp = len(nums[start:end + 1])
        if temp > res:
            res = temp

        return res


solution = Solution()
print(solution.longestConsecutive([100,4,200,1,3,2]))
print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(solution.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))
