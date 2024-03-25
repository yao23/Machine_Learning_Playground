class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        """
        https://www.youtube.com/watch?v=O761YBjGxGA&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=29

        beats 13.67%
        """
        dp = {(1, 1) : 1} # key - (N, K), value - num of arrangements

        for N in range(2, n + 1):
            for K in range(1, k + 1):    
                dp[(N, K)] = dp.get((N - 1, K - 1), 0) + (N - 1) * dp.get((N - 1, K), 0) #dp[(3, 3)] = dfs(2, 2) + 2 * dfs(2, 3)
        
        return dp[(n, k)] % (10 ** 9 + 7)
    
    def rearrangeSticksV0(self, n: int, k: int) -> int:
        """
        memory limit exceed
        """
        dp = {} # key - N, value - K

        def dfs(N, K):
            if N == K: # n = 3, k = 3 => [1, 2, 3]
                return 1
            if N == 0 or K == 0:
                return 0
            if (N, K) in dp:
                return dp[(N, K)]
            dp[(N, K)] = dfs(N - 1, K - 1) + (N - 1) * dfs(N - 1, K) #dp[(3, 3)] = dfs(2, 2) + 2 * dfs(2, 3)
            return dp[(N, K)]
        
        return dfs(n, k) % (10**9 + 7)
