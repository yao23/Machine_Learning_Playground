import collections


class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        https://leetcode.com/problems/valid-triangle-number/discuss/104164/Can-this-problem-possibly-be-solved-by-python

        beats 64.31%
        """
        ans = 0
        nums.sort()
        for i in range(2, len(nums)):
            start = 0
            end = i - 1
            while start < end:
                if nums[start] + nums[end] > nums[i]:
                    ans += end - start
                    end -= 1
                else:
                    start += 1
        return ans

    def triangleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        https://leetcode.com/problems/valid-triangle-number/discuss/104187/Python-O(n2)-solution-526-ms

        beats 27.14%
        """
        nums = sorted(nums)
        total = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                continue
            end = i + 2
            for j in range(i + 1, len(nums) - 1):
                while end < len(nums) and nums[end] < (nums[i] + nums[j]):
                    end += 1
                total += end - j - 1
        return total

    def triangleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        https://leetcode.com/problems/valid-triangle-number/discuss/104179/Python-O(n2)

        beats 84.76%
        """
        nums.sort()
        nums = nums[::-1]
        sol = 0
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                diff = nums[i] - nums[j]
                while nums[k] <= diff and k > j:
                    k -= 1
                sol += (k - j)
                j += 1
        return sol

    def triangleNumber3(self, A):
        """
        :type nums: List[int]
        :rtype: int

        https://leetcode.com/problems/valid-triangle-number/discuss/104204/Python-Straightforward-with-Explanation

        Sort the array. For every pair of sticks u, v with stick u occuring before v (u <= v), we want to know how many
        w occuring after v have w < u + v.

        For every middle stick B[j] = v, we can use two pointers: one pointer i going down from j to 0, and one pointer
        k going from the end to j. This is because if we have all w such that w < u + v, then decreasing u cannot make
        this set larger.

        Let's look at an extension where our sorted array is grouped into counts of it's values. For example, instead
        of dealing with A = [2,2,2,2,3,3,3,3,3,4,4,4], we should deal with only B = [2, 3, 4] and keep a sidecount of
        C[2] = 4, C[3] = 5, C[4] = 3. We'll also keep a prefix sum
        P[k] = C[B[0]] + C[B[1]] + ... + C[B[k-1]] (and P[0] = 0.)

        When we are done setting our pointers and want to add the result, we need to add the result taking into
        account multiplicities (how many times each kind of triangle occurs.) When i == j or j == k, this is a little
        tricky, so let's break it down case by case.

        When i < j, we have C[B[i]] * C[B[j]] * (P[k+1] - P[j+1]) triangles where the last stick has a value > B[j].
        Then, we have another C[B[i]] * (C[B[j]] choose 2) triangles where the last stick has value B[j].
        When i == j, we have (C[B[i]] choose 2) * (P[k+1] - P[j+1]) triangles where the last stick has value > B[j].
        Then, we have another (C[B[i]] choose 3) triangles where the last stick has value B[j].


        beats 46.47%
        """
        C = collections.Counter(A)
        C.pop(0, None)
        B = sorted(C.keys())
        P = [0]
        for x in B:
            P.append(P[-1] + C[x])

        ans = 0
        for j, v in enumerate(B):
            k = len(B) - 1
            i = j
            while 0 <= i <= j <= k:
                while k > j and B[i] + B[j] <= B[k]:
                    k -= 1
                if i < j:
                    ans += C[B[i]] * C[B[j]] * (P[k + 1] - P[j + 1])
                    ans += C[B[i]] * C[B[j]] * (C[B[j]] - 1) / 2
                else:
                    ans += C[B[i]] * (C[B[i]] - 1) / 2 * (P[k + 1] - P[j + 1])
                    ans += C[B[i]] * (C[B[i]] - 1) * (C[B[i]] - 2) / 6
                i -= 1
        return ans