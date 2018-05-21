class Solution(object):
    def maximumGap(self, nums):
        """
        :param nums:
        :return:

        @param nums, a list of integer
        @return an integer
        """
        if len(nums) < 2 or max(nums) - min(nums) == 0:  # in case bsize == 0
            return 0
        max_n, min_n, len_n = max(nums), min(nums), len(nums)
        bsize = (max_n - min_n + 1.0) / len_n  # could have integer issue on OJ
        buckets = [[2 ** 31 - 1, -1] for _ in range(len_n + 1)]
        for i in nums:
            place = int((i - min_n) // bsize)
            buckets[place][0] = min(i, buckets[place][0])
            buckets[place][1] = max(i, buckets[place][1])
        res, prev = 0, buckets[0][0]
        for i in buckets:
            if i != [2 ** 31 - 1, -1]:
                res = max(res, i[0] - prev)
                prev = i[1]
        return res
