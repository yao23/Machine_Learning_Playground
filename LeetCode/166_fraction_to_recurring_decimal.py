class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str

        use a stack to map remainders to their positions

        beats 18.08%
        """
        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator * denominator < 0 else ''
        result = [sign + str(n), '.']
        stack = []
        while remainder not in stack:
            stack.append(remainder)
            n, remainder = divmod(remainder * 10, abs(denominator))
            result.append(str(n))

        idx = stack.index(remainder)
        result.insert(idx + 2, '(')
        result.append(')')
        return ''.join(result).replace('(0)', '').rstrip('.')
