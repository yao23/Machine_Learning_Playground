class Solution(object):
    # @param {integer[]} ratings
    # @return {integer}
    # beats 47.64%
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int

        use two pass scan from left to right and vice versa to keep the candy level up to now
        similar to like the Trapping Rain Water question
        """
        res = [1] * len(ratings)  # also compatible with [] input
        left_base = right_base = 1
        # left scan
        for i in xrange(1, len(ratings)):
            left_base = left_base + 1 if (ratings[i] > ratings[i - 1]) else 1
            res[i] = left_base
        # right scan
        for i in xrange(len(ratings)-2, -1, -1):
            right_base = right_base + 1 if (ratings[i] > ratings[i + 1]) else 1
            res[i] = max(right_base, res[i])
        return sum(res)
