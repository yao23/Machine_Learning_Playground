class Solution(object):
    # beats 44.38%
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if '' == digits:
            return []
        kv_maps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return reduce(lambda acc, digit: [x + y for x in acc for y in kv_maps[digit]], digits, [''])
