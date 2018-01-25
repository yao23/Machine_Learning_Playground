class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int

        "3+2*2" = 7
        " 3/2 " = 1
        " 3+5 / 2 " = 5

        collect all immediate results and add them finally
        stack: store previous numbers
        num: most recent number
        sign: most recent operator

        beats 95.56%
        """
        if not s:
            return "0"
        stack, num, sign = [], 0, "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord("0")
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s) - 1:
                if sign == "-":
                    stack.append(-num)
                elif sign == "+":
                    stack.append(num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                else:
                    tmp = stack.pop()
                    if tmp // num < 0 and tmp % num != 0:
                        stack.append(tmp // num + 1)
                    else:
                        stack.append(tmp // num)
                sign = s[i]
                num = 0
        return sum(stack)
