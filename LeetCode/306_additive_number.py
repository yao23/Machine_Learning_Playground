class Solution(object):
    # beats 17.86%
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if len(num) < 3:
            return False
        for i in range(len(num) // 2):
            for j in range(i + 1, len(num) // 3 * 2):
                one = int(num[:i + 1])
                two = int(num[i + 1:j + 1])
                if self.generate_fib_str(one, two, len(num)) == num:
                    return True
                if num[j] == 0:
                    break
            if num[0] == '0':
                break
        return False

    def generate_fib_str(self, a, b, n):
        # type: int, int, int -> str
        fib_str = str(a) + str(b)
        while len(fib_str) < n:
            fib_str += str(a + b)
            a, b = b, a + b
        return fib_str[:n]