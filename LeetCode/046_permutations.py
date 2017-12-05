class Solution(object):
    # Recursive, take any number as first
    # Take any number as the first number and append any permutation of the other numbers
    # beats 9.16%
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return [[n] + p
            for i, n in enumerate(nums)
            for p in self.permute(nums[:i] + nums[i+1:])] or [[]]

    # Recursive, insert first number anywhere
    # Insert the first number anywhere in any permutation of the remaining numbers
    def permute1(self, nums):
        return nums and [p[:i] + [nums[0]] + p[i:]
                         for p in self.permute(nums[1:])
                         for i in range(len(nums))] or [[]]

    # Reduce, insert next number anywhere
    # Use reduce to insert the next number anywhere in the already built permutations
    def permute2(self, nums):
        return reduce(lambda P, n: [p[:i] + [n] + p[i:]
                                    for p in P for i in range(len(p) + 1)],
                      nums, [[]])

    # Using the library
    def permute3(self, nums):
        return list(itertools.permutations(nums))

    def permute4(self, nums):
        return map(list, itertools.permutations(nums))