class Solution(object):
    # beats 62.23%
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        The smaller numbers on the right of a number are exactly those that jump from its right to its left during a
        stable sort. So I do merge sort with added tracking of those right-to-left jumps.
        """
        def sort(enum):
            half = len(enum) / 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])  # merge sort left and right parts
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:  # have smaller one in right
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

    def countSmaller2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        solution with Segment Tree

        beats 2.58%
        """
        hash_table = {v: i for i, v in enumerate(sorted(set(nums)))}

        tree, r = SegmentTree(len(hash_table)), []
        for i in xrange(len(nums) - 1, -1, -1):
            r.append(tree.sum(0, hash_table[nums[i]] - 1))
            tree.update(hash_table[nums[i]], 1)
        return r[::-1]

    def countSmaller3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        solution with Binary Index Tree

        beats 93.87%
        """
        hash_table = {v: i for i, v in enumerate(sorted(set(nums)))}

        tree, res = BinaryIndexedTree(len(hash_table)), []
        for i in xrange(len(nums) - 1, -1, -1):  # from right to left
            res.append(tree.sum(hash_table[nums[i]]))
            tree.update(hash_table[nums[i]] + 1, 1)
        return res[::-1]

    def countSmaller4(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        solution with Binary Search Tree

        beats 43.55%
        """
        tree = BinarySearchTree()
        return [
                   tree.insert(nums[i], tree.root)
                   for i in xrange(len(nums) - 1, -1, -1)
               ][::-1]

    def countSmaller5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        solution with Rank Tree

        beats 5.48%
        """
        rank_tree, res = RankTree(), []
        for elem in nums[::-1]:  # from right to left
            rank_tree.insert(elem)
            res.insert(0, rank_tree.get_rank(elem))
        return res


class BinaryIndexedTree(object):
    def __init__(self, n):
        self.sums = [0] * (n + 1)

    def update(self, i, val):
        while i < len(self.sums):
            self.sums[i] += 1
            i += i & -i  # length to find ancestor

    def sum(self, i):
        res = 0
        while i > 0:
            res += self.sums[i]
            i -= i & -i  # length to find ancestor
        return res


class SegmentTreeNode(object):
    def __init__(self, val, start, end):
        self.val = val
        self.start = start
        self.end = end
        self.children = []


class SegmentTree(object):
    def __init__(self, n):
        self.root = self.build(0, n - 1)

    def build(self, start, end):
        if start > end:
            return

        root = SegmentTreeNode(0, start, end)
        if start == end:
            return root

        mid = start + end >> 1
        root.children = filter(None, [
            self.build(start, end)
            for start, end in ((start, mid), (mid + 1, end))])
        return root

    def update(self, i, val, root=None):
        root = root or self.root
        if i < root.start or i > root.end:
            return root.val

        if i == root.start == root.end:
            root.val += val
            return root.val

        root.val = sum([self.update(i, val, c) for c in root.children])
        return root.val

    def sum(self, start, end, root=None):
        root = root or self.root
        if end < root.start or start > root.end:
            return 0

        if start <= root.start and end >= root.end:
            return root.val

        return sum([self.sum(start, end, c) for c in root.children])


class BinarySearchTreeNode(object):
    """
    similar like the following Rank Tree
    count and left_tree_size works like rank
    """
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.count = 1
        self.left_tree_size = 0


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, val, root):
        if not root:
            self.root = BinarySearchTreeNode(val)
            return 0

        if val == root.val:
            root.count += 1
            return root.left_tree_size

        if val < root.val:
            root.left_tree_size += 1

            if not root.left:
                root.left = BinarySearchTreeNode(val)
                return 0
            return self.insert(val, root.left)

        if not root.right:
            root.right = BinarySearchTreeNode(val)
            return root.count + root.left_tree_size

        return root.count + root.left_tree_size + self.insert(val, root.right)


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.rank = 0


class RankTree(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        def _insert(root, val):
            if not root:
                return TreeNode(val)
            if val <= root.val:
                root.left = _insert(root.left, val)
                root.rank += 1  # update count of smaller number for root
            if val > root.val:
                root.right = _insert(root.right, val)
            return root

        self.root = _insert(self.root, val)

    def get_rank(self, val):
        def _get_rank(root, val):
            if not root:
                return 0
            if root.val >= val:
                # Go left and look for rank of predecessor
                return _get_rank(root.left, val)
            else:
                # Go right and look for rank of successor
                return 1 + root.rank + _get_rank(root.right, val)

        return _get_rank(self.root, val)
