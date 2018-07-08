class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]

        beats 81.54%
        """
        evenMidCandidate = ["11", "69", "88", "96", "00"]
        oddMidCandidate = ["0", "1", "8"]
        if n == 1:
            return oddMidCandidate
        if n == 2:
            return evenMidCandidate[:-1]
        if n % 2:
            pre, midCandidate = self.findStrobogrammatic(n - 1), oddMidCandidate
        else:
            pre, midCandidate = self.findStrobogrammatic(n - 2), evenMidCandidate
        premid = (n - 1) / 2
        return [p[:premid] + c + p[premid:] for c in midCandidate for p in pre]
