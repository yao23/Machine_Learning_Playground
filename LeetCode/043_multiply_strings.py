class Solution(object):
    def multiply(num1, num2):
        """
        :param num2:
        :return:

        beats 29.37%
        """
        product = [0] * (len(num1) + len(num2))
        pos = len(product) - 1

        for n1 in reversed(num1):
            temp_pos = pos
            for n2 in reversed(num2):
                product[temp_pos] += int(n1) * int(n2)
                product[temp_pos - 1] += product[temp_pos] / 10
                product[temp_pos] %= 10
                temp_pos -= 1
            pos -= 1

        pt = 0
        while pt < len(product) - 1 and product[pt] == 0:
            pt += 1

        return ''.join(map(str, product[pt:]))

    def multiply0(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str

        beats 52.57%
        """
        res = [0] * (len(num1) + len(num2))
        for i, e1 in enumerate(reversed(num1)):
            for j, e2 in enumerate(reversed(num2)):
                res[i + j] += int(e1) * int(e2)
                res[i + j + 1] += res[i + j] / 10
                res[i + j] %= 10

        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return ''.join(map(str, res[::-1]))
