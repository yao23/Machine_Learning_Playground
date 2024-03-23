class Solution:
    """
    https://www.youtube.com/watch?v=cFabMOnJaq0&list=PLot-Xpze53lfxD6l5pAGvCD4nPvWKU8Qo&index=13
    
    beats 71.02%
    """
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while stack and stack[-1] > i and k > 0:
                k -= 1
                stack.pop()
            if stack or i is not "0":
                stack.append(i)
        if k:
            stack = stack[:-k]
        return ''.join(stack) or '0'
