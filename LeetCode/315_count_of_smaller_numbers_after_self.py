class Solution(object):
    # beats 62.23%
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        The smaller numbers on the right of a number are exactly those that jump from its right to its left during a
        stable sort. So I do mergesort with added tracking of those right-to-left jumps.
        """
        def sort(enum):
            half = len(enum) / 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller

    def countSmaller1(self, nums):
        def sort(enum):
            half = len(enum) / 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                m, n = len(left), len(right)
                i = j = 0
                while i < m or j < n:
                    if j == n or i < m and left[i][1] <= right[j][1]:
                        enum[i + j] = left[i]
                        smaller[left[i][0]] += j
                        i += 1
                    else:
                        enum[i + j] = right[j]
                        j += 1
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller
