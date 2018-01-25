class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int

        A -> 1
        B -> 2
        C -> 3
        ...
        Z -> 26
        AA -> 27
        AB -> 28

        beats 23.59%
        """
        return sum((ord(char) - 64) * (26 ** exp) for exp, char in enumerate(s[::-1]))
