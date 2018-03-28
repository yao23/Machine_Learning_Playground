class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]

        Recursive
        beats 94.46%
        """
        ans = []
        self.helper(ans, s, 4, [])
        return ['.'.join(x) for x in ans]

    def helper(self, ans, s, k, temp):
        if len(s) > k * 3:
            return
        if k == 0:
            ans.append(temp[:])
        else:
            for i in range(min(3, len(s) - k + 1)):
                if i == 2 and int(s[:3]) > 255 or i > 0 and s[0] == '0':
                    continue
                self.helper(ans, s[i + 1:], k - 1, temp + [s[:i + 1]])

    def restoreIpAddresses1(self, s):
        """
        :type s: str
        :rtype: List[str]

        Iterative
        beats 74.83%
        """
        res = []
        S = [([], s)]
        while S:
            l, s = S.pop()
            if len(l) == 4:
                if not s:
                    res.append('.'.join(l))
            elif len(s) <= (4 - len(l)) * 3:
                for i in range(min(3, len(s) - 3 + len(l))):
                    if i != 2 or s[:3] <= '255':
                        S.append((l + [s[:i + 1]], s[i + 1:]))
                    if s[0] == '0': break
        return res
