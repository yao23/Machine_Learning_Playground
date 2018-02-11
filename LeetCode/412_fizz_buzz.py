class Solution(object):

    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]

        https://leetcode.com/problems/fizz-buzz/discuss/90007/Python-1-line-solution

        beats 60.57%
        """
        return [('Fizz' if i % 3 == 0 else '') + ('Buzz' if i % 5 == 0 else '') +
                (str(i) if not (i % 3 == 0 or i % 5 == 0) else '') for i in range(1, n + 1)]

    def fizzBuzz1(self, n):
        """
        :type n: int
        :rtype: List[str]

        beats 60.57%
        """
        return [str(i) if (i % 3 != 0 and i % 5 != 0) else (('Fizz' * (i % 3 == 0)) + ('Buzz' * (i % 5 == 0))) for i in
                range(1, n + 1)]

    def fizzBuzz2(self, n):
        """
        :type n: int
        :rtype: List[str]

        beats 32.08%
        """
        return [(not i % 3) * "Fizz" + (not i % 5) * "Buzz" or str(i) for i in range(1, n + 1)]

