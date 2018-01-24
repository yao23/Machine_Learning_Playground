import collections


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool

        beats 28.43%
        """
        return not collections.Counter(ransomNote) - collections.Counter(magazine)

    def canConstruct1(self, ransomNote, magazine):
        """
        :param ransomNote:
        :param magazine:
        :return:

        beats 41.25%
        """
        letter_map = {}
        for letter in ransomNote:
            if letter in letter_map:
                letter_map[letter] += 1
            else:
                letter_map[letter] = 1
        for letter in magazine:
            if letter in letter_map:
                letter_map[letter] -= 1

        for letter in ransomNote:
            if letter_map[letter] > 0:
                return False
        return True
