class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """
        https://www.youtube.com/watch?v=q5ANAl8Z458&list=PLot-Xpze53lfxD6l5pAGvCD4nPvWKU8Qo&index=19
        
        beats 28.19
        """
        stack = [] # pair [num, curLeftMin], mono-decreasing stack
        curMin = nums[0]

        for n in nums:
            while stack and n >= stack[-1][0]:
                stack.pop()
            if stack and n < stack[-1][0] and n > stack[-1][1]:
                return True

            stack.append([n, curMin]) 
            curMin = min(n, curMin)

        return False
