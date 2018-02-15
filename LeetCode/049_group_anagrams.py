class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]

        beats 26.12%
        """
        dic = {}
        for item in sorted(strs):
            sorted_item = ''.join(sorted(item))
            dic[sorted_item] = dic.get(sorted_item, []) + [item]
        return dic.values()
