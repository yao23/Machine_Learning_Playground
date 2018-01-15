class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]

        beats 78.08%
        """
        dmap = dict([('2', 'abc'), ('3', 'def'), ('4', 'ghi'), ('5', 'jkl'), ('6', 'mno'), ('7', 'pqrs'), ('8', 'tuv'),
                     ('9', 'wxyz')])

        def generate_combination(digits):
            if len(digits) == 1:
                for c in dmap[digits[0]]:
                    yield (c,)
            else:
                for c in dmap[digits[0]]:  # every letter for current digit
                    the_rest = generate_combination(digits[1:])  # combination for later part after current digit
                    for r in the_rest:
                        yield (c,) + r

        if not digits:
            return []
        return list(''.join(t) for t in generate_combination(digits))

    mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def letterCombinations1(self, digits):
        """
        :type digits: str
        :rtype: List[str]

        beats 60.34%
        """
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(self.mapping[digits[0]])
        prev = self.letterCombinations(digits[:-1])
        additional = self.mapping[digits[-1]]
        return [s + c for s in prev for c in additional]

    def letterCombinations2(self, digits):
        """
        :type digits: str
        :rtype: List[str]

        # beats 44.38%
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

    def letterCombinations3(self, digits):
        """
        :type digits: str
        :rtype: List[str]

        backtracking solution
        beats 26.60%
        """
        digit_letters_map = dict([('2', 'abc'), ('3', 'def'), ('4', 'ghi'), ('5', 'jkl'), ('6', 'mno'), ('7', 'pqrs'),
                                  ('8', 'tuv'), ('9', 'wxyz')])
        res = []

        def dfs(depth, input_digits, tmp_res, res):
            if depth == len(input_digits):
                res.append(tmp_res)
            else:
                digit = input_digits[depth]
                letters = digit_letters_map[digit]
                for letter in letters:
                    dfs(depth + 1, input_digits, tmp_res + letter, res)

        if not digits:
            return []
        else:
            dfs(0, digits, "", res)
            return res

    def letterCombinations4(self, digits):
        """
        :type digits: str
        :rtype: List[str]

        backtracking solution
        beats 58.77%
        """
        if not digits:
            return []
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        self.dfs(digits, dic, 0, "", res)
        return res

    def dfs(self, digits, dic, index, path, res):
        if len(path) == len(digits):
            res.append(path)
            return
        for i in xrange(index, len(digits)):
            for j in dic[digits[i]]:
                self.dfs(digits, dic, i + 1, path + j, res)