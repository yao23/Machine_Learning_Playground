import re


class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str

        https://leetcode.com/problems/fraction-addition-and-subtraction/discuss/103389/Python-Gxc7D-Lxc7M

        beats 47.41%
        """

        def add(a, b):
            if a == "0/1":
                return b

            def gcd(a, b):
                while b != 0:
                    a, b = b, a % b
                return a

            (an, ad), (bn, bd) = map(int, a.split("/")), map(int, b.split("/"))
            lcm = (ad * bd) / (gcd(ad, bd))
            an, bn = an * (lcm / ad), bn * (lcm / bd)
            n = an + bn
            g = gcd(n, lcm)
            return str(n / g) + "/" + str(lcm / g)

        expression += "+"
        ans = "0/1"
        start = 0
        for i in range(1, len(expression)):
            if expression[i] in ["+", "-"]:
                num = expression[start:i]
                ans = add(ans, num)
                start = i
        return ans if ans[0] != "+" else ans[1:]

    def fractionAddition1(self, expression):
        """
        :type expression: str
        :rtype: str

        https://leetcode.com/problems/fraction-addition-and-subtraction/discuss/103383/two-python-solutions

        beats 12.93%
        """
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        nums = map(int, re.findall('[+-]?\\d+', expression))
        A, B = 0, 1
        for a, b in zip(nums[::2], nums[1::2]):
            A = A * b + B * a
            B *= b
            g = gcd(A, B)
            A /= g
            B /= g
        return '{0}/{1}'.format(A, B)