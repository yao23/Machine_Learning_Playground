class Solution(object):
    # Iterative
    # beats 59.50%
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in sorted(nums):
            res += [item+[num] for item in res]
        return res

    # DFS recursively
    def subsets1(self, nums):
        # beats 16.57%
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in xrange(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], res)

    # Bit Manipulation
    def subsets2(self, nums):
        res = []
        nums.sort()
        for i in xrange(1 << len(nums)):
            tmp = []
            for j in xrange(len(nums)):
                if i & 1 << j:  # if i >> j & 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res