# https://discuss.leetcode.com/topic/31561/some-python-solutions
class Solution(object):
    # beats 82.59%
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        rindex = {c: i for i, c in enumerate(s)}
        result = ''
        for i, c in enumerate(s):
            if c not in result:
                while c < result[-1:] and i < rindex[result[-1]]:
                    result = result[:-1]
                result += c
        return result

    # beats 70.31%
    def removeDuplicateLetters1(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        while s:
            i = min(map(s.rindex, set(s)))
            c = min(s[:i + 1])
            result += c
            s = s[s.index(c):].replace(c, '')
        return result

    # beats 43.69%
    def removeDuplicateLetters2(self, s):
        """
        :type s: str
        :rtype: str
        """
        for c in sorted(set(s)):
            suffix = s[s.index(c):]
            if set(suffix) == set(s):
                return c + self.removeDuplicateLetters(suffix.replace(c, ''))
        return ''