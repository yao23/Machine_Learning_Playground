class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int

        beats 47.33%
        """
        return len(s.strip().split(' ')[-1])