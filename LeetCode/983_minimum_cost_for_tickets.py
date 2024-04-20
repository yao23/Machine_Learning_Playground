class Solution:
    """
    https://www.youtube.com/watch?v=4pY1bsBpIY4

    memozization
    
    beats 16.87%

    for code while j < len(days) and days[j] < days[i] + d:
    it finds next day which needs to buy ticket to cover
    
    i.e. when days = [1, 2, 8], i = 0, days[0] = 1, d = 7
    since it needs days array index instead of the specific day, so we can't put i + d (0 + 7) as parameter index for next recursion 
    
    so it skips days covered by current ticket by looping j with while j < len(days) and days[j] < days[i] + d, and find j = 2 (days[2] = 8) to buy ticket
    """
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        def dfs(i): # i is the index of day which needs to buy ticket to cover
            if i == len(days):
                return 0
            if i in dp:
                return dp[i]

            dp[i] = float("inf")
            for d, c in zip([1, 7, 30], costs):
                j = i
                while j < len(days) and days[j] < days[i] + d: # find next day which needs to buy ticket to cover
                    j += 1
                dp[i] = min(dp[i], c + dfs(j))
            return dp[i]

        return dfs(0)

      """
      DP

      if traverse days index (i) in non-reversed order:
      dp[i] will lose the info of previous min value and only get min value when starting from current index

      if traverse days index (i) in reversed order:
      dp[i] will accumulate based on previous min value while index j moving right

      beats 80.90%
      """
      def mincostTicketsV0(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        for i in range(len(days) - 1, -1, -1):
            dp[i] = float("inf")
            for d, c in zip([1, 7, 30], costs):
                j = i
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], c + dp.get(j, 0))

        return dp[0]
