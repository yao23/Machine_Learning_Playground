class Solution:
    """
    https://www.youtube.com/watch?v=miZ3qV04b1g
    
    beats 25.62%
    """
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {}

        def dfs(i, m, n): #index, current m (num of 0), current n (num of 1s)
            if i == len(strs):
                return 0
            if (i, m, n) in dp:
                return dp[(i, m, n)]
            dp[(i, m, n)] = dfs(i + 1, m, n) # not take current str (strs[i])
            cntM, cntN = strs[i].count("0"), strs[i].count("1")
            if cntM <= m and cntN <= n:
                dp[(i, m, n)] = max(
                    dp[(i, m, n)],
                    1 + dfs(i + 1, m - cntM, n - cntN) # take current str (strs[i])
                )
            return dp[(i, m, n)]

        return dfs(0, m, n)

  """
  DP

  beats 13.56%
  """
  def findMaxFormV1(self, strs: List[str], m: int, n: int) -> int:
        dp = defaultdict(int)

        for s in strs:
            cntM, cntN = s.count("0"), s.count("1")
            for M in range(m, cntM - 1, -1): # reuse dp cache from last layer in reverse order and reduce DP dimension
                for N in range(n, cntN - 1, -1):
                    dp[(M, N)] = max(
                        dp[(M, N)], # not take current str (strs[i])
                        1 + dp[(M - cntM, N - cntN)] # take current str (strs[i])
                    )
        return dp[(m, n)]

  """
  DP

  beats 5.02%
  """
  def findMaxFormV0(self, strs: List[str], m: int, n: int) -> int:
        dp = defaultdict(int)

        for i in range(len(strs)):
            s = strs[i]
            cntM, cntN = strs[i].count("0"), strs[i].count("1")
            for M in range(m + 1):
                for N in range(n + 1):
                    dp[(i, M, N)] = dp[(i - 1, M, N)] # not take current str (strs[i])
            
                    if cntM <= M and cntN <= N:
                        dp[(i, M, N)] = max(
                            dp[(i, M, N)],
                            1 + dp[(i - 1, M - cntM, N - cntN)] # take current str (strs[i])
                        )
        return dp[(len(strs) - 1, m, n)]
