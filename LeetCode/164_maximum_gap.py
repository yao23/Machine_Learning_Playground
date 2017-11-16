class Solution(object):
    # @param nums, a list of integer
    # @return an integer
    def maximumGap(self, nums):
        if len(nums) < 2 or max(nums) - min(nums) == 0:  # in case bsize == 0
            return 0
        maxn, minn, lenn = max(nums), min(nums), len(nums)
        bsize = (maxn - minn + 1.0) / lenn  # could have interger issue on OJ
        buckets = [[2 ** 31 - 1, -1] for _ in range(lenn + 1)]
        for i in nums:
            place = int((i - minn) // bsize)
            buckets[place][0] = min(i, buckets[place][0])
            buckets[place][1] = max(i, buckets[place][1])
        res, prev = 0, buckets[0][0]
        for i in buckets:
            if i != [2 ** 31 - 1, -1]:
                res = max(res, i[0] - prev)
                prev = i[1]
        return res