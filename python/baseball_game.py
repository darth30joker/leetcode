# https://leetcode.com/problems/baseball-game/

class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        scores = []

        for i in operations:
            if i == "+":
                scores.append(scores[-1] + scores[-2])
            elif i == "D":
                scores.append(scores[-1] * 2)
            elif i == "C":
                scores.pop()
            else:
                scores.append(int(i))

        """ 
        n = 0
        for i in scores:
            n += i
        """

        return sum(scores)


solution = Solution()
print(solution.calPoints(["5", "2", "C", "D", "+"]))
print(solution.calPoints(["5","-2","4","C","D","9","+","+"]))
