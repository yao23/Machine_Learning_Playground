class Solution(object):
    # DP, O(n) space
    # beats 80.27%
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        r, c, l= len(s1), len(s2), len(s3)
        if r+c != l:
            return False
        dp = [True for _ in xrange(c+1)]
        for j in xrange(1, c+1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
        for i in xrange(1, r+1):
            dp[0] = (dp[0] and s1[i-1] == s3[i-1])
            for j in xrange(1, c+1):
                dp[j] = (dp[j] and s1[i-1] == s3[i-1+j]) or (dp[j-1] and s2[j-1] == s3[i-1+j])
        return dp[-1]

    # DFS
    # beats 97.99%
    def isInterleave1(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        dp_row, dp_col, dp_len = len(s1), len(s2), len(s3)
        if dp_row + dp_col != dp_len:
            return False
        stack, visited = [(0, 0)], set((0, 0))
        while stack:
            x, y = stack.pop()
            if x + y == dp_len:
                return True
            if x + 1 <= dp_row and s1[x] == s3[x + y] and (x + 1, y) not in visited:
                stack.append((x + 1, y))
                visited.add((x + 1, y))
            if y + 1 <= dp_col and s2[y] == s3[x + y] and (x, y + 1) not in visited:
                stack.append((x, y + 1))
                visited.add((x, y + 1))
        return False

    # BFS
    # beats 97.99%
    def isInterleave2(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        r, c, l = len(s1), len(s2), len(s3)
        if r + c != l:
            return False
        queue, visited = [(0, 0)], set((0, 0))
        while queue:
            x, y = queue.pop(0)
            if x + y == l:
                return True
            if x + 1 <= r and s1[x] == s3[x + y] and (x + 1, y) not in visited:
                queue.append((x + 1, y));
                visited.add((x + 1, y))
            if y + 1 <= c and s2[y] == s3[x + y] and (x, y + 1) not in visited:
                queue.append((x, y + 1));
                visited.add((x, y + 1))
        return False