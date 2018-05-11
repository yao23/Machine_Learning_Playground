class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str

        beats 99.84%
        """
        return " ".join(s.strip().split()[::-1])
