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

    # beats 50.00%
    def calculate2(self, s):
        if s.isnumeric:
            if "(" not in s and ")" not in s and "+" not in s and "-" not in s:
                return s
        val_stack = []
        op_stack = []
        s = ''.join(s.split())  # trim space, like " 2-1 + 2 "
        i = 0
        for ss in s:
            if ss == "(":
                op_stack.append(ss)
            elif ss == ")":
                while op_stack[-1] != "(":
                    val_stack.append(self.cal(op_stack.pop(), val_stack.pop(), val_stack.pop()))
                op_stack.pop()
            elif ss in "+-*/":
                while op_stack and not self.is_higher_than(ss, op_stack[-1]):
                    val_stack.append(self.cal(op_stack.pop(), val_stack.pop(), val_stack.pop()))
                op_stack.append(ss)
            else:
                if i > 0 and s[i - 1].isdigit():  # append all digits, like 11 in "1-11"
                    ss = str(val_stack.pop()) + ss
                val_stack.append(int(ss))
            i += 1

        while op_stack:
            val_stack.append(self.cal(op_stack.pop(), val_stack.pop(), val_stack.pop()))

        return val_stack.pop()

    def cal(self, operator, operand1, operand2):
        if operator == "+":
            return operand1 + operand2
        else:
            return operand2 - operand1

    def is_higher_than(self, op1, op2):
        if op2 == "(":
            return op1 != "("
        else:
            return op2 in "+-" and op1 in "*/"
