class ValidWordAbbr(object):
    # beats 45.93%
    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.dic = collections.defaultdict(set)
        for s in dictionary:
            val = s
            if len(s) > 2:
                s = s[0] + str(len(s) - 2) + s[-1]
            self.dic[s].add(val)

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        val = word
        if len(word) > 2:
            word = word[0] + str(len(word) - 2) + word[-1]
        # if word abbreviation not in the dictionary, or word itself in the dictionary (word itself may
        # appear multiple times in the dictionary, so it's better using set instead of list)
        return len(self.dic[word]) == 0 or (len(self.dic[word]) == 1 and val == list(self.dic[word])[0])

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)