# https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    roman_dict = dict(
        I=1,
        V=5,
        X=10,
        L=50,
        C=100,
        D=500,
        M=1000 
    )

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        number = 0

        previous_value = None

        for i in s:
            value = self.roman_dict[i]

            if not previous_value or (previous_value and previous_value >= value):
                number += value
                previous_value = value
            elif previous_value and previous_value < value:
                if value == 5 * previous_value or value == 10 * previous_value:
                    number -= previous_value
                    number += value - previous_value
                    previous_value = None

        return number


solution = Solution()
print(solution.romanToInt("III"))
print(solution.romanToInt("LVIII"))
print(solution.romanToInt("MCMXCIV"))
