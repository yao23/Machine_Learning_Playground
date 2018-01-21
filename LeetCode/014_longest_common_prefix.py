class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str

        beats 14.79%
        """
        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:  # the character in this position is the same for all the objects in strs
                return strs[0][:i]
        else:
            return min(strs)

    def longestCommonPrefix1(self, strs):
        """
        :type strs: List[str]
        :rtype: str

        beats 31.43%
        """
        if not strs:
            return ""
        else:
            return reduce(self.lcp, strs)

    def lcp(self, str1, str2):
        i = 0
        while i < len(str1) and i < len(str2):
            if str1[i] == str2[i]:
                i = i + 1
            else:
                break
        return str1[:i]
