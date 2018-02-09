class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]

        https://discuss.leetcode.com/topic/32970/ac-soluiton-code

        beats 28.07%
        """
        if A is None or B is None:
            return None
        row_num_a, col_num_a, col_num_b = len(A), len(A[0]), len(B[0])
        if len(B) != col_num_a:
            raise Exception("A's column number must be equal to B's row number.")
        result = [[0 for _ in range(col_num_b)] for _ in range(row_num_a)]
        table_b = {}
        for k, row in enumerate(B):
            table_b[k] = {}
            for j, element_b in enumerate(row):
                if element_b:
                    table_b[k][j] = element_b
        for i, row in enumerate(A):
            for k, element_a in enumerate(row):
                if element_a:
                    for j, element_b in table_b[k].iteritems():
                        result[i][j] += element_a * element_b
        return result
