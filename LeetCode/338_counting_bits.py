class Solution(object):
    def countBits(self, n: int) -> List[int]:
        """
        https://www.youtube.com/watch?v=RyBM56RIWrM    

        beats 69.18%
        """
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if i == offset * 2: # update offset when i is power of 2 (i.e. 2, 4, 8, 16)
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
    
    def countBitsV0(self, num):
        """
        :type num: int
        :rtype: List[int]

        beats 94.38%
        """
        ini_arr = [0]
        if num > 0:
            while len(ini_arr) < num + 1:
                ini_arr.extend([x + 1 for x in ini_arr])

        return ini_arr[0:num + 1]
