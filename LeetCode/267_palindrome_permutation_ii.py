from collections import Counter

class Solution(object):
    # beats 63.83%
    def combinations(self, chars, res, path=[]):
        if not chars:
            res.append(path)
            return
        i, n = 0, len(chars)
        while i < n:
            while 0 < i < n and chars[i] == chars[i - 1]:
                i += 1
            if i < n:
                c = chars.pop(i)
                self.combinations(chars, res, path + [c])
                chars.insert(i, c)
            i += 1
        return

    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        c, chars, odds = Counter(s), [], []
        for char in c:
            if not c[char] % 2:
                chars += [char] * (c[char] // 2)
            else:
                chars += [char] * ((c[char] - 1) // 2)
                odds += char,
        if len(odds) > 1:
            return []
        perms, odd, res = [], "" if not odds else odds[0], []
        self.combinations(chars, perms)
        for perm in perms:
            res.append("".join(perm + [odd] + perm[::-1]))
        return res