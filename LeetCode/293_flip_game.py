class Solution(object):
    # beats 89.85%
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return [s[:i] + "--" + s[i + 2:] for i in range(len(s) - 1) if s[i] == s[i + 1] == "+"]