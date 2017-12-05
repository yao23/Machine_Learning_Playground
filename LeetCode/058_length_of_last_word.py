class Solution(object):
    # beats 47.33%
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(' ')[-1])