class Solution(object):
    # "((3+4)+5-4+2)+1" => 11
    # "((3+4)+5-4)" => 8
    # "2-(5-6)" => 3
    # beats 100.00%
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, num, sign, stack = 0, 0, 1, []
        for ss in s:
            if ss.isdigit():
                num = 10 * num + int(ss)
            elif ss in ["-", "+"]:
                res += sign * num  # last number
                num = 0
                sign = [-1, 1][ss == "+"]  # "+" for [-1, 1][1] = 1 and "-" for [-1, 1][0] = -1
            elif ss == "(":
                stack.append(res)  # last number
                stack.append(sign)  # last sign
                sign, res = 1, 0
            elif ss == ")":
                res += sign * num  # current number
                res *= stack.pop()  # "+" or "-"
                res += stack.pop()  # last number
                num = 0
        return res + num * sign

    # beats 58.91%
    def calculate1(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        i, signs = 0, [1, 1]
        while i < len(s):
            c = s[i]
            if c.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                total += signs.pop() * int(s[start:i])
                continue
            if c in '+-(':
                signs += signs[-1] * (1, -1)[c == '-'],
            elif c == ')':
                signs.pop()
            i += 1
        return total
