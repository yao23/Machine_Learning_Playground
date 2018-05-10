class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int

        beats 56.21%
        """
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                right, left = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(left + right)
                elif token == "-":
                    stack.append(left - right)
                elif token == "*":
                    stack.append(left * right)
                else:
                    # here take care of the case like "1/-22",
                    # in Python 2.x, it returns -1, while in
                    # Leetcode it should return 0
                    if left * right < 0 and left % right != 0:
                        stack.append(left / right + 1)
                    else:
                        stack.append(left / right)
        return stack.pop()
