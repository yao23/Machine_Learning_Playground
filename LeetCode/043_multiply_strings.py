class Solution(object):
    # beats 29.37%
    def multiply(num1, num2):
        product = [0] * (len(num1) + len(num2))
        pos = len(product) - 1

        for n1 in reversed(num1):
            tempPos = pos
            for n2 in reversed(num2):
                product[tempPos] += int(n1) * int(n2)
                product[tempPos - 1] += product[tempPos] / 10
                product[tempPos] %= 10
                tempPos -= 1
            pos -= 1

        pt = 0
        while pt < len(product) - 1 and product[pt] == 0:
            pt += 1

        return ''.join(map(str, product[pt:]))

    # beats 52.57%
    def multiply0(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0] * (len(num1) + len(num2))
        for i, e1 in enumerate(reversed(num1)):
            for j, e2 in enumerate(reversed(num2)):
                res[i + j] += int(e1) * int(e2)
                res[i + j + 1] += res[i + j] / 10
                res[i + j] %= 10

        while len(res) > 1 and res[-1] == 0: res.pop()
        return ''.join(map(str, res[::-1]))