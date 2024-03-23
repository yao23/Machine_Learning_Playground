class Solution(object):
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """
        https://www.youtube.com/watch?v=FzTYfsmtOso&list=PLot-Xpze53leOBgcVsJBEGrHPd_7x_koV&index=11
        
        beats 80.74%
        """
        seen, res = set(), set()

        for i in range(len(s) - 9): # need at least 10 characters
            cur = s[i : i + 10]
            if cur in seen: # seen before means repeated
                res.add(cur)
            seen.add(cur)
        return list(res)
        
    def findRepeatedDnaSequencesV0(self, s):
        """
        :type s: str
        :rtype: List[str]

        beats 67.21%
        """
        r, record = set(), set()
        for i in xrange(len(s) - 9):
            substring = s[i:i + 10]
            [record, r][substring in record].add(substring)
        return list(r)
