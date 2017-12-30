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

    def candy1(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int

        use one pass scan from left to right

        beats 100.00%
        """
        ratings_len = len(ratings)
        if ratings_len == 0:
            return -1
        cur_sum = 1
        prev = 1
        down = 0
        for i in range(1, ratings_len):
            if ratings[i] < ratings[i - 1]:
                down += 1
            else:
                # check descend sequence before
                if down > 0:
                    # step 1: add from 1 to down
                    cur_sum += (down * (down + 1) // 2)
                    # step 2: add enough on prev
                    if down >= prev:
                        cur_sum += (down - prev + 1)
                    prev = 1
                    down = 0
                prev = 1 if (ratings[i] == ratings[i - 1]) else (prev + 1)
                cur_sum += prev
        if down > 0:
            cur_sum += (down * (down + 1) // 2)
            if down >= prev:
                cur_sum += (down - prev + 1)
        return cur_sum

