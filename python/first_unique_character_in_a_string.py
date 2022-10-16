# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        characters = {}
        for i in s:
            if i not in characters:
                characters[i] = 0

            characters[i] += 1

        n = 0
        for n, i in enumerate(s):
            if characters[i] == 1:
                return n

            n += 1

        return -1


solution = Solution()
print(solution.firstUniqChar("leetcode"))
print(solution.firstUniqChar("loveleetcode"))
