import itertools


class Solution(object):
    """
    beats 49.62%
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(depth, perm):
            if depth == len(nums):
                res.append(perm.copy())
                return

            for i in range(depth, len(nums)):
                nums[i], nums[depth] = nums[depth], nums[i]
                perm.append(nums[depth])
                backtrack(depth + 1, perm)
                perm.pop()
                nums[i], nums[depth] = nums[depth], nums[i]

        backtrack(0, [])

        return res

    def permuteV4(self, nums: List[int]) -> List[List[int]]:
        """
        https://www.youtube.com/watch?v=s7AvT7cGdSo
        
        beats 83.41%
        """
        res = []

        # base case
        if len(nums) == 1:
            return [nums[:]]  # nums[:] is a deep copy

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permuteV4(nums)

            for perm in perms: # [2,3], [3,2]
                perm.append(n) # [2,3,1], [3,2,1]
            res.extend(perms) # add multi list
            nums.append(n)
        return res

    def helper_method(self, nums, nums_len, depth, result):
        """
        :param nums:
        :param nums_len:
        :param depth:
        :param result:
        :return:

        swap current index with pivot one to generate new permutation
        """
        if depth == nums_len:
            tmp_res = list(nums)
            result.append(tmp_res)
            return

        for i in range(depth, nums_len):
            if i != depth:
                nums[depth], nums[i] = nums[i], nums[depth]
                self.helper_method(nums, nums_len, depth + 1, result)
                nums[depth], nums[i] = nums[i], nums[depth]
            else:
                self.helper_method(nums, nums_len, depth + 1, result)

    def permute5(self, nums):
        """
        :param nums:
        :return:

        beats 58.61%
        """
        result = []
        nums_len = len(nums)
        self.helper_method(nums, nums_len, 0, result)

        return result

    def permuteV0(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Recursive, take any number as first
        Take any number as the first number and append any permutation of the other numbers
        beats 9.16%
        """
        return [[n] + p
            for i, n in enumerate(nums)
            for p in self.permute(nums[:i] + nums[i+1:])] or [[]]

    def permute1(self, nums):
        """
        :param nums:
        :return:

        Recursive, insert first number anywhere
        Insert the first number anywhere in any permutation of the remaining numbers
        """
        return nums and [p[:i] + [nums[0]] + p[i:]
                         for p in self.permute(nums[1:])
                         for i in range(len(nums))] or [[]]

    def permute2(self, nums):
        """
        :param nums:
        :return:

        Reduce, insert next number anywhere
        Use reduce to insert the next number anywhere in the already built permutations
        """
        return reduce(lambda P, n: [p[:i] + [n] + p[i:]
                                    for p in P for i in range(len(p) + 1)],
                      nums, [[]])

    def permute3(self, nums):
        """
        :param nums:
        :return:

        Using the library
        """
        return list(itertools.permutations(nums))

    def permute4(self, nums):
        return map(list, itertools.permutations(nums))
