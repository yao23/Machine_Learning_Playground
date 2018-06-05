class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        beats 44.70%
        """
        d1, d2 = [0 for _ in xrange(256)], [0 for _ in xrange(256)]
        for i in xrange(len(s)):
            if d1[ord(s[i])] != d2[ord(t[i])]:
                return False
            d1[ord(s[i])] = i+1
            d2[ord(t[i])] = i+1
        return True

    def isIsomorphic1(self, s, t):
        d1, d2 = {}, {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i]
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]
        return sorted(d1.values()) == sorted(d2.values())

    def isIsomorphic2(self, s, t):
        d1, d2 = [[] for _ in xrange(256)], [[] for _ in xrange(256)]
        for i, val in enumerate(s):
            d1[ord(val)].append(i)
        for i, val in enumerate(t):
            d2[ord(val)].append(i)
        return sorted(d1) == sorted(d2)

    def isIsomorphic3(self, s, t):
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

    def isIsomorphic4(self, s, t):
        return [s.find(i) for i in s] == [t.find(j) for j in t]

    def isIsomorphic5(self, s, t):
        return map(s.find, s) == map(t.find, t)
