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

        https://leetcode.com/problems/candy/discuss/42770/
        test case: ratings = [0, 4, 5, 5, 2, 1, 0, 0]

        This solution picks each element from the input array only once. (use one pass scan from left to right)
        First, we give a candy to the first child. Then for each child we have three cases:

        His/her rating is equal to the previous one -> give 1 candy.
        His/her rating is greater than the previous one -> give him (previous + 1) candies.
        His/her rating is less than the previous one -> don't know what to do yet, let's just count the number of such
        consequent cases.

        When we enter 1 or 2 condition we can check our count from 3. If it's not zero then we know that we were
        descending before and we have everything to update our total candies amount: number of children in descending
        sequence of ratings - countDown, number of candies given at peak - prev (we don't update prev when descending).
        Total number of candies for "descending" children can be found through arithmetic progression formula
        (1+2+...+countDown). Plus we need to update our peak child if his number of candies is less then or equal to
        countDown.

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

