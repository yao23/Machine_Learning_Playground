class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        https://www.youtube.com/watch?v=cTBiBSnjO3c&list=PLot-Xpze53lfxD6l5pAGvCD4nPvWKU8Qo&index=6
        
        beats 50.50%
        """
        res = [0] * len(temperatures)
        stack = [] # [temp, index], monolithic decreasing stack (decreaing from bottom to top)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIdx = stack.pop()
                res[stackIdx] = i - stackIdx
            stack.append([t, i])

        return res
