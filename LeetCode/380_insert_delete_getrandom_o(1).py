import random


class RandomizedSet(object):
    """
    We just keep track of the index of the added elements, so when we remove them, we copy the last one into it.
    From Python docs (https://wiki.python.org/moin/TimeComplexity) we know that list.append() takes O(1),
    both average and amortized. Dictionary get and set functions take O(1) average, so we are OK.

    https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/85397/Simple-solution-in-Python

    beats 78.97%
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums, self.pos = [], {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            idx, last = self.pos[val], self.nums[-1]
            self.nums[idx], self.pos[last] = last, idx
            self.nums.pop()
            self.pos.pop(val, 0)
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]


class RandomizedSet1(object):
    """
    https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/85414/2-Python-implementations-using-dictionary-and-list-(Syned-and-Asyned)-with-explanationl

    beats 85.79%
    """
    def __init__(self):
        self.l = []
        self.d = {}

    def insert(self, val):
        if val in self.d:
            return False
        self.d[val] = len(self.l)
        self.l.append(val)
        return True

    def remove(self, val):
        if val not in self.d:
            return False
        i, new_val = self.d[val], self.l[-1]
        self.l[i], self.d[new_val] = new_val, i
        del self.d[val]
        self.l.pop()
        return True

    def getRandom(self):
        return random.choice(self.l)


class RandomizedSet2(object):
    """
    beats 45.13%
    """
    def __init__(self):
        self.l = []
        self.d = {}

    def insert(self, val):
        if val in self.d:
            return False
        i = len(self.d)
        self.d[val] = i
        if i < len(self.l):
            self.l[i] = val
        else:
            self.l.append(val)
        return True

    def remove(self, val):
        if val not in self.d:
            return False
        i, new_val = self.d[val], self.l[len(self.d) - 1]
        self.l[i], self.d[new_val] = new_val, i
        del self.d[val]
        return True

    def getRandom(self):
        return self.l[random.randrange(len(self.d))]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
