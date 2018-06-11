class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str

        beats 20.68%
        """
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s
