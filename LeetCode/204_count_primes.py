class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int

        https://leetcode.com/problems/count-primes/discuss/57595/

        primes[i * i: n: i] = [False] * len(primes[i * i: n: i])

        let's assume n == 100, we need to count all the primes which are less than 100:
        when i == 2:
        It will mark out the numbers as none-prime:
        4: 100 : 2 -> 4,6,8,10,12,14 ... 100
        which makes prime[4] = False, prime[6] = False, prime[8] = False...

        similarly:
        when i == 3:
        9: 100 : 3 -> 9,12,15,18,21,24 ... 96, 99
        when i == 4:
        16: 100 :4 -> 16,20,24,28 ... 96,100

        beats 96.13%
        """
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)

    def countPrimes1(self, n):
        """
        :param n:
        :return:

        cleaner solution than the above one with slicing

        beats 53.66%
        """
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = False
        return sum(primes)

    def countPrimes2(self, n):
        """
        :type n: int
        :rtype: int

        use 1, 0 instead of True, False, it will be faster .

        beats 100.00%
        """
        if n < 2:
            return 0
        s = [1] * n
        s[0] = s[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if s[i] == 1:
                s[i * i:n:i] = [0] * len(s[i * i:n:i])
        return sum(s)
