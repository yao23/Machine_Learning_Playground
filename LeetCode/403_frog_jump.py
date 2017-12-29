class Solution:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool

        beats 94.74%
        """
        if stones[1] != 1:
            return False
        stone_set, fail = set(stones), set()
        stack = [(0, 0)]
        while stack:
            stone, jump = stack.pop()
            for j in (jump-1, jump, jump+1):
                s = stone + j
                if j > 0 and s in stone_set and (s, j) not in fail:
                    if s == stones[-1]:
                        return True
                    stack.append((s, j))
            fail.add((stone, jump))
        return False

    def canCross1(self, stones):
        """
        :type stones: List[int]
        :rtype: bool

        beats 31.58%
        """
        if stones[1] != 1:
            return False
        # create a dictionary where the keys are the stones
        # and the values are empty sets that will contain
        # integers which represent the jump lengths that
        # can reach the stone represented by the key
        d = dict((x, set()) for x in stones)

        # catches a tricky test case: stones = [0,2]
        if stones[1] != 1:
            return False

        # the problems says that the first jump made is
        # always of length 1 and starts at stone 0. That
        # means the jump length that was used to reach
        # stone 1 is 1 so I add it into the set at stone 1
        d[1].add(1)

        # iterate over all the stones after 0
        for i in range(len(stones[1:])):

            # iterate over each jump length used to reach
            # the current stone
            for j in d[stones[i]]:

                # iterate over every jump length possible
                # (k-1, k, k+1) given the current jump length
                for k in range(j - 1, j + 2):

                    # if that jump length lands on a stone
                    if k > 0 and stones[i] + k in d:
                        # add that jump length used to get there to
                        # the set of jump lengths for the stone the
                        # jump puts the frog on
                        d[stones[i] + k].add(k)

        # if the last stone has any jump lengths in it's
        # set, that means that it is possible to get to
        # the last stone
        return d[stones[-1]] != set()
