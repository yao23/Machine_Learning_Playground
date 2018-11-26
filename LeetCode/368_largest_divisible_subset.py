class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        beats 97.62%
        """
        S = {-1: set()}
        for x in sorted(nums):
            S[x] = max((S[d] for d in S if x % d == 0), key=len) | {x}
        return list(max(S.values(), key=len))

# My S[x] is the largest subset with x as the largest element, i.e., the subset of all divisors of x in the input.
# With S[-1] = emptyset as useful base case. Since divisibility is transitive, a multiple x of some divisor d is also
# a multiple of all elements in S[d], so it's not necessary to explicitly test divisibility of x
# by all elements in S[d]. Testing x % d suffices.

# While storing entire subsets isn't super efficient, it's also not that bad. To extend a subset,
# the new element must be divisible by all elements in it, meaning it must be at least twice as large as
# the largest element in it. So with the 31-bit integers we have here, the largest possible set has size 31
# (containing all powers of 2).
