class NumArray(object):
    def __init__(self, nums):
        """
        :param nums:

        beats 76.75%
        """
        self.n = len(nums)
        self.a, self.c = nums, [0] * (self.n + 1)
        for i in range(self.n):
            k = i + 1
            while k <= self.n:
                self.c[k] += nums[i]
                k += (k & -k)

    def update(self, i, val):
        diff, self.a[i] = val - self.a[i], val
        i += 1
        while i <= self.n:
            self.c[i] += diff
            i += (i & -i)

    def sumRange(self, i, j):
        res, j = 0, j + 1
        while j:
            res += self.c[j]
            j -= (j & -j)
        while i:
            res -= self.c[i]
            i -= (i & -i)
        return res


class NumArray1(object):
    def __init__(self, nums):
        """
        :type nums: List[int]

        beats 22.88%
        """
        self.update = nums.__setitem__
        self.sumRange = lambda i, j: sum(nums[i:j + 1])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
