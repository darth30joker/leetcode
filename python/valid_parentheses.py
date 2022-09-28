# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        previous = []
        
        matched = False
        
        for i in s:
            if not previous or i in ["(", "[", "{"]:
                previous.append(i)
                continue
                
            if i == ")" and previous[-1] == "(":
                previous.pop(-1)
                continue
                
            if i == "]" and previous[-1] == "[":
                previous.pop(-1)
                continue
                
            if i == "}" and previous[-1] == "{":
                previous.pop(-1)
                continue

            break
                
        if not previous:
            matched = True
            
        return matched


solution = Solution()
print(solution.isValid("{[]}"))
print(solution.isValid("{]}"))
print(solution.isValid("{[}"))
print(solution.isValid("(])"))
